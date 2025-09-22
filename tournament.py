import numpy as np
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/mcts_model.pkl")

# Define MCTS variants
variants = [
    {"name": "Variant A", "C": 1.2, "sim": 1500},
    {"name": "Variant B", "C": 2.0, "sim": 1200},
    {"name": "Variant C", "C": 1.5, "sim": 800},
    {"name": "Variant D", "C": 0.8, "sim": 1800},
    {"name": "Variant E", "C": 1.8, "sim": 1000},
]

# Predict win rate
def predict_win_rate(va, vb):
    features = pd.DataFrame([{
        "CA": va["C"], "simA": va["sim"],
        "CB": vb["C"], "simB": vb["sim"],
        "C_diff": va["C"] - vb["C"],
        "sim_diff": va["sim"] - vb["sim"]
    }])
    return model.predict(features)[0]

# Round-robin matchups
results = []
for i in range(len(variants)):
    for j in range(i+1, len(variants)):
        va, vb = variants[i], variants[j]
        win_rate_A = predict_win_rate(va, vb)
        results.append([va["name"], vb["name"], win_rate_A, 1 - win_rate_A])

df_results = pd.DataFrame(results, columns=["Player A", "Player B", "WinRate_A", "WinRate_B"])
print("\nMatchup predictions:")
print(df_results)

# --- Elo system ---
def elo_expected(ra, rb): return 1 / (1 + 10 ** ((rb - ra) / 400))
def update_elo(ratings, a, b, score_a, K=32):
    ra, rb = ratings[a], ratings[b]
    ea, eb = elo_expected(ra, rb), elo_expected(rb, ra)
    ratings[a] += K * (score_a - ea)
    ratings[b] += K * ((1 - score_a) - eb)

ratings = {v["name"]: 1500 for v in variants}
for _, row in df_results.iterrows():
    update_elo(ratings, row["Player A"], row["Player B"], row["WinRate_A"])

leaderboard = pd.DataFrame(ratings.items(), columns=["Variant", "Elo"]).sort_values("Elo", ascending=False)
print("\nLeaderboard:")
print(leaderboard)
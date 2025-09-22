import os
import numpy as np
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# --- Ensure directories exist ---
os.makedirs("data", exist_ok=True)
os.makedirs("models", exist_ok=True)

# --- Synthetic dataset generation ---
def simulate_match(C1, sims1, C2, sims2, n_games=10):
    """Simulate matches between two MCTS variants (very simplified)."""
    skill_A = sims1 * (1 / (1 + np.exp(-C1)))
    skill_B = sims2 * (1 / (1 + np.exp(-C2)))

    prob_A = skill_A / (skill_A + skill_B)
    wins_A = np.random.binomial(n_games, prob_A)
    return wins_A / n_games

def generate_dataset(n_pairs=300, matches_per_pair=12):
    rows = []
    for _ in range(n_pairs):
        C1, C2 = np.random.uniform(0.5, 2.0, size=2)
        sims1, sims2 = np.random.randint(50, 500, size=2)
        win_rate_A = simulate_match(C1, sims1, C2, sims2, n_games=matches_per_pair)

        rows.append({
            "CA": C1, "simA": sims1,
            "CB": C2, "simB": sims2,
            "C_diff": C1 - C2,
            "sim_diff": sims1 - sims2,
            "win_rate_A": win_rate_A
        })
    return pd.DataFrame(rows)

# --- Generate data ---
df = generate_dataset(n_pairs=300, matches_per_pair=12)

# Save dataset
dataset_path = os.path.join("data", "mcts_matchups.csv")
df.to_csv(dataset_path, index=False)

print(f"✅ Dataset saved to {dataset_path} with {len(df)} samples")

# --- Train/test split ---
X = df.drop(columns=["win_rate_A"])
y = df["win_rate_A"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Train model ---
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# --- Evaluate ---
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"📊 Model evaluation: MSE={mse:.4f}, R²={r2:.4f}")

# --- Save model ---
model_path = os.path.join("models", "mcts_model.pkl")
joblib.dump(model, model_path)

print(f"✅ Trained model saved to {model_path}")
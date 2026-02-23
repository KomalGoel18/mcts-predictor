🧩 MCTS Predictor
=================

A small machine learning project that predicts the outcome of Monte Carlo Tree Search (MCTS) variants when playing against each other in a given game.

The project:

- Trains a **RandomForestRegressor** on synthetic matchup data between pairs of MCTS parameter settings.
- Uses the trained model to **predict win rates** between variants.
- Runs round-robin **tournament simulations** and builds a simple **Elo-style leaderboard** of the variants.

## 📂 Project structure

```text
mcts-predictor/
├── data/           # Generated datasets (CSV, created by train_model.py)
├── models/         # Saved ML models (.pkl, created by train_model.py)
├── train_model.py  # Generate synthetic data & train the model
├── tournament.py   # Simulate tournaments & build an Elo leaderboard
├── requirements.txt# Python dependencies
├── README.md       # Project documentation (this file)
└── .gitignore
```

> Note: `data/` and `models/` are created automatically the first time you run `train_model.py`.

## ⚙️ Installation

**Prerequisites**

- **Python**: 3.9 or newer
- Recommended: a virtual environment (`venv`, `conda`, etc.)

**Clone the repository and install dependencies**

```bash
git clone <https://github.com/KomalGoel18/mcts-predictor>
cd mcts-predictor

python -m venv .venv

# Activate (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

## 🏋️ Training the model

The training script:

- Generates a synthetic dataset of MCTS variant matchups.
- Trains a `RandomForestRegressor` to predict the win rate of Variant A vs Variant B.
- Saves the dataset to `data/mcts_matchups.csv`.
- Saves the trained model to `models/mcts_model.pkl`.

Run:

```bash
python train_model.py
```

Example console output (values will vary):

```text
✅ Dataset saved to data\mcts_matchups.csv with 300 samples
📊 Model evaluation: MSE=0.0187, R²=0.6912
✅ Trained model saved to models\mcts_model.pkl
```

## 🎮 Running a tournament

Once the model has been trained and saved, you can run a simple round-robin tournament between predefined MCTS variants.

This will:

- Load the model from `models/mcts_model.pkl`.
- Define several variants (different values of exploration constant `C` and number of simulations).
- Predict win rates for every pair of variants.
- Build and print an Elo-style leaderboard.

Run:

```bash
python tournament.py
```

Example console output (truncated):

```text
Matchup predictions:
    Player A   Player B  WinRate_A  WinRate_B
0  Variant A  Variant B   0.662917   0.337083
1  Variant A  Variant C   0.690833   0.309167
2  Variant A  Variant D   0.432083   0.567917
...
9  Variant D  Variant E   0.629583   0.370417

Leaderboard:
     Variant          Elo
0  Variant A  1513.689926
3  Variant D  1508.904551
1  Variant B  1503.485131
4  Variant E  1490.021374
2  Variant C  1483.899018
```

## 🧠 How it works (high level)

- **Synthetic matches**  
  - `train_model.py` defines `simulate_match`, which takes two variants (each defined by `C` and number of simulations) and simulates a small number of games to estimate Variant A’s win rate.

- **Features used for prediction**
  - For each matchup, the dataset includes:
    - `CA`, `simA`: exploration constant and simulations for Variant A.
    - `CB`, `simB`: same for Variant B.
    - `C_diff`, `sim_diff`: differences between the two variants.
    - `win_rate_A`: empirical win rate of Variant A in the simulation.

- **Model**
  - A `RandomForestRegressor` is trained to predict `win_rate_A` from the above features.

- **Tournament**
  - `tournament.py` defines a list of named variants and uses the trained model to predict win rates for all pairs.
  - An Elo update rule is applied to build a leaderboard from these predicted outcomes.
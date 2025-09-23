🧩 MCTS Predictor

A machine learning model to predict the outcome of Monte Carlo Tree Search (MCTS) variants when playing against each other in a given game.

The project trains a RandomForestRegressor on synthetic matchup data and predicts win rates between different MCTS parameter settings.
It also runs tournament simulations and builds a simple Elo leaderboard of the variants.

📂 Project Structure
mcts-predictor/
│
├── data/                 # Generated datasets (CSV)
├── models/               # Saved ML models (.pkl)
├── notebooks/            # (Optional) Jupyter notebooks for analysis
├── train_model.py        # Train the model & save dataset + trained model
├── tournament.py         # Simulate tournaments & predict matchups
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation (this file)
└── .gitignore            # Ignore venv, cache, etc.

⚙️ Installation

Clone the repo and set up a virtual environment.

# Clone repo
git clone https://github.com/KomalGoel18/mcts-predictor.git
cd mcts-predictor

# Create virtual environment
python -m venv venv

# Activate (PowerShell)
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

🏋️ Training the Model

Run the training script to generate a dataset and train the ML model:

python train_model.py


Expected output:

✅ Dataset saved to data\mcts_matchups.csv with 300 samples
📊 Model evaluation: MSE=0.0187, R²=0.6912
✅ Trained model saved to models\mcts_model.pkl

🎮 Running a Tournament
python tournament.py


Example output:

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

📊 Tech Stack

Python 3.9+

scikit-learn → Model training (RandomForest)

pandas / numpy → Data handling

matplotlib → (Optional) visualization

joblib → Model persistence

🚀 Future Enhancements

Replace synthetic match generator with real game engine data (e.g., DeepMind OpenSpiel).

Add visualizations of win-rate distributions.

Implement other ML models (XGBoost, Neural Nets).

Extend leaderboard with different ranking systems.
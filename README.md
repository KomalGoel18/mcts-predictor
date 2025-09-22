# MCTS Predictor 🔮

This project predicts how well one Monte Carlo Tree Search (MCTS) variant will perform against another in a given game, using a machine learning model trained on synthetic matchups.

---

## 🚀 Features
- Generate synthetic MCTS matchup data
- Train a RandomForest regression model
- Predict win rates between MCTS variants
- Run round-robin tournaments
- Rank variants with Elo ratings

---

## 📂 Project Structure
mcts-predictor/
│── models/ # trained models
│ └── mcts_model.pkl
│── train_model.py # generate dataset & train model
│── tournament.py # simulate tournaments
│── requirements.txt # dependencies
│── .gitignore # ignored files
│── README.md # documentation

yaml
Copy code

---

## ⚙️ Installation
Clone the repo and install dependencies:
```bash
git clone https://github.com/your-username/mcts-predictor.git
cd mcts-predictor
pip install -r requirements.txt
📊 Usage
1. Train a new model
bash
Copy code
python train_model.py
This generates synthetic data, trains a RandomForest model, and saves it to models/mcts_model.pkl.

2. Run tournament simulation
bash
Copy code
python tournament.py
This loads the trained model, simulates round-robin matchups, and outputs an Elo leaderboard.

🧠 Example Output
less
Copy code
Matchup predictions:
    Player A   Player B  WinRate_A  WinRate_B
0  Variant A  Variant B   0.612345   0.387655
1  Variant A  Variant C   0.732101   0.267899
...

Leaderboard:
    Variant     Elo
0  Variant D  1532.8
1  Variant A  1511.2
2  Variant B  1488.7
...
📌 Notes
Dataset is not committed (can be regenerated).

Model is committed for quick use.

Extend variants list in tournament.py to test more configurations.

📜 License
MIT License – feel free to use, modify, and share.

yaml
Copy code

---

✅ With this setup:  
- Anyone can retrain (`train_model.py`).  
- Anyone can simulate tournaments (`tournament.py`).  
- Repo is light (no dataset bloat).  
- Professional structure + documentation.  

---
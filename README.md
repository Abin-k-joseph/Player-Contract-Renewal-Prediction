
# ⚽ Player Contract Renewal Decision Engine

A **Machine Learning–based decision support system** designed to help football clubs, scouting teams, and sporting directors decide whether a player’s contract should be **renewed or not** using data-driven insights.

---

## 📌 Project Description

This project predicts a football player’s **contract renewal eligibility** using Machine Learning.  
The model is trained on **performance metrics, injury history, tactical trust, and financial indicators** to support smarter contract decisions.

---

## 🗂️ Features Used

- Age  
- Position  
- Continent  
- Minutes Played  
- Goals Scored  
- Assists Provided  
- Defensive Impact  
- Injury Days  
- Market Value (€ Millions)  
- Contract Years Left  
- Coach Trust Score  
- Saves *(Goalkeepers only)*  

---

## ⚙️ Feature Engineering

- **Attack Contribution** = Goals + Assists  
- **Trust Adjusted Usage** = Minutes Played × Coach Trust Score  
- **Injury Risk Index** = Injury Days / Age  
- **Goalkeeper Effectiveness** = Saves / Minutes Played  

---

## 🤖 Machine Learning Model

- **Problem Type:** Binary Classification  
- **Target Variable:** `Renew_Contract`  
  - `1` → Renew Contract  
  - `0` → Do Not Renew  
- **Algorithm Used:** Random Forest Classifier  
- **Model Serialization:** Joblib  

---

## 🛠️ Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Streamlit  
- Joblib  

---

## ▶️ How to Run the Project

 Install dependencies & Run the Streamlit application :
```bash
pip install -r requirements.txt
python -m streamlit run app.py






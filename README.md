# 🏗️ Concrete Compressive Strength Prediction

## App link: 
https://concrete-compressive-strength-prediction-8ub6hfhpfwk7jakcsogcm.streamlit.app/
    
## 📖 Project Overview

This project predicts the compressive strength of concrete using a machine learning regression model.

Concrete strength depends on several input parameters like cement content, water ratio, age of curing, and other ingredients.

By training a model on historical data, we can estimate the strength of concrete for given mixtures and curing times.

The final application uses a Flask web app where users can input the concrete mixture details and get a predicted strength value instantly.

## 📌 Project Structure

📂 Concrete-Strength-Prediction

│── app.py   

│── concrete_data.csv

│── data.csv 

│── eda.ipynb

│── model.ipynb

│── model.pkl  

│── requirements.txt 

│── README.md             


## 📂 Dataset

Source: Concrete Compressive Strength Dataset (UCI Repository / Kaggle)

Target Variable: Concrete_compressive_strength (MPa)

Features:

Cement (kg/m³)

Blast Furnace Slag (kg/m³)

Fly Ash (kg/m³)

Water (kg/m³)

Superplasticizer (kg/m³)

Coarse Aggregate (kg/m³)

Fine Aggregate (kg/m³)

Age (days)

## ⚙️ Tech Stack

Python 🐍

Libraries:

pandas, numpy (data handling)

scikit-learn (machine learning)

matplotlib, seaborn (visualization)

ML Model: GradientBoostingRegressor

Framework: streamlit (for web application)

## 🔎 Exploratory Data Analysis (EDA)

During EDA, we explored:

Distribution of features (cement, water, etc.)

Correlation with compressive strength

Feature importance

📊 Visualizations used:

Histograms & KDE plots for feature distributions

Heatmap for correlation

Scatter plots of features vs. target

## 🧠 Model Training

Split data: 80% training, 20% testing

Model: GradientBoostingRegressor (best performance for regression task)

## Evaluation Metrics:

R² Score

Root Mean Squared Error (RMSE)

## 🚀 How to Run the Project

🔧 Installation

Install dependencies:

pip install -r requirements.txt

▶️ Run the App
streamlit run app.py

Enter input values (cement, water, age, etc.) and click Predict.

## 📊 Results

Best model: Gradient Boosting Regressor

Achieved R² score ~0.90+ (depending on dataset split)

Can accurately predict compressive strength within reasonable error range.

## Screenshot :
<img width="763" height="768" alt="image" src="https://github.com/user-attachments/assets/178b1096-6447-4884-966c-9e4eb8bf888b" />

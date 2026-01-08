# 🧑‍💼 Employee Attrition Prediction System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Machine Learning](https://img.shields.io/badge/Model-Random_Forest-green)
![Framework](https://img.shields.io/badge/App-Streamlit-red)
![Status](https://img.shields.io/badge/Status-Active-success)

A comprehensive Data Science project that helps HR departments predict employee turnover. This system generates synthetic HR data, trains a **Random Forest Classifier** to identify at-risk employees, and provides an interactive web interface for real-time predictions.

## 🚀 Overview

High employee turnover is costly for businesses. This project solves that problem by:
1.  **Simulating Realistic Data:** Generates a synthetic dataset of employee metrics (Satisfaction, Salary, Overtime, etc.).
2.  **Predictive Modeling:** Uses a Machine Learning model to analyze patterns and predict the probability of an employee leaving.
3.  **Decision Support:** Offers a user-friendly dashboard for HR managers to input employee details and get instant risk assessments.

## ✨ Features

* **Synthetic Data Pipeline:** Custom script to generate labeled HR datasets for training.
* **Machine Learning Model:** Implements a Random Forest Classifier with an accuracy of ~85-90%.
* **Interactive Dashboard:** Streamlit-based web app for real-time inference.
* **Risk Probability:** Outputs not just a "Yes/No" prediction, but a confidence score (e.g., "82% Risk").

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-Learn
* **App Framework:** Streamlit
* **Model Storage:** Joblib

## 📂 Project Structure

```
HRAtrition/
├── src/
│   ├── data_gen.py        # Generates synthetic HR data (hr_data.csv)
│   ├── model_train.py     # Trains the Random Forest model and saves it
├── app.py                 # Main Streamlit Dashboard
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation


```
💻 Installation & Usage
```
1. Clone the Repository
Bash

git clone [https://github.com/](https://github.com/Praneeth9346/HRAtrition.git
cd HRAtrition
2. Install Dependencies
Bash

pip install -r requirements.txt
3. Run the Application
You don't need to run the scripts manually. The app handles everything!

Bash

streamlit run app.py
```
First Run: The app will automatically detect if the model is missing, generate the data, and train the model for you.

Subsequent Runs: It will load the saved model instantly.

🔬 How It Works (Under the Hood)
Step 1: Data Generation
The src/data_gen.py script creates 2,000 synthetic employee records with features like:

Job Satisfaction: (1-4 Scale)

Overtime: (Yes/No)

Monthly Income: (Salary)

Years at Company: (0-40 years)

Attrition: (Target Variable - calculated based on a weighted formula of the above features)

Step 2: Model Training
The src/model_train.py script:

Loads the generated CSV.

Splits data into Training (80%) and Testing (20%) sets.

Trains a Random Forest Classifier (n_estimators=100).

Evaluates performance (Accuracy & F1-Score).

Saves the trained model as model.pkl.

Step 3: Deployment
The app.py loads model.pkl and takes user inputs via sliders and dropdowns to generate a live prediction.

🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

📝 License
Distributed under the MIT License.

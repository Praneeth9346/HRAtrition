import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
from src.data_gen import generate_hr_data

def train_model():
    print("⏳ Generating Data...")
    df = generate_hr_data(2000)
    
    # Features (X) and Target (y)
    X = df.drop('Attrition', axis=1)
    y = df['Attrition']
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train
    print("⏳ Training Random Forest...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"✅ Model Trained! Accuracy: {acc:.2%}")
    print(classification_report(y_test, preds))
    
    # Save
    joblib.dump(model, 'model.pkl')
    print("💾 Model saved to model.pkl")

if __name__ == "__main__":
    train_model()

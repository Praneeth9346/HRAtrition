import pandas as pd
import numpy as np
import random

def generate_hr_data(n_samples=2000):
    np.random.seed(42)
    
    data = []
    for _ in range(n_samples):
        age = np.random.randint(22, 60)
        daily_rate = np.random.randint(100, 1500)
        distance = np.random.randint(1, 30)
        education = np.random.randint(1, 5)
        satisfaction = np.random.randint(1, 4) # 1=Low, 4=High
        years_at_company = np.random.randint(0, 20)
        salary = np.random.randint(2000, 20000)
        overtime = np.random.choice([0, 1]) # 0=No, 1=Yes
        
        # Logic: Low satisfaction + Low Salary + Overtime = High Chance of Attrition
        score = (4 - satisfaction) * 2 + overtime * 3 + (1 if salary < 5000 else 0) * 2
        attrition = 1 if score > 5 + np.random.randn() else 0
        
        data.append([age, daily_rate, distance, education, satisfaction, years_at_company, salary, overtime, attrition])
        
    cols = ['Age', 'DailyRate', 'DistanceFromHome', 'Education', 'JobSatisfaction', 'YearsAtCompany', 'MonthlyIncome', 'OverTime', 'Attrition']
    df = pd.DataFrame(data, columns=cols)
    return df

if __name__ == "__main__":
    df = generate_hr_data()
    df.to_csv("hr_data.csv", index=False)
    print("✅ hr_data.csv created!")

import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()
records = 1000
data = []

for i in range(records):
    # Base Profile Logic
    # 0: Healthy, 1: At Risk (Burnout), 2: At Risk (Dropout)
    profile = np.random.choice([0, 1, 2], p=[0.7, 0.15, 0.15])
    
    name = fake.name()
    student_id = f"STU{1000 + i}"
    
    if profile == 1:  # Burnout Profile (High Library, Low Sleep)
        lib_hours = random.randint(30, 50)
        sleep_hours = random.uniform(3, 5)
        attendance = random.randint(90, 100)
        medical_visits = random.randint(2, 5) # Stress related
        risk_score = random.randint(70, 95)
    elif profile == 2:  # Dropout Profile (Low Attendance, Late Hostel)
        lib_hours = random.randint(0, 5)
        sleep_hours = random.uniform(8, 10)
        attendance = random.randint(30, 60)
        medical_visits = random.randint(0, 1)
        risk_score = random.randint(75, 98)
    else:  # Normal/Healthy
        lib_hours = random.randint(10, 20)
        sleep_hours = random.uniform(6, 8)
        attendance = random.randint(75, 95)
        medical_visits = random.randint(0, 1)
        risk_score = random.randint(5, 40)

    data.append({
        "student_id": student_id,
        "name": name,
        "library_hours_weekly": lib_hours,
        "avg_sleep_hours": round(sleep_hours, 1),
        "attendance_pct": attendance,
        "hostel_late_entries": random.randint(0, 10) if profile == 2 else random.randint(0, 2),
        "medical_issues": medical_visits,
        "burnout_risk": risk_score # This is our 'Label' for the AI to learn
    })

df = pd.DataFrame(data)
df.to_csv("student_data_1000.csv", index=False)
print("✅ Success! Generated 1,000 realistic student records in student_data_1000.csv")
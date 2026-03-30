import joblib
import pandas as pd
from fastapi import APIRouter, HTTPException
from app.models.behavioral import ActivityLog, MedicalRecord
from app.core.storage import activity_logs, medical_records

model = joblib.load("burnout_model.pkl")

router = APIRouter()

@router.post("/logs/activity")
async def log_activity(log: ActivityLog):
    activity_logs.append(log)
    return {"message": "Activity logged"}

@router.post("/logs/medical")
async def log_medical(record: MedicalRecord):
    medical_records.append(record)
    return {"message": "Medical record saved"}

# STUDENTS DATA
@router.get("/students")
async def get_students():
    df = pd.read_csv("student_data_1000.csv")
    return df.to_dict(orient="records")

# DASHBOARD OVERVIEW
@router.get("/analytics/overview")
async def analytics_overview():
    df = pd.read_csv("student_data_1000.csv")

    return {
        "total_students": len(df),
        "avg_attendance": round(df["attendance_pct"].mean(),2),
        "high_risk_students": int(len(df[df["burnout_risk"] > 80])),
        "medical_issues": int(df["medical_issues"].sum())
    }

# HIGH RISK ALERT
@router.get("/analytics/high-risk-students")
async def high_risk_students():
    df = pd.read_csv("student_data_1000.csv")
    high_risk = df[df["burnout_risk"] > 80]
    return high_risk.to_dict(orient="records")
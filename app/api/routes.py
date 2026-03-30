import joblib
import pandas as pd
from fastapi import APIRouter
from app.models.behavioral import ActivityLog, MedicalRecord
from app.core.storage import activity_logs, medical_records

model = joblib.load("burnout_model.pkl")

router = APIRouter()

# Activity logging
@router.post("/logs/activity")
async def log_activity(log: ActivityLog):
    activity_logs.append(log)
    return {
        "message": "Activity logged",
        "total_logs": len(activity_logs)
    }

# Medical logging
@router.post("/logs/medical")
async def log_medical(record: MedicalRecord):
    medical_records.append(record)
    return {
        "message": "Medical record saved",
        "total_records": len(medical_records)
    }

# IR dashboard
@router.get("/admin/ir-report")
async def get_institutional_report():
    df = pd.read_csv("student_data_1000.csv")

    high_risk = df[df["burnout_risk"] > 70]
    avg_attendance = df["attendance_pct"].mean()

    return {
        "total_students": len(df),
        "high_risk_students": len(high_risk),
        "average_campus_attendance": f"{avg_attendance:.2f}%",
        "status": "Critical" if len(high_risk) > 100 else "Stable"
    }

@router.get("/predict/{student_id}")
async def predict_risk(student_id: str):

    df = pd.read_csv("student_data_1000.csv")

    student = df[df["student_id"] == student_id]

    if student.empty:
        raise HTTPException(status_code=404, detail="Student not found")

    features = student[
        [
            "library_hours_weekly",
            "avg_sleep_hours",
            "attendance_pct",
            "hostel_late_entries",
            "medical_issues",
        ]
    ]

    risk_score = model.predict(features)[0]

    intervention = "Keep it up!"

    if risk_score > 75:
        intervention = "Urgent: Schedule counselor meeting"

    elif risk_score > 50:
        intervention = "Warning: Increase sleep duration"

    return {
        "student_name": student.iloc[0]["name"],
        "risk_score": round(float(risk_score), 2),
        "intervention": intervention,
    }
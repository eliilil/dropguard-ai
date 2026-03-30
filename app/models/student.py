from pydantic import BaseModel
from typing import Optional

class StudentRecord(BaseModel):
    student_id: str
    name: str
    library_hours_weekly: int
    avg_sleep_hours: float
    attendance_pct: int
    hostel_late_entries: int
    medical_issues: int
    burnout_risk: int

    class StudentInput(BaseModel):
    library_hours_weekly: int
    avg_sleep_hours: float
    attendance_pct: int
    hostel_late_entries: int
    medical_issues: int
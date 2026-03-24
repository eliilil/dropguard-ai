from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class DailyLog(BaseModel):
    student_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    
    # Academic Indicators
    attendance: bool
    study_hours: float = Field(..., ge=0, le=24)
    assignments_completed: int = Field(default=0)
    
    # Wellness Indicators (Psychology Metrics)
    mood_score: int = Field(..., ge=1, le=10)
    sleep_hours: float = Field(..., ge=0, le=24)
    stress_level: int = Field(..., ge=1, le=10)
    
    class Config:
        json_schema_extra = {
            "example": {
                "student_id": "S12345",
                "attendance": True,
                "study_hours": 4.5,
                "mood_score": 7,
                "sleep_hours": 6.5,
                "stress_level": 4
            }
        }
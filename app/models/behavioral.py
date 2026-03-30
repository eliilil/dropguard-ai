from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

# Enums (VERY IMPORTANT)
class Location(str, Enum):
    hostel = "hostel"
    library = "library"
    campus_gate = "campus_gate"

class Action(str, Enum):
    IN = "IN"
    OUT = "OUT"

class ActivityLog(BaseModel):
    student_id: str
    location: Location
    action: Action
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class MedicalRecord(BaseModel):
    student_id: str
    issue_type: str
    severity: int = Field(ge=1, le=10)  # validation
    days_off: int
    timestamp: datetime = Field(default_factory=datetime.utcnow)
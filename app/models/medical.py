from pydantic import BaseModel

class MedicalRecord(BaseModel):
    student_id: str
    severity: str
    category: str
    is_excused: bool
def calculate_isolation_score(hostel_hours, library_hours):
    if hostel_hours > library_hours * 2:
        return "High Isolation Risk"
    return "Normal"

def check_medical_risk(visit_count):
    if visit_count > 3:
        return "Medical Alert"
    return "Normal"
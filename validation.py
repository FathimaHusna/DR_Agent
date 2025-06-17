def validate_inputs(role, experience, skills, rate, tone):
    errors = []
    if not role.strip():
        errors.append("Role cannot be empty.")
    if not skills:
        errors.append("At least one skill is required.")
    if not rate.endswith("/hr"):
        errors.append("Rate must end with /hr (e.g., $25/hr).")
    if tone not in ["Professional", "Friendly", "Direct", "Inspiring"]:
        errors.append("Invalid tone selected.")
    return errors

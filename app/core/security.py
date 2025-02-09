class SecurityViolation(Exception):
    pass


def validate_path(path: str):
    if not path.startswith("/data"):
        raise SecurityViolation("Access outside /data directory prohibited")


def validate_task(task: dict):
    if any(step.get("action") == "delete" for step in task.get("steps", [])):
        raise SecurityViolation("Delete operations are prohibited")

    for step in task.get("steps", []):
        if "path" in step:
            validate_path(step["path"])


def initialize_security():
    # Initialize any security modules here
    pass

from app.core.llm_handler import parse_task_with_llm
from app.core.security import validate_task
from app.core.task_handlers import phase_a_handlers, phase_b_handlers
from app.utils.logger import logger


async def process_task(task_description: str):
    parsed_task = await parse_task_with_llm(task_description)
    validate_task(parsed_task)

    if parsed_task["phase"] == "A":
        handler = getattr(phase_a_handlers, f"handle_{parsed_task['task_id']}")
    else:
        handler = getattr(phase_b_handlers, f"handle_{parsed_task['task_type']}")

    return handler(parsed_task["parameters"])

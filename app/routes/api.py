from fastapi import APIRouter, HTTPException
from app.core.task_processor import process_task
from app.core.file_ops import read_file

router = APIRouter()

@router.post("/run")
async def execute_task(task: str):
    try:
        result = await process_task(task)
        return {"status": "success", "result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/read")
async def read_file_endpoint(path: str):
    try:
        return read_file(path)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")

from fastapi import FastAPI
from app.routes.api import router
from app.core.security import initialize_security

app = FastAPI()
app.include_router(router)
initialize_security()

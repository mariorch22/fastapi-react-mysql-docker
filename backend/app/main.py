from fastapi import FastAPI
from app.db.base import Base  # Neue Import
from app.db.session import engine
from app.middleware.test import add_process_time_header
from app.middleware.cors import cors_middleware
from app.api.endpoints import root
from app.api.endpoints import user

# scans all classes which inherit from Base and creates the tables
Base.metadata.create_all(bind=engine)
app = FastAPI()

app.middleware("http")(add_process_time_header)
app.middleware("http")(cors_middleware)

# Include routers
app.include_router(root.router)
app.include_router(user.router)

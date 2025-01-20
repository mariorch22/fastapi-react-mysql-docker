from pydantic import BaseModel  # Neue Import


# Pydantic Model für Request Validierung
class UserCreate(BaseModel):
    name: str
    email: str

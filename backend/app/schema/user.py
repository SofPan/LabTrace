import uuid

from pydantic import BaseModel, ConfigDict, Field

from app.models.user import UserRole


class UserCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    role: UserRole


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    role: UserRole
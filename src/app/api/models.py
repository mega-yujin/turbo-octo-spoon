from pydantic import BaseModel, Field


class ORMBaseModel(BaseModel):
    class Config:
        orm_mode = True


class BaseResponse(BaseModel):
    result: str = Field(default='ok')
    detail: str

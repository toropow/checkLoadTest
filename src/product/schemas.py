from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

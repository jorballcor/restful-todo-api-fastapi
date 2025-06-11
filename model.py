from pydantic import BaseModel

class todo_schema(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
    
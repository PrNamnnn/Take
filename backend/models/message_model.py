from pydantic import BaseModel
from typing import Optional

class Message(BaseModel):
    message : str

class Save_task(BaseModel):
    title : str
    subheading : str
    content : str

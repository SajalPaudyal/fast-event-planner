from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id:int
    title:str
    image:str
    description:str
    tags:List[str]
    location:str

    class Config:
        schema_extra = {
            "example" : {
                "title":"Complete the basics of FastAPI",
                "image":"https://linktomyimage.com/image.png",
                "description":"a beautiful image",
                "tags":["python","fastAPI","new project"],
                "location":"New Baneshwor, Kathmandu, Nepal"
            }
        }

    
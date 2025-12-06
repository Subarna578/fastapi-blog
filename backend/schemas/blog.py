from pydantic import BaseModel, model_validator
from datetime import datetime
from typing import Optional

class BlogCreate(BaseModel):
    title: str 
    slug: str 
    content: Optional[str]= None

    @model_validator(mode='before')
    @classmethod
    def generate_slug(cls, values):
        if isinstance(values, dict) and 'title' in values:
            values["slug"] = values.get("title").replace(" ", "-").lower()
        return values

class UpdateBlog(BlogCreate):
    is_active : bool
    pass 

    
class ShowBlog(BaseModel):
    title: str
    content: Optional[str]
    created_at: datetime

    class Config():
        from_attributes = True

from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True

class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int

    class Config:
        from_attributes = True
        
class PortfolioBase(BaseModel):
    title: str
    description: str
    technologies: Optional[str] = None
    github_link: Optional[str] = None
    live_demo_link: Optional[str] = None
    image_url: Optional[str] = None
    category_id: Optional[int] = None
    tag_ids: Optional[List[int]] = []

class PortfolioCreate(PortfolioBase):
    pass

class PortfolioUpdate(PortfolioBase):
    pass

class PortfolioResponse(PortfolioBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class Portfolio(PortfolioBase):
    id: int
    category: Optional[Category] = None
    tags: List[Tag] = []

    class Config:
        from_attributes = True
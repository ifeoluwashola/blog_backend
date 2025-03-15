from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional

class AboutMeBase(BaseModel):
    name: str
    bio: str
    email: EmailStr
    profile_picture: Optional[HttpUrl] = None
    github: Optional[HttpUrl] = None
    linkedin: Optional[HttpUrl] = None
    twitter: Optional[HttpUrl] = None

class AboutMeCreate(AboutMeBase):
    """Schema for creating or updating the about section."""
    pass

class AboutMeResponse(AboutMeBase):
    """Schema for returning about me data."""
    id: int

    class Config:
        from_attributes = True

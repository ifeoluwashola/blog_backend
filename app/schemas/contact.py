from pydantic import BaseModel, EmailStr
from datetime import datetime

class ContactMessageBase(BaseModel):
    name: str
    email: EmailStr
    subject: str
    message: str

class ContactMessageCreate(ContactMessageBase):
    """Schema for creating a new contact message."""
    pass

class ContactMessageResponse(ContactMessageBase):
    """Schema for returning contact message data."""
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

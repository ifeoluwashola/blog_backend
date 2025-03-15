from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.contact import ContactMessageCreate, ContactMessageResponse
from app.services import contact as service
from typing import List

router = APIRouter()

@router.post("/create_contact_message/", response_model=ContactMessageResponse, status_code=status.HTTP_201_CREATED)
def submit_contact_message(message: ContactMessageCreate, db: Session = Depends(get_db)):
    """Submit a new contact message."""
    return service.create_contact_message(db, message)

@router.get("/list_contact_messages/", response_model=List[ContactMessageResponse])
def get_all_contact_messages(db: Session = Depends(get_db)):
    """Retrieve all contact messages (for admin only)."""
    return service.list_contact_messages(db)

@router.get("/get_contact_message/{message_id}", response_model=ContactMessageResponse)
def get_contact_message_by_id(message_id: int, db: Session = Depends(get_db)):
    """Retrieve a specific contact message by ID."""
    message = service.get_contact_message(db, message_id)
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    return message
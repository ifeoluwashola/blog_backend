from sqlalchemy.orm import Session
from app.models.contact import ContactMessage
from app.schemas.contact import ContactMessageCreate

def create_contact_message(db: Session, message: ContactMessageCreate):
    """Store a new contact message in the database."""
    db_message = ContactMessage(**message.model_dump())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def list_contact_messages(db: Session):
    """Retrieve all contact messages."""
    return db.query(ContactMessage).order_by(ContactMessage.created_at.desc()).all()

def get_contact_message(db: Session, message_id: int):
    """Retrieve a specific contact message by ID."""
    return db.query(ContactMessage).filter(ContactMessage.id == message_id).first()

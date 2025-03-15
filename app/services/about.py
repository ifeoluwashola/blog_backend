from sqlalchemy.orm import Session
from app.models.about import AboutMe
from app.schemas.about import AboutMeCreate

def create_or_update_about_me(db: Session, about_data: AboutMeCreate):
    """Create or update the About Me section (only one entry should exist)."""
    db_about = db.query(AboutMe).first()

    if db_about:
        for key, value in about_data.model_dump().items():
            setattr(db_about, key, value)
    else:
        db_about = AboutMe(**about_data.model_dump())
        db.add(db_about)
    
    db.commit()
    db.refresh(db_about)
    return db_about

def get_about_me(db: Session):
    """Retrieve the about me section (only one record)."""
    return db.query(AboutMe).first()

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.about import AboutMeCreate, AboutMeResponse
from app.services import about as service

router = APIRouter()

@router.post("/update/", response_model=AboutMeResponse, status_code=status.HTTP_201_CREATED)
def update_about_me(about_data: AboutMeCreate, db: Session = Depends(get_db)):
    """Create or update the About Me section."""
    return service.create_or_update_about_me(db, about_data)

@router.get("/list/", response_model=AboutMeResponse)
def retrieve_about_me(db: Session = Depends(get_db)):
    """Retrieve the About Me section."""
    about = service.get_about_me(db)
    if not about:
        raise HTTPException(status_code=404, detail="No About Me section found")
    return about
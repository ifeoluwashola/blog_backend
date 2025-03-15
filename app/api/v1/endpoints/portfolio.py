from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.portfolio import PortfolioCreate, PortfolioUpdate, PortfolioResponse, Portfolio, CategoryCreate, Category, TagCreate, Tag
from app.services import portfolio as services
from app.services.user import get_current_user
from typing import List

router = APIRouter()

@router.post("/categories/create/", response_model=Category)
def create_category(category: CategoryCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return services.create_category(db, category)

@router.get("/categories/list/", response_model=List[Category])
def get_categories(db: Session = Depends(get_db)):
    return services.get_categories(db)

@router.post("/tags/create/", response_model=Tag)
def create_tag(tag: TagCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return services.create_tag(db, tag)

@router.get("/tags/list/", response_model=List[Tag])
def get_tags(db: Session = Depends(get_db)):
    return services.get_tags(db)

@router.post("/create_project/", response_model=PortfolioResponse, status_code=status.HTTP_201_CREATED)
def create_project(
    project: PortfolioCreate, 
    db: Session = Depends(get_db), 
    current_user=Depends(get_current_user)
):
    return services.create_project(db, project, current_user)

@router.put("/update_project/{project_id}", response_model=PortfolioResponse)
def update_project(
    project_id: int, 
    project: PortfolioUpdate, 
    db: Session = Depends(get_db), 
    current_user=Depends(get_current_user)
):
    return services.update_project(db, project_id, project, current_user)

@router.get("/list_projects/", response_model=List[PortfolioResponse])
def list_projects(db: Session = Depends(get_db)):
    return services.get_all_projects(db)

@router.get("/get_project/{project_id}", response_model=PortfolioResponse)
def get_project(project_id: int, db: Session = Depends(get_db)):
    return services.get_project_by_id(db, project_id)

@router.delete("/delete/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return services.delete_project(db, project_id, current_user)

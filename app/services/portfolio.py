from sqlalchemy.orm import Session
from app.models.portfolio import Portfolio, Category, Tag
from app.schemas.portfolio import PortfolioCreate, CategoryCreate, TagCreate, PortfolioUpdate, PortfolioPaginatedResponse, PortfolioResponse
from fastapi import HTTPException
from typing import List, Dict

def create_category(db: Session, category: CategoryCreate):
    """Creates a new category."""
    db_category = Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session) -> List[Category]:
    """Retrieve all categories."""
    return db.query(Category).all()

def create_tag(db: Session, tag: TagCreate):
    """Creates a new tag."""
    db_tag = Tag(name=tag.name)
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def get_tags(db: Session) -> List[Tag]:
    """Retrieve all tags."""
    return db.query(Tag).all()

def create_project(db: Session, project: PortfolioCreate, current_user):
    """Creates a new portfolio project with categories and tags."""
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admin can create projects.")

    db_project = Portfolio(
        title=project.title,
        description=project.description,
        technologies=project.technologies,
        github_link=project.github_link,
        live_demo_link=project.live_demo_link,
        image_url=project.image_url,
        category_id=project.category_id,
    )

    # Assign Tags
    if project.tag_ids:
        tags = db.query(Tag).filter(Tag.id.in_(project.tag_ids)).all()
        db_project.tags = tags

    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def update_project(db: Session, project_id: int, project_update: PortfolioUpdate, current_user):
    """Only admin can update projects."""
    db_project = db.query(Portfolio).filter(Portfolio.id == project_id).first()
    
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized to update projects")

    for key, value in project_update.model_dump(exclude_unset=True).items():
        setattr(db_project, key, value)

    db.commit()
    db.refresh(db_project)
    return db_project

def get_all_projects(db: Session, limit: int, offset: int) -> PortfolioPaginatedResponse:
    """Retrieve paginated list of portfolio projects."""
    total_count = db.query(Portfolio).count()
    projects = db.query(Portfolio).limit(limit).offset(offset).all()
    return PortfolioPaginatedResponse(
        total=total_count, 
        projects=[PortfolioResponse.model_validate(project) for project in projects]
        )

def get_project_by_id(db: Session, project_id: int):
    """Retrieve a project by ID."""
    db_project = db.query(Portfolio).filter(Portfolio.id == project_id).first()
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

def delete_project(db: Session, project_id: int, current_user):
    """Only admin can delete projects."""
    db_project = db.query(Portfolio).filter(Portfolio.id == project_id).first()
    
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized to delete projects")

    db.delete(db_project)
    db.commit()
    return {"message": "Project deleted successfully"}

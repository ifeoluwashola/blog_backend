from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base


# Association table for Many-to-Many relationship between Portfolio and Tags
portfolio_tags = Table(
    "portfolio_tags",
    Base.metadata,
    Column("portfolio_id", Integer, ForeignKey("portfolio.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tag.id"), primary_key=True),
)

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    # One-to-Many relationship with Portfolio
    projects = relationship("Portfolio", back_populates="category")

class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    # Many-to-Many relationship with Portfolio
    projects = relationship("Portfolio", secondary=portfolio_tags, back_populates="tags")

class Portfolio(Base):
    __tablename__ = "portfolio"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    technologies = Column(String(255), nullable=True)  # Comma-separated list of technologies
    github_link = Column(String(255), nullable=True)
    live_demo_link = Column(String(255), nullable=True)
    image_url = Column(String(255), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
        # ForeignKey to Category
    category_id = Column(Integer, ForeignKey("category.id"))
    category = relationship("Category", back_populates="projects")

    # Many-to-Many relationship with Tags
    tags = relationship("Tag", secondary=portfolio_tags, back_populates="projects")

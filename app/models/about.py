from sqlalchemy import Column, Integer, String, Text
from app.db.base_class import Base

class AboutMe(Base):
    """Model to store admin's about me details."""
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    bio = Column(Text, nullable=False)
    profile_picture = Column(String(255), nullable=True)
    email = Column(String(100), nullable=False)
    github = Column(String(255), nullable=True)
    linkedin = Column(String(255), nullable=True)
    twitter = Column(String(255), nullable=True)

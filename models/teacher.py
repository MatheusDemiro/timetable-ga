from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from settings import Base
from models.lesson import Lesson


class Teacher(Base):
    __tablename__ = 'teacher'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    lessons = relationship(Lesson, backref="teacher_lesson")
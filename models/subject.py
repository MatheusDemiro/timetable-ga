from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from settings import Base
from models.lesson import Lesson


class Subject(Base):
    __tablename__ = 'subject'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    code = Column(String(255))
    period = Column(Integer)
    shift = Column(String(1))
    lessons_per_week = Column(Integer)
    lessons = relationship(Lesson, backref="subject_lesson")

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.teacher import Teacher
from settings import Base


class Availability(Base):
    __tablename__ = 'availability'

    id = Column(Integer, primary_key=True)
    day_of_week = Column(Integer)
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    teacher = relationship(Teacher, backref="teacher_availability")

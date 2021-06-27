from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from settings import Base


class Lesson(Base):
    __tablename__ = 'lesson'

    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey('subject.id'))
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    semester = Column(String(6))
    teacher = relationship('Teacher', lazy='subquery')
    subject = relationship('Subject', lazy='subquery')

    def __str__(self):
        return "Lesson %d: (%s, %s, %s, %s, %d)" % (self.id, self.subject.code, self.subject.name, self.teacher.name,
                                                    self.semester, self.subject.lessons_per_week)

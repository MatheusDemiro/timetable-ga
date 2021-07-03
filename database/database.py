from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.availability import Availability
from models.subject import Subject
from models.teacher import Teacher
from models.lesson import Lesson
from settings import Base
from settings import SQLALCHEMY_URI


class Database:
    def __init__(self):
        self.engine = create_engine(SQLALCHEMY_URI)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def get_availability(self):
        availabilities = self.session.query(Availability).all()

        self.session.close()

        return availabilities

    def get_teachers(self):
        teachers = self.session.query(Teacher).all()

        self.session.close()

        return teachers

    def get_subjects(self):
        subjects = self.session.query(Subject).all()

        self.session.close()

        return subjects

    def get_lessons(self):
        lessons = self.session.query(Lesson).all()

        self.session.close()

        return lessons

    def create_database(self):
        Base.metadata.create_all(self.engine, tables=[Subject.__table__, Teacher.__table__, Lesson.__table__,
                                                      Availability.__table__])

    def populate_database(self):
        teachers = [
            Teacher(id=1, name="LUCIANO"),
            Teacher(id=2, name="FLAVIUS"),
            Teacher(id=3, name="JOÃO PAULO"),
            Teacher(id=4, name="LUIZ PAULO"),
            Teacher(id=5, name="GILSON"),
            Teacher(id=6, name="KARLIANE"),
            Teacher(id=7, name="FABRÍCIO"),
            Teacher(id=8, name="DEILSON")
        ]

        subjects = [
            Subject(id=1, name="FUNDAMENTOS DE MATEMÁTICA", code="FMAT", period=1, lessons_per_week=2),
            Subject(id=2, name="ALGORITMOS E LÓGICA DE PROGRAMAÇÃO", code="ALGLP", period=1, lessons_per_week=3),
            Subject(id=3, name="LÓGICA", code="LOG", period=1, lessons_per_week=2),
            Subject(id=4, name="ESTRUTURA DE DADOS", code="ED", period=2, lessons_per_week=3),
            Subject(id=5, name="INTRODUÇÃO A INFORMÁTICA", code="II", period=1, lessons_per_week=2),
            Subject(id=6, name="TEORIA GERAL DA ADMINISTRAÇÃO", code="TGA", period=1, lessons_per_week=2),
            Subject(id=7, name="FUNDAMENTOS DE SISTEMAS DE INFORMAÇÃO", code="FSI", period=2, lessons_per_week=2),
            Subject(id=8, name="ORGANIZAÇÃO SISTEMAS E MÉTODOS", code="OSM", period=2, lessons_per_week=2),
            Subject(id=9, name="PROGRAMAÇÃO ORIENTADA A OBJETOS I", code="POOI", period=2, lessons_per_week=2),
            Subject(id=10, name="ÁLGEBRA LINEAR", code="AL", period=2, lessons_per_week=2)

        ]

        lessons = [
            Lesson(id=1, subject_id=1, teacher_id=1, semester="2012.1", teacher=teachers[0], subject=subjects[0]),
            Lesson(id=2, subject_id=2, teacher_id=2, semester="2012.1", teacher=teachers[1], subject=subjects[1]),
            Lesson(id=3, subject_id=3, teacher_id=3, semester="2012.1", teacher=teachers[2], subject=subjects[2]),
            Lesson(id=4, subject_id=4, teacher_id=3, semester="2012.1", teacher=teachers[2], subject=subjects[3]),
            Lesson(id=5, subject_id=5, teacher_id=4, semester="2012.1", teacher=teachers[3], subject=subjects[4]),
            Lesson(id=6, subject_id=6, teacher_id=5, semester="2012.1", teacher=teachers[4], subject=subjects[5]),
            Lesson(id=7, subject_id=7, teacher_id=5, semester="2012.1", teacher=teachers[4], subject=subjects[6]),
            Lesson(id=8, subject_id=8, teacher_id=6, semester="2012.1", teacher=teachers[5], subject=subjects[7]),
            Lesson(id=9, subject_id=9, teacher_id=7, semester="2012.1", teacher=teachers[6], subject=subjects[8]),
            Lesson(id=10, subject_id=10, teacher_id=8, semester="2012.1", teacher=teachers[7], subject=subjects[9])
        ]

        availabilities = [
            Availability(id=1, teacher_id=1, day_of_week=1, teacher=teachers[0]),
            Availability(id=2, teacher_id=1, day_of_week=4, teacher=teachers[0]),
            Availability(id=3, teacher_id=2, day_of_week=0, teacher=teachers[1]),
            Availability(id=4, teacher_id=2, day_of_week=3, teacher=teachers[1]),
            Availability(id=5, teacher_id=3, day_of_week=1, teacher=teachers[2]),
            Availability(id=6, teacher_id=3, day_of_week=3, teacher=teachers[2]),
            Availability(id=7, teacher_id=4, day_of_week=0, teacher=teachers[3]),
            Availability(id=8, teacher_id=4, day_of_week=4, teacher=teachers[3]),
            Availability(id=9, teacher_id=5, day_of_week=1, teacher=teachers[4]),
            Availability(id=10, teacher_id=5, day_of_week=2, teacher=teachers[4]),
            Availability(id=11, teacher_id=5, day_of_week=0, teacher=teachers[4]),
            Availability(id=12, teacher_id=6, day_of_week=0, teacher=teachers[5]),
            Availability(id=13, teacher_id=6, day_of_week=1, teacher=teachers[5]),
            Availability(id=14, teacher_id=7, day_of_week=1, teacher=teachers[6]),
            Availability(id=15, teacher_id=7, day_of_week=2, teacher=teachers[6]),
            Availability(id=16, teacher_id=8, day_of_week=2, teacher=teachers[7]),
            Availability(id=17, teacher_id=8, day_of_week=3, teacher=teachers[7]),
        ]

        self.session.bulk_save_objects(teachers)
        self.session.bulk_save_objects(subjects)
        self.session.bulk_save_objects(lessons)
        self.session.bulk_save_objects(availabilities)
        self.session.commit()

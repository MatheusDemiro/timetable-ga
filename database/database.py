from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.unified_database import UnifiedDatabase
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
        self.teachers = [
            Teacher(name="LUCIANO"),  # 0
            Teacher(name="FLAVIUS"),  # 1
            Teacher(name="JOÃO PAULO"),  # 2
            Teacher(name="LUIZ PAULO"),  # 3
            Teacher(name="GILSON"),  # 4
            Teacher(name="KARLIANE"),  # 5
            Teacher(name="FABRÍCIO"),  # 6
            Teacher(name="DELSON"),  # 7
            Teacher(name="TACIANO"),  # 8
            Teacher(name="JOÃO BORGES"),  # 9
            Teacher(name="CELSO"),  # 10
            Teacher(name="ROGÉRIO"),  # 11
            Teacher(name="JOSÉ ENÉAS"),  # 12
            Teacher(name="DÉSIO"),  # 13
            Teacher(name="CÉLIA"),  # 14
            Teacher(name="LEOMARQUES"),  # 15
            Teacher(name="RICARDO"),  # 16
            Teacher(name="TALITHA"),  # 17
            Teacher(name="VYRNA"),  # 18
            Teacher(name="CARLOS"),  # 19
            Teacher(name="KARLIANE E LUIZ PAULO"),  # 20
            Teacher(name="TIAGO")  # 21
        ]

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
        Base.metadata.create_all(self.engine, tables=[Subject.__table__,
                                                      Teacher.__table__,
                                                      Lesson.__table__,
                                                      Availability.__table__])

    def create_teachers(self):
        self.session.bulk_save_objects(self.teachers, True)

    def create_unified_database(self):
        unified_database = UnifiedDatabase(self.teachers, self.session)

        unified_database.period1()
        unified_database.period2()
        unified_database.period3()
        unified_database.period4()
        unified_database.period5()
        unified_database.period6()
        unified_database.period7()
        unified_database.period8()

        unified_database.save_availabilities()

    def populate_database_20121(self):
        subjects = [
            Subject(name="FUNDAMENTOS DE MATEMÁTICA", code="FMAT", period=1, lessons_per_week=2, shift='T'),
            Subject(name="ALGORITMOS E LÓGICA DE PROGRAMAÇÃO", code="ALG", period=1, lessons_per_week=3, shift='T'),
            Subject(name="LÓGICA", code="LOG", period=1, lessons_per_week=2, shift='T'),
            Subject(name="INTRODUÇÃO A INFORMÁTICA", code="II", period=1, lessons_per_week=2, shift='T'),
            Subject(name="TEORIA GERAL DA ADMINISTRAÇÃO", code="TGA", period=1, lessons_per_week=2, shift='T'),
            Subject(name="ESTRUTURA DE DADOS", code="ED", period=3, lessons_per_week=3, shift='T'),
            Subject(name="FUNDAMENTOS DE SISTEMAS DE INFORMAÇÃO", code="FSI", period=3, lessons_per_week=2, shift='T'),
            Subject(name="ORGANIZAÇÃO SISTEMAS E MÉTODOS", code="OSM", period=3, lessons_per_week=2, shift='T'),
            Subject(name="PROGRAMAÇÃO ORIENTADA A OBJETOS I", code="POOI", period=3, lessons_per_week=2, shift='T'),
            Subject(name="ÁLGEBRA LINEAR", code="AL", period=3, lessons_per_week=2, shift='T'),
            Subject(name="EMPREENDEDORISMO EM INFORMÁTICA", code="EMP", period=5, lessons_per_week=2, shift='T'),
            Subject(name="ENGENHARIA DE SOFTWARE II", code="ES2", period=5, lessons_per_week=2, shift='T'),
            Subject(name="PROGRAMAÇÃO WEB", code="PWEB", period=5, lessons_per_week=2, shift='T'),
            Subject(name="PROJETO E ADMIN. DE BANCO DE DADOS", code="PABD", period=5, lessons_per_week=2, shift='T'),
            Subject(name="SISTEMAS OPERACIONAIS", code="SO", period=5, lessons_per_week=2, shift='T'),
            Subject(name="DIREITO E LEGISLAÇÃO SOCIAL", code="DIR", period=7, lessons_per_week=2, shift='T'),
            Subject(name="MATEMÁTICA FINANCEIRA", code="MATF", period=7, lessons_per_week=2, shift='T'),
            Subject(name="CONTABILIDADE E CUSTOS", code="CEC", period=7, lessons_per_week=3, shift='T'),
            Subject(name="GESTÃO DE PROJETO DE SOFTWARE", code="GPS", period=7, lessons_per_week=2, shift='T'),
            Subject(name="SISTEMA DE APOIO A DECISÃO", code="SAD", period=7, lessons_per_week=2, shift='T'),
        ]

        self.session.bulk_save_objects(subjects, True)

        '''
        PERÍODO 2 (2012.2)
            Subject(id=11, name="CÁLCULO DIFERENCIAL E INTEGRAL", code="CDI", period=2, lessons_per_week=2),
            Subject(id=12, name="LEITURA E PRODUÇÃO DE TEXTO", code="LPT", period=2, lessons_per_week=2),
            Subject(id=13, name="PROGRAMAÇÃO", code="PROG", period=2, lessons_per_week=2),
            Subject(id=14, name="METODOLOGIA DO TRABALHO CIENTÍFICO", code="MTC", period=2, lessons_per_week=2),
            Subject(id=15, name="TEORIA GERAL DE SISTEMAS", code="TGS", period=2, lessons_per_week=2),
        '''

        lessons = [
            Lesson(subject_id=subjects[0].id, teacher_id=self.teachers[0].id, semester="2012.1", teacher=self.teachers[0], subject=subjects[0]),
            Lesson(subject_id=subjects[1].id, teacher_id=self.teachers[1].id, semester="2012.1", teacher=self.teachers[1], subject=subjects[1]),
            Lesson(subject_id=subjects[2].id, teacher_id=self.teachers[2].id, semester="2012.1", teacher=self.teachers[2], subject=subjects[2]),
            Lesson(subject_id=subjects[3].id, teacher_id=self.teachers[3].id, semester="2012.1", teacher=self.teachers[3], subject=subjects[3]),
            Lesson(subject_id=subjects[4].id, teacher_id=self.teachers[4].id, semester="2012.1", teacher=self.teachers[4], subject=subjects[4]),
            Lesson(subject_id=subjects[5].id, teacher_id=self.teachers[2].id, semester="2012.1", teacher=self.teachers[2], subject=subjects[5]),
            Lesson(subject_id=subjects[6].id, teacher_id=self.teachers[4].id, semester="2012.1", teacher=self.teachers[4], subject=subjects[6]),
            Lesson(subject_id=subjects[7].id, teacher_id=self.teachers[5].id, semester="2012.1", teacher=self.teachers[5], subject=subjects[7]),
            Lesson(subject_id=subjects[8].id, teacher_id=self.teachers[6].id, semester="2012.1", teacher=self.teachers[6], subject=subjects[8]),
            Lesson(subject_id=subjects[9].id, teacher_id=self.teachers[7].id, semester="2012.1", teacher=self.teachers[7], subject=subjects[9]),
            Lesson(subject_id=subjects[10].id, teacher_id=self.teachers[4].id, semester="2012.1", teacher=self.teachers[4], subject=subjects[10]),
            Lesson(subject_id=subjects[11].id, teacher_id=self.teachers[8].id, semester="2012.1", teacher=self.teachers[8], subject=subjects[11]),
            Lesson(subject_id=subjects[12].id, teacher_id=self.teachers[6].id, semester="2012.1", teacher=self.teachers[6], subject=subjects[12]),
            Lesson(subject_id=subjects[13].id, teacher_id=self.teachers[8].id, semester="2012.1", teacher=self.teachers[8], subject=subjects[13]),
            Lesson(subject_id=subjects[14].id, teacher_id=self.teachers[9].id, semester="2012.1", teacher=self.teachers[9], subject=subjects[14]),
            Lesson(subject_id=subjects[15].id, teacher_id=self.teachers[11].id, semester="2012.1", teacher=self.teachers[11], subject=subjects[15]),
            Lesson(subject_id=subjects[16].id, teacher_id=self.teachers[0].id, semester="2012.1", teacher=self.teachers[0], subject=subjects[16]),
            Lesson(subject_id=subjects[17].id, teacher_id=self.teachers[10].id, semester="2012.1", teacher=self.teachers[10], subject=subjects[17]),
            Lesson(subject_id=subjects[18].id, teacher_id=self.teachers[5].id, semester="2012.1", teacher=self.teachers[5], subject=subjects[18]),
            Lesson(subject_id=subjects[19].id, teacher_id=self.teachers[1].id, semester="2012.1", teacher=self.teachers[1], subject=subjects[19]),
        ]

        self.session.bulk_save_objects(lessons, True)

        '''
        FMAT - Luciano - ID 1 - 0,1,2,3 - SEG,TER,QUA,QUI
        ALG - FLAVIUS - ID 2 - 0,1,2,3 - SEG,TER,QUA,QUI
        LOG,ED - JOÃO PAULO - ID 3 - 0,1,2,3,4 - SEG,TER,QUA,QUI,SEX
        II - LUIZ PAULO - ID 4 - 1,3 - TER,QUI
        TGA,FSI,EMP - GILSON - ID 5 - 2,3,4 - QUA,QUI,SEX
        OSM - KARLIANE - ID 6 - 0,1,2,3,4 - SEG,TER,QUA,QUI,SEX
        POOI,PWEB - FABRÍCIO - ID 7 - 0,1,2,4 - SEG,TER,QUA,SEX
        AL - DEILSON - ID 8 - 0,1,2,3,4 - SEG,TER,QUA,QUI,SEX
        ESII, PABD - TACIANO - ID 9 - 0,1,2,3,4 - SEG,TER,QUA,QUI,SEX
        SO - JOÃO BORGES - ID 10 - 0,1,2,3 - SEG,TER,QUA,QUI
        CEC - CELSO - ID 11 - 0,1,2 - SEG,TER,QUA
        DIR - ROGÉRIO - ID 12 - 3,4 - QUI,SEX
        '''

        availabilities = [
            Availability(teacher_id=self.teachers[0].id, day_of_week=0, teacher=self.teachers[0]),
            Availability(teacher_id=self.teachers[0].id, day_of_week=1, teacher=self.teachers[0]),
            Availability(teacher_id=self.teachers[0].id, day_of_week=2, teacher=self.teachers[0]),
            Availability(teacher_id=self.teachers[0].id, day_of_week=3, teacher=self.teachers[0]),
            Availability(teacher_id=self.teachers[1].id, day_of_week=0, teacher=self.teachers[1]),
            Availability(teacher_id=self.teachers[1].id, day_of_week=1, teacher=self.teachers[1]),
            Availability(teacher_id=self.teachers[1].id, day_of_week=2, teacher=self.teachers[1]),
            Availability(teacher_id=self.teachers[1].id, day_of_week=3, teacher=self.teachers[1]),
            Availability(teacher_id=self.teachers[2].id, day_of_week=0, teacher=self.teachers[2]),
            Availability(teacher_id=self.teachers[2].id, day_of_week=1, teacher=self.teachers[2]),
            Availability(teacher_id=self.teachers[2].id, day_of_week=2, teacher=self.teachers[2]),
            Availability(teacher_id=self.teachers[2].id, day_of_week=3, teacher=self.teachers[2]),
            Availability(teacher_id=self.teachers[2].id, day_of_week=4, teacher=self.teachers[2]),
            Availability(teacher_id=self.teachers[3].id, day_of_week=1, teacher=self.teachers[3]),
            Availability(teacher_id=self.teachers[3].id, day_of_week=3, teacher=self.teachers[3]),
            Availability(teacher_id=self.teachers[4].id, day_of_week=2, teacher=self.teachers[4]),
            Availability(teacher_id=self.teachers[4].id, day_of_week=3, teacher=self.teachers[4]),
            Availability(teacher_id=self.teachers[4].id, day_of_week=4, teacher=self.teachers[4]),
            Availability(teacher_id=self.teachers[5].id, day_of_week=0, teacher=self.teachers[5]),
            Availability(teacher_id=self.teachers[5].id, day_of_week=1, teacher=self.teachers[5]),
            Availability(teacher_id=self.teachers[5].id, day_of_week=2, teacher=self.teachers[5]),
            Availability(teacher_id=self.teachers[5].id, day_of_week=3, teacher=self.teachers[5]),
            Availability(teacher_id=self.teachers[5].id, day_of_week=4, teacher=self.teachers[5]),
            Availability(teacher_id=self.teachers[6].id, day_of_week=0, teacher=self.teachers[6]),
            Availability(teacher_id=self.teachers[6].id, day_of_week=1, teacher=self.teachers[6]),
            Availability(teacher_id=self.teachers[6].id, day_of_week=2, teacher=self.teachers[6]),
            Availability(teacher_id=self.teachers[6].id, day_of_week=4, teacher=self.teachers[6]),
            Availability(teacher_id=self.teachers[7].id, day_of_week=0, teacher=self.teachers[7]),
            Availability(teacher_id=self.teachers[7].id, day_of_week=1, teacher=self.teachers[7]),
            Availability(teacher_id=self.teachers[7].id, day_of_week=2, teacher=self.teachers[7]),
            Availability(teacher_id=self.teachers[7].id, day_of_week=3, teacher=self.teachers[7]),
            Availability(teacher_id=self.teachers[7].id, day_of_week=4, teacher=self.teachers[7]),
            Availability(teacher_id=self.teachers[8].id, day_of_week=0, teacher=self.teachers[8]),
            Availability(teacher_id=self.teachers[8].id, day_of_week=1, teacher=self.teachers[8]),
            Availability(teacher_id=self.teachers[8].id, day_of_week=2, teacher=self.teachers[8]),
            Availability(teacher_id=self.teachers[8].id, day_of_week=3, teacher=self.teachers[8]),
            Availability(teacher_id=self.teachers[8].id, day_of_week=4, teacher=self.teachers[8]),
            Availability(teacher_id=self.teachers[9].id, day_of_week=0, teacher=self.teachers[9]),
            Availability(teacher_id=self.teachers[9].id, day_of_week=1, teacher=self.teachers[9]),
            Availability(teacher_id=self.teachers[9].id, day_of_week=2, teacher=self.teachers[9]),
            Availability(teacher_id=self.teachers[9].id, day_of_week=3, teacher=self.teachers[9]),
            Availability(teacher_id=self.teachers[10].id, day_of_week=0, teacher=self.teachers[10]),
            Availability(teacher_id=self.teachers[10].id, day_of_week=1, teacher=self.teachers[10]),
            Availability(teacher_id=self.teachers[10].id, day_of_week=2, teacher=self.teachers[10]),
            Availability(teacher_id=self.teachers[11].id, day_of_week=3, teacher=self.teachers[11]),
            Availability(teacher_id=self.teachers[11].id, day_of_week=4, teacher=self.teachers[11]),
        ]

        self.session.bulk_save_objects(availabilities)
        self.session.commit()

    def populate_database_20122(self):
        subjects = [
            Subject(name="ALGORITMOS E LÓGICA DE PROGRAMAÇÃO", code="ALG", period=1, lessons_per_week=3, shift='M'),
            Subject(name="LÓGICA", code="LOG", period=1, lessons_per_week=2, shift='M'),

            Subject(name="CÁLCULO DIFERENCIAL E INTEGRAL", code="CAL", period=2, lessons_per_week=2, shift='T'),
            Subject(name="LEITURA E PRODUÇÃO DE TEXTO", code="LPT", period=2, lessons_per_week=2, shift='T'),
            Subject(name="PROGRAMAÇÃO", code="PROG", period=2, lessons_per_week=3, shift='T'),
            Subject(name="METODOLOGIA DO TRABALHO CIENTÍFICO", code="MTC", period=2, lessons_per_week=2, shift='T'),
            Subject(name="TEORIA GERAL DE SISTEMAS", code="TGS", period=2, lessons_per_week=2, shift='T'),

            Subject(name="PROBABILIDADE E ESTATÍSTICA", code="PE", period=4, lessons_per_week=2, shift='T'),
            Subject(name="PROGRAMAÇÃO ORIENTADA A OBJETOS II", code="POO2", period=4, lessons_per_week=2, shift='T'),
            Subject(name="ENGENHARIA DE SOFTWARE I", code="ES1", period=4, lessons_per_week=2, shift='T'),
            Subject(name="BANCO DE DADOS", code="BD", period=4, lessons_per_week=2, shift='T'),
            Subject(name="ARQUITETURA DE COMPUTADORES", code="ARQ", period=4, lessons_per_week=2, shift='T'),
            Subject(name="ARQUITETURA DE COMPUTADORES", code="ARQ", period=3, lessons_per_week=2, shift='M'),
            Subject(name="INGLÊS TÉCNICO", code="ING", period=4, lessons_per_week=2, shift='T'),

            Subject(name="CONTABILIDADE E CUSTOS", code="CEC", period=6, lessons_per_week=2, shift='T'),
            Subject(name="REDES DE COMPUTADORES", code="RED", period=6, lessons_per_week=2, shift='T'),
            Subject(name="GESTÃO DE PROJETOS DE SOFTWARE", code="GPS", period=6, lessons_per_week=2, shift='T'),
            Subject(name="FILOSOFIA I", code="FIL", period=6, lessons_per_week=2, shift='T'),
            Subject(name="TÓPICOS ESPECIAIS EM SEGURANÇA DA INFORMAÇÃO", code="TESI", period=6, lessons_per_week=2, shift='T'),
            Subject(name="TÓPICOS EM SISTEMAS DE INFORMAÇÃO (TÉCNICA DE ALGORITMOS)", code="TSI", period=6, lessons_per_week=2, shift='T'),

            Subject(name="SISTEMAS DE APOIO A DECISÃO", code="SAD", period=8, lessons_per_week=2, shift='T'),
            Subject(name="PROGRAMAÇÃO VISUAL", code="PV", period=8, lessons_per_week=2, shift='T'),
            Subject(name="DIREITO E LEGISLAÇÃO SOCIAL", code="DIR", period=8, lessons_per_week=2, shift='T'),
            Subject(name="ÉTICA", code="ETIC", period=8, lessons_per_week=2, shift='T'),
            Subject(name="ALGORITMOS EXPERIMENTAIS", code="AEX", period=8, lessons_per_week=2, shift='T'),
            Subject(name="TÓPICOS ESPECIAIS EM ENGENHARIA DE SOFTWARE (AMBIENTE E PRÁTICA DE PROGRAMAÇÃO)", code="TEES", period=7, lessons_per_week=2, shift='M'),
        ]

        self.session.bulk_save_objects(subjects, True)

        lessons = [
            Lesson(subject_id=subjects[0].id, teacher_id=self.teachers[12].id, semester="2012.2", teacher=self.teachers[12], subject=subjects[0]),
            Lesson(subject_id=subjects[1].id, teacher_id=self.teachers[2].id, semester="2012.2", teacher=self.teachers[2], subject=subjects[1]),
            Lesson(subject_id=subjects[2].id, teacher_id=self.teachers[13].id, semester="2012.2", teacher=self.teachers[13], subject=subjects[2]),
            Lesson(subject_id=subjects[3].id, teacher_id=self.teachers[14].id, semester="2012.2", teacher=self.teachers[14], subject=subjects[3]),
            Lesson(subject_id=subjects[4].id, teacher_id=self.teachers[1].id, semester="2012.2", teacher=self.teachers[1], subject=subjects[4]),
            Lesson(subject_id=subjects[5].id, teacher_id=self.teachers[4].id, semester="2012.2", teacher=self.teachers[4], subject=subjects[5]),
            Lesson(subject_id=subjects[6].id, teacher_id=self.teachers[4].id, semester="2012.2", teacher=self.teachers[4], subject=subjects[6]),
            Lesson(subject_id=subjects[7].id, teacher_id=self.teachers[0].id, semester="2012.2", teacher=self.teachers[0], subject=subjects[7]),
            Lesson(subject_id=subjects[8].id, teacher_id=self.teachers[6].id, semester="2012.2", teacher=self.teachers[6], subject=subjects[8]),
            Lesson(subject_id=subjects[9].id, teacher_id=self.teachers[6].id, semester="2012.2", teacher=self.teachers[6], subject=subjects[9]),
            Lesson(subject_id=subjects[10].id, teacher_id=self.teachers[8].id, semester="2012.2", teacher=self.teachers[8], subject=subjects[10]),
            Lesson(subject_id=subjects[11].id, teacher_id=self.teachers[3].id, semester="2012.2", teacher=self.teachers[3], subject=subjects[11]),
            Lesson(subject_id=subjects[12].id, teacher_id=self.teachers[3].id, semester="2012.2", teacher=self.teachers[3], subject=subjects[12]),
            Lesson(subject_id=subjects[13].id, teacher_id=self.teachers[15].id, semester="2012.2", teacher=self.teachers[15], subject=subjects[13]),
            Lesson(subject_id=subjects[14].id, teacher_id=self.teachers[16].id, semester="2012.2", teacher=self.teachers[16], subject=subjects[14]),
            Lesson(subject_id=subjects[15].id, teacher_id=self.teachers[9].id, semester="2012.2", teacher=self.teachers[9], subject=subjects[15]),
            Lesson(subject_id=subjects[16].id, teacher_id=self.teachers[5].id, semester="2012.2", teacher=self.teachers[5], subject=subjects[16]),
            Lesson(subject_id=subjects[17].id, teacher_id=self.teachers[17].id, semester="2012.2", teacher=self.teachers[17], subject=subjects[17]),
            Lesson(subject_id=subjects[18].id, teacher_id=self.teachers[9].id, semester="2012.2", teacher=self.teachers[9], subject=subjects[18]),
            Lesson(subject_id=subjects[19].id, teacher_id=self.teachers[12].id, semester="2012.2", teacher=self.teachers[12], subject=subjects[19]),

            Lesson(subject_id=subjects[20].id, teacher_id=self.teachers[1].id, semester="2012.2", teacher=self.teachers[1], subject=subjects[20]),
            Lesson(subject_id=subjects[21].id, teacher_id=self.teachers[20].id, semester="2012.2", teacher=self.teachers[20], subject=subjects[21]),
            Lesson(subject_id=subjects[22].id, teacher_id=self.teachers[18].id, semester="2012.2", teacher=self.teachers[18], subject=subjects[22]),
            Lesson(subject_id=subjects[23].id, teacher_id=self.teachers[19].id, semester="2012.2", teacher=self.teachers[19], subject=subjects[23]),
            Lesson(subject_id=subjects[24].id, teacher_id=self.teachers[2].id, semester="2012.2", teacher=self.teachers[2], subject=subjects[24]),
            Lesson(subject_id=subjects[25].id, teacher_id=self.teachers[8].id, semester="2012.2", teacher=self.teachers[8], subject=subjects[25]),
        ]

        self.session.bulk_save_objects(lessons, True)

        self.session.commit()

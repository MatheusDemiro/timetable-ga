import random

from models.availability import Availability
from models.subject import Subject
from models.lesson import Lesson


class UnifiedDatabase:
    def __init__(self, teachers, session):
        self.session = session
        self.teachers = teachers
        self.availabilities = {}

    def get_lessons(self):
        lessons = self.session.query(Lesson).all()

        self.session.close()

        return lessons

    def get_availabilities(self):
        teachers = []
        lessons = self.get_lessons()

        for lesson in lessons:
            if lesson.teacher.name not in self.availabilities:
                self.availabilities[lesson.teacher.name] = {"days": [], "total_lessons": 1,
                                                            "total_lessons_per_week": lesson.subject.lessons_per_week}
                teachers.append(lesson.teacher)
            else:
                self.availabilities[lesson.teacher.name]["total_lessons"] += 1
                self.availabilities[lesson.teacher.name]["total_lessons_per_week"] += lesson.subject.lessons_per_week

        for teacher in teachers:
            for i in range(3):
                day = self.sort_day(teacher)
                self.availabilities[teacher.name]["days"].append(day)

        print(self.count_lessons_per_day())

    def count_lessons_per_day(self):
        count = {}
        for key in self.availabilities.keys():
            for day in self.availabilities[key]["days"]:
                day_of_week = self.get_day_of_week(day)
                if day_of_week not in count:
                    count[day_of_week] = 1
                else:
                    count[day_of_week] += 1
        return count

    @staticmethod
    def get_day_of_week(day):
        if day == 0:
            return "SEG"
        if day == 1:
            return "TER"
        if day == 2:
            return "QUA"
        if day == 3:
            return "QUI"
        if day == 4:
            return "SEX"

    def sort_day(self, teacher):
        days_of_week = range(0, 5)
        day = random.choice(days_of_week)
        while day in self.availabilities[teacher.name]["days"]:
            day = random.choice(days_of_week)
        return day

    def period1(self):
        subjects_period1 = [
            Subject(name="ALGORITMOS E LÓGICA DE PROGRAMAÇÃO", code="ALG", period=1, lessons_per_week=3, shift='T'),
            Subject(name="INTRODUÇÃO A INFORMÁTICA", code="II", period=1, lessons_per_week=2, shift='T'),
            Subject(name="FUNDAMENTOS DE MATEMÁTICA", code="FMAT", period=1, lessons_per_week=2, shift='T'),
            Subject(name="LÓGICA", code="LOG", period=1, lessons_per_week=2, shift='T'),
            Subject(name="TEORIA GERAL DA ADMINISTRAÇÃO", code="TGA", period=1, lessons_per_week=2, shift='T'),
        ]

        self.session.bulk_save_objects(subjects_period1, True)

        lessons_period1 = [
            Lesson(subject_id=subjects_period1[0].id, teacher_id=self.teachers[1].id, semester="2012.1",
                   teacher=self.teachers[1], subject=subjects_period1[0]),
            Lesson(subject_id=subjects_period1[1].id, teacher_id=self.teachers[3].id, semester="2012.1",
                   teacher=self.teachers[3], subject=subjects_period1[1]),
            Lesson(subject_id=subjects_period1[2].id, teacher_id=self.teachers[0].id, semester="2012.1",
                   teacher=self.teachers[0], subject=subjects_period1[2]),
            Lesson(subject_id=subjects_period1[3].id, teacher_id=self.teachers[2].id, semester="2012.1",
                   teacher=self.teachers[2], subject=subjects_period1[3]),
            Lesson(subject_id=subjects_period1[4].id, teacher_id=self.teachers[4].id, semester="2012.1",
                   teacher=self.teachers[4], subject=subjects_period1[4]),
        ]

        self.session.bulk_save_objects(lessons_period1, True)
        self.session.commit()

    def period2(self):
        subjects_period2 = [
            Subject(name="CÁLCULO DIFERENCIAL E INTEGRAL", code="CAL", period=2, lessons_per_week=2, shift='T'),
            Subject(name="LEITURA E PRODUÇÃO DE TEXTO", code="LPT", period=2, lessons_per_week=2, shift='T'),
            Subject(name="PROGRAMAÇÃO", code="PROG", period=2, lessons_per_week=3, shift='T'),
            Subject(name="METODOLOGIA DO TRABALHO CIENTÍFICO", code="MTC", period=2, lessons_per_week=2, shift='T'),
            Subject(name="TEORIA GERAL DE SISTEMAS", code="TGS", period=2, lessons_per_week=2, shift='T'),
        ]

        self.session.bulk_save_objects(subjects_period2, True)

        lessons_period2 = [
            Lesson(subject_id=subjects_period2[0].id, teacher_id=self.teachers[13].id, semester="2012.2",
                   teacher=self.teachers[13], subject=subjects_period2[0]),
            Lesson(subject_id=subjects_period2[1].id, teacher_id=self.teachers[14].id, semester="2012.2",
                   teacher=self.teachers[14], subject=subjects_period2[1]),
            Lesson(subject_id=subjects_period2[2].id, teacher_id=self.teachers[1].id, semester="2012.2",
                   teacher=self.teachers[1], subject=subjects_period2[2]),
            Lesson(subject_id=subjects_period2[3].id, teacher_id=self.teachers[4].id, semester="2012.2",
                   teacher=self.teachers[4], subject=subjects_period2[3]),
            Lesson(subject_id=subjects_period2[4].id, teacher_id=self.teachers[4].id, semester="2012.2",
                   teacher=self.teachers[4], subject=subjects_period2[4]),
        ]

        self.session.bulk_save_objects(lessons_period2, True)
        self.session.commit()

    def period3(self):
        subjects_period3 = [
            Subject(name="ESTRUTURA DE DADOS", code="ED", period=3, lessons_per_week=3, shift='T'),
            Subject(name="FUNDAMENTOS DE SISTEMAS DE INFORMAÇÃO", code="FSI", period=3, lessons_per_week=2, shift='T'),
            Subject(name="ORGANIZAÇÃO SISTEMAS E MÉTODOS", code="OSM", period=3, lessons_per_week=2, shift='T'),
            Subject(name="PROGRAMAÇÃO ORIENTADA A OBJETOS I", code="POOI", period=3, lessons_per_week=2, shift='T'),
            Subject(name="ÁLGEBRA LINEAR", code="AL", period=3, lessons_per_week=2, shift='T'),
        ]

        self.session.bulk_save_objects(subjects_period3, True)

        lessons_period3 = [
            Lesson(subject_id=subjects_period3[0].id, teacher_id=self.teachers[2].id, semester="2012.1",
                   teacher=self.teachers[2], subject=subjects_period3[0]),
            Lesson(subject_id=subjects_period3[1].id, teacher_id=self.teachers[4].id, semester="2012.1",
                   teacher=self.teachers[4], subject=subjects_period3[1]),
            Lesson(subject_id=subjects_period3[2].id, teacher_id=self.teachers[5].id, semester="2012.1",
                   teacher=self.teachers[5], subject=subjects_period3[2]),
            Lesson(subject_id=subjects_period3[3].id, teacher_id=self.teachers[6].id, semester="2012.1",
                   teacher=self.teachers[6], subject=subjects_period3[3]),
            Lesson(subject_id=subjects_period3[4].id, teacher_id=self.teachers[7].id, semester="2012.1",
                   teacher=self.teachers[7], subject=subjects_period3[4]),
        ]

        self.session.bulk_save_objects(lessons_period3, True)
        self.session.commit()

    def period4(self):
        subjects_period4 = [
            Subject(name="PROBABILIDADE E ESTATÍSTICA", code="PE", period=4, lessons_per_week=2, shift='T'),
            Subject(name="PROGRAMAÇÃO ORIENTADA A OBJETOS II", code="POO2", period=4, lessons_per_week=2, shift='T'),
            Subject(name="ENGENHARIA DE SOFTWARE I", code="ES1", period=4, lessons_per_week=2, shift='T'),
            Subject(name="BANCO DE DADOS", code="BD", period=4, lessons_per_week=2, shift='T'),
            Subject(name="ARQUITETURA DE COMPUTADORES", code="ARQ", period=4, lessons_per_week=2, shift='T'),
            Subject(name="INGLÊS TÉCNICO", code="ING", period=4, lessons_per_week=2, shift='T'),
        ]

        self.session.bulk_save_objects(subjects_period4, True)

        lessons_period4 = [
            Lesson(subject_id=subjects_period4[0].id, teacher_id=self.teachers[0].id, semester="2012.2",
                   teacher=self.teachers[0], subject=subjects_period4[0]),
            Lesson(subject_id=subjects_period4[1].id, teacher_id=self.teachers[6].id, semester="2012.2",
                   teacher=self.teachers[6], subject=subjects_period4[1]),
            Lesson(subject_id=subjects_period4[2].id, teacher_id=self.teachers[6].id, semester="2012.2",
                   teacher=self.teachers[6], subject=subjects_period4[2]),
            Lesson(subject_id=subjects_period4[3].id, teacher_id=self.teachers[8].id, semester="2012.2",
                   teacher=self.teachers[8], subject=subjects_period4[3]),
            Lesson(subject_id=subjects_period4[4].id, teacher_id=self.teachers[3].id, semester="2012.2",
                   teacher=self.teachers[3], subject=subjects_period4[4]),
            Lesson(subject_id=subjects_period4[5].id, teacher_id=self.teachers[15].id, semester="2012.2",
                   teacher=self.teachers[15], subject=subjects_period4[5]),
        ]

        self.session.bulk_save_objects(lessons_period4, True)
        self.session.commit()

    def period5(self):
        subjects_period5 = [
            Subject(name="EMPREENDEDORISMO EM INFORMÁTICA", code="EMP", period=5, lessons_per_week=2, shift='T'),
            Subject(name="ENGENHARIA DE SOFTWARE II", code="ES2", period=5, lessons_per_week=2, shift='T'),
            Subject(name="PROGRAMAÇÃO WEB", code="PWEB", period=5, lessons_per_week=2, shift='T'),
            Subject(name="PROJETO E ADMIN. DE BANCO DE DADOS", code="PABD", period=5, lessons_per_week=2, shift='T'),
            Subject(name="SISTEMAS OPERACIONAIS", code="SO", period=5, lessons_per_week=2, shift='T'),
        ]

        self.session.bulk_save_objects(subjects_period5, True)

        lessons_period5 = [
            Lesson(subject_id=subjects_period5[0].id, teacher_id=self.teachers[4].id, semester="2012.1",
                   teacher=self.teachers[4], subject=subjects_period5[0]),
            Lesson(subject_id=subjects_period5[1].id, teacher_id=self.teachers[8].id, semester="2012.1",
                   teacher=self.teachers[8], subject=subjects_period5[1]),
            Lesson(subject_id=subjects_period5[2].id, teacher_id=self.teachers[6].id, semester="2012.1",
                   teacher=self.teachers[6], subject=subjects_period5[2]),
            Lesson(subject_id=subjects_period5[3].id, teacher_id=self.teachers[8].id, semester="2012.1",
                   teacher=self.teachers[8], subject=subjects_period5[3]),
            Lesson(subject_id=subjects_period5[4].id, teacher_id=self.teachers[9].id, semester="2012.1",
                   teacher=self.teachers[9], subject=subjects_period5[4]),
        ]

        self.session.bulk_save_objects(lessons_period5, True)
        self.session.commit()

    def period6(self):
        subjects_period6 = [
            Subject(name="CONTABILIDADE E CUSTOS", code="CEC", period=6, lessons_per_week=2, shift='T'),
            Subject(name="REDES DE COMPUTADORES", code="RED", period=6, lessons_per_week=2, shift='T'),
            Subject(name="GESTÃO DE PROJETOS DE SOFTWARE", code="GPS", period=6, lessons_per_week=2, shift='T'),
            Subject(name="FILOSOFIA I", code="FIL", period=6, lessons_per_week=2, shift='T'),
            Subject(name="TÓPICOS ESPECIAIS EM SEGURANÇA DA INFORMAÇÃO", code="SEG", period=6, lessons_per_week=2, shift='T'),
            Subject(name="TÓPICOS EM SISTEMAS DE INFORMAÇÃO (TÉCNICA DE ALGORITMOS)", code="TSI", period=6, lessons_per_week=2, shift='T'),
        ]

        self.session.bulk_save_objects(subjects_period6, True)

        lessons_period6 = [
            Lesson(subject_id=subjects_period6[0].id, teacher_id=self.teachers[16].id, semester="2012.2",
                   teacher=self.teachers[16], subject=subjects_period6[0]),
            Lesson(subject_id=subjects_period6[1].id, teacher_id=self.teachers[9].id, semester="2012.2",
                   teacher=self.teachers[9], subject=subjects_period6[1]),
            Lesson(subject_id=subjects_period6[2].id, teacher_id=self.teachers[5].id, semester="2012.2",
                   teacher=self.teachers[5], subject=subjects_period6[2]),
            Lesson(subject_id=subjects_period6[3].id, teacher_id=self.teachers[17].id, semester="2012.2",
                   teacher=self.teachers[17], subject=subjects_period6[3]),
            Lesson(subject_id=subjects_period6[4].id, teacher_id=self.teachers[9].id, semester="2012.2",
                   teacher=self.teachers[9], subject=subjects_period6[4]),
            Lesson(subject_id=subjects_period6[5].id, teacher_id=self.teachers[12].id, semester="2012.2",
                   teacher=self.teachers[12], subject=subjects_period6[5]),
        ]

        self.session.bulk_save_objects(lessons_period6, True)
        self.session.commit()

    def period7(self):
        # PDM(opt), SDIS(opt), MIC(opt), MATF, TEES, PV 2013.1
        # DIR(2013.1), MATF, PV 2014.1
        subjects_period7 = [
            Subject(name="DIREITO E LEGISLAÇÃO SOCIAL", code="DIR", period=7, lessons_per_week=2, shift='T'),
            Subject(name="MATEMÁTICA FINANCEIRA", code="MATF", period=7, lessons_per_week=2, shift='T'),
            Subject(name="PROGRAMAÇÃO VISUAL", code="PV", period=7, lessons_per_week=2, shift='T'),
        ]

        self.session.bulk_save_objects(subjects_period7, True)

        lessons_period7 = [
            Lesson(subject_id=subjects_period7[0].id, teacher_id=self.teachers[18].id, semester="2012.1",
                   teacher=self.teachers[18], subject=subjects_period7[0]),
            Lesson(subject_id=subjects_period7[1].id, teacher_id=self.teachers[0].id, semester="2012.1",
                   teacher=self.teachers[0], subject=subjects_period7[1]),
            Lesson(subject_id=subjects_period7[2].id, teacher_id=self.teachers[21].id, semester="2015.1",
                   teacher=self.teachers[21], subject=subjects_period7[2]),
        ]

        self.session.bulk_save_objects(lessons_period7, True)
        self.session.commit()

    def period8(self):
        # SAD, DIR, AEX, ETIC 2012.2
        subjects_period8 = [
            Subject(name="SISTEMAS DE APOIO A DECISÃO", code="SAD", period=8, lessons_per_week=2, shift='T'),
            # Subject(name="DIREITO E LEGISLAÇÃO SOCIAL", code="DIR", period=8, lessons_per_week=2, shift='T'),
            Subject(name="ÉTICA", code="ETIC", period=8, lessons_per_week=2, shift='T'),
            Subject(name="ALGORITMOS EXPERIMENTAIS", code="AEX", period=8, lessons_per_week=2, shift='T'),   # optativa
        ]

        self.session.bulk_save_objects(subjects_period8, True)

        lessons_period8 = [
            Lesson(subject_id=subjects_period8[0].id, teacher_id=self.teachers[1].id, semester="2012.2",
                   teacher=self.teachers[1], subject=subjects_period8[0]),
            # Lesson(subject_id=subjects_period8[1].id, teacher_id=self.teachers[18].id, semester="2012.2",
            #        teacher=self.teachers[18], subject=subjects_period8[1]),
            Lesson(subject_id=subjects_period8[1].id, teacher_id=self.teachers[19].id, semester="2012.2",
                   teacher=self.teachers[19], subject=subjects_period8[1]),
            Lesson(subject_id=subjects_period8[2].id, teacher_id=self.teachers[2].id, semester="2012.2",
                   teacher=self.teachers[2], subject=subjects_period8[2]),
        ]

        self.session.bulk_save_objects(lessons_period8, True)
        self.session.commit()

    def save_availabilities(self):
        availabilities = [
            Availability(teacher_id=self.teachers[4].id, day_of_week=0, teacher=self.teachers[4]),
            Availability(teacher_id=self.teachers[4].id, day_of_week=1, teacher=self.teachers[4]),
            Availability(teacher_id=self.teachers[4].id, day_of_week=2, teacher=self.teachers[4]),
            Availability(teacher_id=self.teachers[4].id, day_of_week=3, teacher=self.teachers[4]),
            Availability(teacher_id=self.teachers[4].id, day_of_week=4, teacher=self.teachers[4]),

            Availability(teacher_id=self.teachers[6].id, day_of_week=1, teacher=self.teachers[6]),
            Availability(teacher_id=self.teachers[6].id, day_of_week=2, teacher=self.teachers[6]),
            Availability(teacher_id=self.teachers[6].id, day_of_week=3, teacher=self.teachers[6]),

            Availability(teacher_id=self.teachers[1].id, day_of_week=0, teacher=self.teachers[1]),
            Availability(teacher_id=self.teachers[1].id, day_of_week=1, teacher=self.teachers[1]),
            Availability(teacher_id=self.teachers[1].id, day_of_week=2, teacher=self.teachers[1]),
            Availability(teacher_id=self.teachers[1].id, day_of_week=3, teacher=self.teachers[1]),
            Availability(teacher_id=self.teachers[1].id, day_of_week=4, teacher=self.teachers[1]),

            Availability(teacher_id=self.teachers[2].id, day_of_week=1, teacher=self.teachers[2]),
            Availability(teacher_id=self.teachers[2].id, day_of_week=2, teacher=self.teachers[2]),
            Availability(teacher_id=self.teachers[2].id, day_of_week=4, teacher=self.teachers[2]),

            Availability(teacher_id=self.teachers[3].id, day_of_week=0, teacher=self.teachers[3]),
            Availability(teacher_id=self.teachers[3].id, day_of_week=2, teacher=self.teachers[3]),
            Availability(teacher_id=self.teachers[3].id, day_of_week=4, teacher=self.teachers[3]),

            Availability(teacher_id=self.teachers[16].id, day_of_week=2, teacher=self.teachers[16]),
            Availability(teacher_id=self.teachers[16].id, day_of_week=3, teacher=self.teachers[16]),

            Availability(teacher_id=self.teachers[8].id, day_of_week=0, teacher=self.teachers[8]),
            Availability(teacher_id=self.teachers[8].id, day_of_week=2, teacher=self.teachers[8]),
            Availability(teacher_id=self.teachers[8].id, day_of_week=3, teacher=self.teachers[8]),
            Availability(teacher_id=self.teachers[8].id, day_of_week=4, teacher=self.teachers[8]),

            Availability(teacher_id=self.teachers[0].id, day_of_week=1, teacher=self.teachers[0]),
            Availability(teacher_id=self.teachers[0].id, day_of_week=3, teacher=self.teachers[0]),
            Availability(teacher_id=self.teachers[0].id, day_of_week=4, teacher=self.teachers[0]),

            Availability(teacher_id=self.teachers[5].id, day_of_week=1, teacher=self.teachers[5]),
            Availability(teacher_id=self.teachers[5].id, day_of_week=3, teacher=self.teachers[5]),

            Availability(teacher_id=self.teachers[9].id, day_of_week=0, teacher=self.teachers[9]),
            Availability(teacher_id=self.teachers[9].id, day_of_week=1, teacher=self.teachers[9]),
            Availability(teacher_id=self.teachers[9].id, day_of_week=2, teacher=self.teachers[9]),

            Availability(teacher_id=self.teachers[12].id, day_of_week=1, teacher=self.teachers[12]),
            Availability(teacher_id=self.teachers[12].id, day_of_week=3, teacher=self.teachers[12]),

            Availability(teacher_id=self.teachers[13].id, day_of_week=2, teacher=self.teachers[13]),
            Availability(teacher_id=self.teachers[13].id, day_of_week=4, teacher=self.teachers[13]),

            Availability(teacher_id=self.teachers[7].id, day_of_week=0, teacher=self.teachers[7]),
            Availability(teacher_id=self.teachers[7].id, day_of_week=2, teacher=self.teachers[7]),

            Availability(teacher_id=self.teachers[14].id, day_of_week=0, teacher=self.teachers[14]),
            Availability(teacher_id=self.teachers[14].id, day_of_week=1, teacher=self.teachers[14]),

            Availability(teacher_id=self.teachers[19].id, day_of_week=0, teacher=self.teachers[19]),
            Availability(teacher_id=self.teachers[19].id, day_of_week=2, teacher=self.teachers[19]),

            Availability(teacher_id=self.teachers[21].id, day_of_week=0, teacher=self.teachers[21]),
            Availability(teacher_id=self.teachers[21].id, day_of_week=3, teacher=self.teachers[21]),

            Availability(teacher_id=self.teachers[17].id, day_of_week=0, teacher=self.teachers[17]),
            Availability(teacher_id=self.teachers[17].id, day_of_week=2, teacher=self.teachers[17]),

            Availability(teacher_id=self.teachers[15].id, day_of_week=0, teacher=self.teachers[15]),
            Availability(teacher_id=self.teachers[15].id, day_of_week=1, teacher=self.teachers[15]),

            Availability(teacher_id=self.teachers[18].id, day_of_week=1, teacher=self.teachers[18]),
            Availability(teacher_id=self.teachers[18].id, day_of_week=2, teacher=self.teachers[18]),
        ]

        # dic = {}
        # for i in availabilities:
        #     if i.teacher.name not in dic:
        #         dic[i.teacher.name] = {"DIAS": [self.get_day_of_week(i.day_of_week)]}
        #     else:
        #         dic[i.teacher.name]["DIAS"].append(self.get_day_of_week(i.day_of_week))
        #
        # for i in dic.keys():
        #     print("%s - %s" % (i, ",".join(dic[i]["DIAS"])))

        self.session.bulk_save_objects(availabilities)
        self.session.commit()

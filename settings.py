from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_URI = "mysql://root:password@localhost:3306/timetable?charset=utf8"
POPULATION_SIZE = 100
GENERATIONS_NUMBER = 2000
TOTAL_PERIODS = 8
PERIODS = [1, 2, 3, 4, 5, 6, 7, 8]
LESSONS_PER_DAY = 3
LESSON_HOUR = 2
WEEK_SIZE = 5
EXCLUSIVE_DEDICATION = False

Base = declarative_base()

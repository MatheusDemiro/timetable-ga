from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_URI = "mysql://root:password@localhost:3306/timetable?charset=utf8"
POPULATION_SIZE = 100
GENERATIONS_NUMBER = 10
TOTAL_PERIODS = 2
LESSONS_PER_DAY = 3
LESSON_HOUR = 2
WEEK_SIZE = 5

Base = declarative_base()

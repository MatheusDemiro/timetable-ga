from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_URI = "mysql://root@localhost:3306/timetable?charset=utf8"
POPULATION_SIZE = 20
GENERATIONS_NUMBER = 1
TOTAL_PERIODS = 2
LESSONS_PER_DAY = 3
WEEK_SIZE = 5

Base = declarative_base()

from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_URI = "mysql://root@localhost:3306/timetable?charset=utf8"
POPULATION_SIZE = 100
GENERATIONS_NUMBER = 2000
PERIOD_QUANTITY = 2
LESSONS_PER_DAY = 3
WEEK_SIZE = 5

Base = declarative_base()

# coding: utf-8
from sqlalchemy import Column, DECIMAL, Float, Integer, NCHAR, String, Table
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
Base = declarative_base()
metadata = Base.metadata


class DictClas(Base):
    __tablename__ = 'Dict_Class'

    Code = Column(String(50, 'Chinese_PRC_CI_AS'))
    Class = Column(String(100, 'Chinese_PRC_CI_AS'))
    id = Column(Integer, primary_key=True)
    Subsys = Column(String(50, 'Chinese_PRC_CI_AS'))


class ExpertJudge(Base):
    __tablename__ = 'Expert_Judge'

    ID = Column(Integer, primary_key=True)
    Class = Column(String(100, 'Chinese_PRC_CI_AS'))
    Year = Column(String(50, 'Chinese_PRC_CI_AS'))
    Expert = Column(String(50, 'Chinese_PRC_CI_AS'))
    Stage = Column(Integer)


class ExpertList(Base):
    __tablename__ = 'Expert_List'

    Id = Column(Integer, primary_key=True)
    Expert_Name = Column(String(100, 'Chinese_PRC_CI_AS'))
    Birth_Year = Column(String(50, 'Chinese_PRC_CI_AS'))
    Sex = Column(String(50, 'Chinese_PRC_CI_AS'))
    People = Column(String(50, 'Chinese_PRC_CI_AS'))
    Institution = Column(String(50, 'Chinese_PRC_CI_AS'))
    Professional_Title = Column(String(50, 'Chinese_PRC_CI_AS'))
    Administrative_duty = Column(String(500, 'Chinese_PRC_CI_AS'))
    City = Column(String(50, 'Chinese_PRC_CI_AS'))
    Province = Column(String(50, 'Chinese_PRC_CI_AS'))
    Address = Column(String(50, 'Chinese_PRC_CI_AS'))
    Zip = Column(String(50, 'Chinese_PRC_CI_AS'))
    Highestdegree = Column(String(50, 'Chinese_PRC_CI_AS'))
    Degreedate = Column(String(50, 'Chinese_PRC_CI_AS'))
    University = Column(String(50, 'Chinese_PRC_CI_AS'))
    Country = Column(String(50, 'Chinese_PRC_CI_AS'))
    Honorary_Reward = Column(String(500, 'Chinese_PRC_CI_AS'))
    Tel = Column(String(50, 'Chinese_PRC_CI_AS'))
    Email = Column(String(50, 'Chinese_PRC_CI_AS'))
    Class = Column(String(500, 'Chinese_PRC_CI_AS'))


t_Paper_Country_HotDegree = Table(
    'Paper_Country_HotDegree', metadata,
    Column('class', String(100, 'Chinese_PRC_CI_AS')),
    Column('year', String(50, 'Chinese_PRC_CI_AS')),
    Column('country', String(50, 'Chinese_PRC_CI_AS')),
    Column('Hot_degree', DECIMAL(18, 3))
)


t_Paper_Country_Influence = Table(
    'Paper_Country_Influence', metadata,
    Column('class', String(100, 'Chinese_PRC_CI_AS')),
    Column('year', String(50, 'Chinese_PRC_CI_AS')),
    Column('Influence', Float(53)),
    Column('country', String(50, 'Chinese_PRC_CI_AS'))
)


t_Paper_HotDegree = Table(
    'Paper_HotDegree', metadata,
    Column('class', String(100, 'Chinese_PRC_CI_AS')),
    Column('year', String(50, 'Chinese_PRC_CI_AS')),
    Column('Paper_Num_total', Integer),
    Column('Hot_degree', DECIMAL(18, 3))
)


t_Paper_Influence = Table(
    'Paper_Influence', metadata,
    Column('class', String(100, 'Chinese_PRC_CI_AS')),
    Column('year', String(50, 'Chinese_PRC_CI_AS')),
    Column('Influence', Float(53)),
    Column('subsys', NCHAR(10))
)


t_Patent_Country_HotDegree = Table(
    'Patent_Country_HotDegree', metadata,
    Column('class', String(100, 'Chinese_PRC_CI_AS')),
    Column('year', String(50, 'Chinese_PRC_CI_AS')),
    Column('country', String(50, 'Chinese_PRC_CI_AS')),
    Column('Hot_degree', DECIMAL(18, 3))
)


t_Patent_Country_Influence = Table(
    'Patent_Country_Influence', metadata,
    Column('class', String(100, 'Chinese_PRC_CI_AS')),
    Column('year', String(50, 'Chinese_PRC_CI_AS')),
    Column('Patent_fc_class_country', Float(53)),
    Column('country', String(50, 'Chinese_PRC_CI_AS'))
)


t_Patent_HotDegree = Table(
    'Patent_HotDegree', metadata,
    Column('class', String(100, 'Chinese_PRC_CI_AS')),
    Column('year', String(50, 'Chinese_PRC_CI_AS')),
    Column('Hot_degree', DECIMAL(18, 3))
)


t_Patent_Influence = Table(
    'Patent_Influence', metadata,
    Column('class', String(100, 'Chinese_PRC_CI_AS')),
    Column('year', String(50, 'Chinese_PRC_CI_AS')),
    Column('Influence', Float(53)),
    Column('subsys', NCHAR(10))
)


class User(UserMixin, Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    username = Column(String(50, 'Chinese_PRC_CI_AS'), unique=True)
    email = Column(String(50, 'Chinese_PRC_CI_AS'), unique=True)
    password = Column(String(50, 'Chinese_PRC_CI_AS'))
    def __init__(self,username, password, email):
        self.username = username
        self.password = password
        self.email = email
    def get_id(self):
        return unicode(self.id)

class Country(Base):
    __tablename__ = 'country'

    ID = Column(Integer, primary_key=True)
    Country = Column(String(50, 'Chinese_PRC_CI_AS'))

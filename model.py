# coding: utf-8
from sqlalchemy import Column, DECIMAL, Float, Integer, NCHAR, String
from sqlalchemy.ext.declarative import declarative_base

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


class PaperCountryHotDegree(Base):
    __tablename__ = 'Paper_Country_HotDegree'

    id = Column(Integer, primary_key=True)
    _class = Column('class', String(100, 'Chinese_PRC_CI_AS'))
    year = Column(String(50, 'Chinese_PRC_CI_AS'))
    country = Column(String(50, 'Chinese_PRC_CI_AS'))
    Hot_degree = Column(DECIMAL(18, 3))


class PaperCountryInfluence(Base):
    __tablename__ = 'Paper_Country_Influence'

    id = Column(Integer, primary_key=True)
    _class = Column('class', String(100, 'Chinese_PRC_CI_AS'))
    year = Column(String(50, 'Chinese_PRC_CI_AS'))
    Influence = Column(Float(53))
    country = Column(String(50, 'Chinese_PRC_CI_AS'))


class PaperHotDegree(Base):
    __tablename__ = 'Paper_HotDegree'

    id = Column(Integer, primary_key=True)
    _class = Column('class', String(100, 'Chinese_PRC_CI_AS'))
    year = Column(String(50, 'Chinese_PRC_CI_AS'))
    Paper_Num_total = Column(Integer)
    Hot_degree = Column(DECIMAL(18, 3))


class PaperInfluence(Base):
    __tablename__ = 'Paper_Influence'

    id = Column(Integer, primary_key=True)
    _class = Column('class', String(100, 'Chinese_PRC_CI_AS'))
    year = Column(String(50, 'Chinese_PRC_CI_AS'))
    Influence = Column(Float(53))
    subsys = Column(NCHAR(10))


class PatentCountryHotDegree(Base):
    __tablename__ = 'Patent_Country_HotDegree'

    id = Column(Integer, primary_key=True)
    _class = Column('class', String(100, 'Chinese_PRC_CI_AS'))
    year = Column(String(50, 'Chinese_PRC_CI_AS'))
    country = Column(String(50, 'Chinese_PRC_CI_AS'))
    Hot_degree = Column(DECIMAL(18, 3))


class PatentCountryInfluence(Base):
    __tablename__ = 'Patent_Country_Influence'

    id = Column(Integer, primary_key=True)
    _class = Column('class', String(100, 'Chinese_PRC_CI_AS'))
    year = Column(String(50, 'Chinese_PRC_CI_AS'))
    Patent_fc_class_country = Column(Float(53))
    country = Column(String(50, 'Chinese_PRC_CI_AS'))


class PatentHotDegree(Base):
    __tablename__ = 'Patent_HotDegree'

    id = Column(Integer, primary_key=True)
    _class = Column('class', String(100, 'Chinese_PRC_CI_AS'))
    year = Column(String(50, 'Chinese_PRC_CI_AS'))
    Hot_degree = Column(DECIMAL(18, 3))


class PatentInfluence(Base):
    __tablename__ = 'Patent_Influence'

    id = Column(Integer, primary_key=True)
    _class = Column('class', String(100, 'Chinese_PRC_CI_AS'))
    year = Column(String(50, 'Chinese_PRC_CI_AS'))
    Influence = Column(Float(53))
    subsys = Column(NCHAR(10))


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    username = Column(String(50, 'Chinese_PRC_CI_AS'), unique=True)
    email = Column(String(50, 'Chinese_PRC_CI_AS'), unique=True)
    password = Column(String(50, 'Chinese_PRC_CI_AS'))


class Country(Base):
    __tablename__ = 'country'

    ID = Column(Integer, primary_key=True)
    Country = Column(String(50, 'Chinese_PRC_CI_AS'))

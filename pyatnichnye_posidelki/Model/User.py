from sqlalchemy import Column, Integer, String, ForeignKey

from Model.Base import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String)
    password = Column(Integer)
    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)
    numOfMedicalCard = Column(Integer)
    dateGetMedicalCard = Column(String)
    genderId = Column(Integer, ForeignKey('gender.id'))


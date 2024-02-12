from sqlalchemy import Column, Integer, String
from Model.Base import *


class Gender(Base):
    __tablename__ = 'gender'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

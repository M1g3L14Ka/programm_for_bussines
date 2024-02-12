from sqlalchemy import Column, Integer, String

from Model.Base import *


class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

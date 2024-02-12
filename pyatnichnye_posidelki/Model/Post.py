from sqlalchemy import Column, Integer, String, ForeignKey
from Model.Base import *


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    roleId = Column(Integer, ForeignKey('role.id'))

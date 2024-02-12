from sqlalchemy import Column, Integer, ForeignKey, String
from Model.Base import *


class Personal(Base):
    __tablename__ = 'personal'

    id = Column(Integer, primary_key=True, index=True)
    postId = Column(Integer, ForeignKey('post.id'))
    name = Column(String)
    isWorking = Column(Integer)
    genderId = Column(Integer)

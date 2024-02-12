from sqlalchemy import Column, Integer, ForeignKey, String
from Model.Base import *


class IllHistory(Base):
    __tablename__ = 'illHistory'

    id = Column(Integer, primary_key=True, index=True)
    doctorId = Column(Integer, ForeignKey('personal.id'))
    patientId = Column(Integer, ForeignKey('user.id'))
    diagnosisId = Column(Integer, ForeignKey('diagnosis.id'))
    diagnostedDate = Column(String)
    idDone = Column(Integer)


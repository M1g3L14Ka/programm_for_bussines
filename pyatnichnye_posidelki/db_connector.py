from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model.Base import Base
from psycopg2 import *
from Model.Post import Post

postgresql_database = "postgresql://postgres:1@127.0.0.1:5433/postgres"

engine = create_engine(postgresql_database, echo=True)
Session = sessionmaker(autoflush=False, bind=engine)

with Session(autoflush=False, bind=engine) as db:
    terapevt = db.query(Post).first()
    print(terapevt.id, terapevt.roleId, terapevt.name)

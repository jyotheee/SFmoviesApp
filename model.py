from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref


engine = create_engine("sqlite:///movies.db", echo=False)
dbsession = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

Base = declarative_base()
Base.query = dbsession.query_property()

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key = True)
    title = Column(String(64), nullable = False)
    location = Column (String(64), nullable = True)

def createTable():
    Base.metadata.create_all(engine)

def connect():
    global dbsession
    return dbsession()

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()








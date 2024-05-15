# database.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

URL = 'postgresql://secUREusER:StrongEnoughPassword)@51.250.26.59:5432/query'

engine = create_engine(URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class GameDB(Base):
    __tablename__ = 'game_shop'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    release_year = Column(Integer, nullable=False)
    genre = Column(String, nullable=False)

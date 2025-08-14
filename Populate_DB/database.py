from sqlalchemy.engine import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String


postgres_URL = "postgresql://postgres:diwa123@localhost:5432/PopulateEx"
engine = create_engine(postgres_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Heros(Base):
    __tablename__ = "heros"
    id = Column(Integer, primary_key=True, index=True)
    hero_name = Column(String)
    real_name = Column(String)
    age = Column(Integer)
    universe = Column(String)

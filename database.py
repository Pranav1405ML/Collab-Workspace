from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///workspace.db")

Base = declarative_base()

class CodeSnippet(Base):
    __tablename__ = "snippets"
    id = Column(Integer, primary_key = True)
    code = Column(String)

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind = engine)
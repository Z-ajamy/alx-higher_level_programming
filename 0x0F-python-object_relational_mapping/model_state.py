from sqlalchemy import create_engine, Column, INTEGER, String
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column('id', INTEGER, primary_key=True, nullable=False)
    name = Column('name', String(128), nullable=False)

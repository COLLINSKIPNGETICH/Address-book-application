from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)

# Initialize the database engine
engine = create_engine('sqlite:///database.db')

# Create the tables in the database
Base.metadata.create_all(engine)

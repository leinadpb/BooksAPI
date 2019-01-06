from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
engine = create_engine('sqlite:///database.db', convert_unicode=True)

Base = declarative_base()
Base.metadata.bind = engine
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = scoped_session(Session)
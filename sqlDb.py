from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
Engine = create_engine('sqlite:///:memory:', echo = False)
""" engine = create_engine('sqlite:///:memory:', echo = False)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)    """

#More in future

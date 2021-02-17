# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class Link(Base):

    __tablename__ = "link"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    goto = Column(String, nullable=False)
    topic = Column(String)


engine = create_engine('sqlite:///url.db', echo=True)
Base.metadata.create_all(engine)

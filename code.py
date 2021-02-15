# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from os import listdir
import sys


def listFile(path='.', ext='url'):

    result = []
    for item in listdir(path):
        if item[-len(ext):] == ext:
            result.append(item)
    return result


def gatherLink(file_name, key='URL='):

    with open(file_name, 'r') as file:
        for line in file:
            if line[:len(key)] == key:
                return file.name, line[len(key):]


def genTxt(listing):

    with open('out.csv', 'w') as file:
        for item in listing:
            file.write(item[0])
            file.write('\t')
            file.write(item[1])
    return


def genDb(listing):

    Base = declarative_base()

    class Link(Base):

        __tablename__ = "link"

        id = Column(Integer, primary_key=True)
        name = Column(String)
        goto = Column(String, nullable=False)
        topic = Column(String)

    engine = create_engine('sqlite:///url.db', echo=True)
    Base.metadata.create_all(engine)

    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.configure(bind=engine)
    session = DBSession()
    for item in listing:
        newLink = Link(name=item[0], goto=item[1].rstrip())
        session.add(newLink)
        session.commit()
    return


def genHtml():

    engine = create_engine('sqlite:///url.db', echo=True)
    Base = declarative_base()
    Base.metadata.bind = engine

    class Link(Base):

        __tablename__ = "link"

        id = Column(Integer, primary_key=True)
        name = Column(String)
        goto = Column(String, nullable=False)
        topic = Column(String)

    DBSession = sessionmaker()
    DBSession.configure(bind=engine)
    session = DBSession()
    items = session.query(Link).all()
    with open('index.html', 'w') as file:
        link = '<ul>'
        for item in items:
            link += '<li><a href="'
            link += item.goto
            link += '">'
            link += item.name
            link += '</a></li>'
        link += '</ul>'
        file.write(link)
    return


def main():

    # if len(sys.argv) > 1:
    #     path = sys.argv[1]
    # else:
    #     path
    sources = listFile()
    listing = []
    for source in sources:
        listing.append(gatherLink(source))
    # genDb(listing)
    genHtml()


if __name__ == "__main__":
    main()

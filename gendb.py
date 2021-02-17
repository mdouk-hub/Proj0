# -*- coding: utf-8 -*-
from listfile import listFile
from gatherlink import gatherLink
from sqlalchemy import create_engine
from database import Base, Link
from sqlalchemy.orm import sessionmaker


def main():

    sources = listFile()
    listing = []
    for source in sources:
        listing.append((source, gatherLink(source)))
    engine = create_engine('sqlite:///url.db', echo=True)
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.configure(bind=engine)
    session = DBSession()
    for item in listing:
        newLink = Link(name=item[0], goto=item[1].rstrip())
        session.add(newLink)
        session.commit()
    print('Database successfully created.')


if __name__ == "__main__":
    main()

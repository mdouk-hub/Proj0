# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from database import Base, Link
from sqlalchemy.orm import sessionmaker


def main():

    engine = create_engine('sqlite:///url.db', echo=True)
    Base.metadata.bind = engine
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
    print('WebPage successfully created.')


if __name__ == "__main__":
    main()

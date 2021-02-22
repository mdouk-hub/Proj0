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
        out = '<ul>'
        for item in items:
            out += '<li><a href="'
            out += item.goto
            out += '">'
            out += item.name
            out += '</a></li>'
        out += '</ul>'
        file.write(out)
    print('WebPage successfully created.')


if __name__ == "__main__":
    main()

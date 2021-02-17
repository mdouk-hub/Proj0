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
        link = '<table><thead><tr>'
        link += '<th>Id</th>'
        link += '<th>Name</th>'
        link += '<th>Goto</th>'
        link += '<th>Topic</th>'
        link += '</tr></thead><tbody>'
        for item in items:
            link += '<tr><td>'
            link += str(item.id)
            link += '</td><td>'
            link += str(item.name)
            link += '</td><td>'
            link += str(item.goto)
            link += '</td><td>'
            link += str(item.topic)
            link += '</td></tr>'
        link += '</tbody></table>'
        file.write(link)
    print('WebPage successfully created.')


if __name__ == "__main__":
    main()

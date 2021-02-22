# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from database import Base, Link
from sqlalchemy.orm import sessionmaker


def main():

    out = '<!DOCTYPE html><html lang="en">'
    out += '<head>'
    out += '<meta charset="utf-8">'
    out += '<title>Links</title>'
    out += '<link href="style.css" rel="stylesheet" type="text/css">'
    out += '</head>'
    out += '<body><table><thead><tr>'
    out += '<th>Id</th>'
    out += '<th>Name</th>'
    out += '<th>Goto</th>'
    out += '<th>Topic</th>'
    out += '</tr></thead>'

    engine = create_engine('sqlite:///url.db', echo=True)
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.configure(bind=engine)
    session = DBSession()
    items = session.query(Link).all()

    out += '<tbody>'
    for item in items:
        out += '<tr><td>'
        out += str(item.id)
        out += '</td><td>'
        out += str(item.name)
        out += '</td><td>'
        out += str(item.goto)
        out += '</td><td>'
        out += str(item.topic)
        out += '</td></tr>'
    out += '</tbody></table></body></html>'
    
    with open('index.html', 'w') as file:
        file.write(out)
    print('WebPage successfully created.')


if __name__ == "__main__":
    main()

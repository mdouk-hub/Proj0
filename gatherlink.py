# -*- coding: utf-8 -*-
from listfile import listFile


def gatherLink(file_name, key='URL='):

    with open(file_name, 'r') as file:
        for line in file:
            if line[:len(key)] == key:
                return line[len(key):]


def main():

    sources = listFile()
    listing = []
    for source in sources:
        listing.append((source, gatherLink(source)))
    print('%s Link(s) Found:' % len(listing))
    for item in listing:
        print(item)


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
from gatherlink import gatherLink
from listfile import listFile


def main():

    sources = listFile()
    listing = []
    for source in sources:
        listing.append((source, gatherLink(source)))
    with open('url.csv', 'w') as file:
        for item in listing:
            file.write(item[0])
            file.write('\t')
            file.write(item[1])
    print('File generated successfully.')


if __name__ == "__main__":
    main()

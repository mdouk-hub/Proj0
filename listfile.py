# -*- coding: utf-8 -*-
from os import listdir


def listFile(path='.', ext='url'):

    result = []
    for item in listdir(path):
        if item[-len(ext):] == ext:
            result.append(item)
    return result


def main():

    sources = listFile()
    print('%s File(s) Found:' % len(sources))
    for source in sources:
        print(source)


if __name__ == "__main__":
    main()

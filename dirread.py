#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os

import jinja2


def error(msg):
    print(msg, file=sys.stderr)
    exit(1)


def getscriptpath():
    return os.path.dirname(os.path.realpath(__file__))


def collect_subpaths(dirpath):
    pathlist = []
    tree = os.walk(dirpath)
    for dir in tree:
        path = dir[0]
        files = dir[2]
        for file in files:
            pathlist.append(os.path.join(path, file))
    pathlist.sort()
    return pathlist


def main():
    if len(sys.argv) != 2:
        error('Give a dirctory name as only argument.')
    
    dirpath = sys.argv[1]
    if not os.path.exists(dirpath):
        error('Directory not found.')

    subpaths = collect_subpaths(dirpath)
    for path in subpaths:
        print(path)

    # templatepath = os.path.join(getscriptpath(), "template.html")
    # with open(templatepath, encoding="utf8") as f:
    #     content = f.read()

    # template = jinja2.Template(content)
    # rendered = template.render(
    #     path="Test path",
    #     message="Hello, world!"
    # )
    # print(rendered)


if __name__ == '__main__':
    main()

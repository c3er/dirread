#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Todo:
# - Better sorting of files (first the files in the highest level etc.)
# - Support for .gitignore
# - Syntax highlighting


import sys
import os
import string

import jinja2


class TextFile:
    def __init__(self, path, content):
        self.path = path
        self._content = content

    @property
    def content(self):
        if self.issupported():
            return "\n" + self._content
        return ""

    def issupported(self):
        return self._content is not None


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


# Source http://stackoverflow.com/a/1446870
def istext(filename):
    bytecount = 1000
    try:
        with open(filename, "r+b") as f:
            content = f.read(bytecount)
    except PermissionError:
        return False

    # Empty files are considered text
    if not content:
        return True

    # Files with null bytes are likely binary
    if 0 in content:
        return False

    # If more than 30% non-text characters, then this is considered a binary file
    nontextlimit = 300
    count = 0
    for byte in content:
        if chr(byte) not in string.printable:
            count += 1
    return count <= nontextlimit


def readcontent(path):
    if istext(path):
        with open(path, encoding="utf8") as f:
            return f.read()
    return None


def main():
    if len(sys.argv) != 2:
        error('Give a dirctory name as only argument.')
    
    dirpath = sys.argv[1]
    if not os.path.exists(dirpath):
        error('Directory not found.')

    subpaths = collect_subpaths(dirpath)
    contents = [readcontent(path) for path in subpaths]
    files = [TextFile(path, content) for path, content in zip(subpaths, contents)]

    templatepath = os.path.join(getscriptpath(), "template.html")
    with open(templatepath, encoding="utf8") as f:
        template_content = f.read()

    template = jinja2.Template(template_content)
    rendered = template.render(
        path=dirpath,
        files=files
    )

    with open("output.html", "w", encoding="utf8") as f:
        f.write(rendered)


if __name__ == '__main__':
    main()

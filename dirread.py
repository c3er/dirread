#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Todo:
# - Escape HTML characters
# - Syntax highlighting


import sys
import os
import string
import html
import webbrowser

import jinja2  # pip install Jinja2

import gitignore


OUTDIR = "output"
OUTFILE = "output.html"


class TextFile:
    def __init__(self, path, content):
        self.path = path
        self._content = content

    @property
    def content(self):
        if self.issupported():
            return "\n" + html.escape(self._content)
        return ""

    def issupported(self):
        return self._content is not None


def error(msg):
    print(msg, file=sys.stderr)
    exit(1)


def getscriptpath():
    return os.path.dirname(os.path.realpath(__file__))


def collect_subpaths(dirpath):
    return gitignore.filterpaths(dirpath)


# Source http://stackoverflow.com/a/1446870
def istext(filename):
    bytecount = 1000
    try:
        with open(filename, "r+b") as f:
            content = f.read(bytecount)
    except (PermissionError, TypeError):
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


def readfile(path):
    if istext(path):
        with open(path, encoding="utf8") as f:
            return f.read()
    return None


def writeoutput(content):
    outdir = os.path.join(getscriptpath(), OUTDIR)
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    outpath = os.path.join(outdir, OUTFILE)

    with open(outpath, "w", encoding="utf8") as f:
        f.write(content)

    return outpath


def main():
    if len(sys.argv) != 2:
        error('Give a dirctory name as only argument.')
    
    dirpath = sys.argv[1]
    if not os.path.exists(dirpath):
        error('Directory not found.')

    subpaths = collect_subpaths(dirpath)
    contents = [readfile(path) for path in subpaths]
    files = [TextFile(path, content) for path, content in zip(subpaths, contents)]

    templatepath = os.path.join(getscriptpath(), "template.html")
    with open(templatepath, encoding="utf8") as f:
        template_content = f.read()

    template = jinja2.Template(template_content)
    rendered = template.render(
        path=dirpath,
        files=files
    )

    outpath = writeoutput(rendered)
    webbrowser.open(outpath)


if __name__ == '__main__':
    main()

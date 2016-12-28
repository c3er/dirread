#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Algorithm based on
# https://git-scm.com/docs/gitignore#_pattern_format
# not completely


import os
import collections
import enum
import fnmatch


class PathType(enum.Enum):
    unknown = 0
    file = 1
    directory = 2


class IgnoreList(collections.UserList):
    _always_ignored = [
        ".git",
    ]

    def __init__(self, ignores):
        super().__init__(ignores)

    def matches(self, filepath):
        filename = _getlastpathpart(filepath)
        if filename in self._always_ignored:
            return True
        if os.path.isdir(filepath):
            filetype = PathType.directory
        else:
            filetype = PathType.file
        for ignore in self.data:
            if ignore.matches(filename, filetype):
                return True
        return False


def parse(filepath):
    with open(filepath, encoding="utf8") as f:
        ignores = f.readlines()
    unfiltered = [_create_ignore(ignore) for ignore in ignores]
    return IgnoreList([ignore for ignore in unfiltered if ignore is not None])


def filterpaths(dirpath):
    files = os.listdir(dirpath)
    if ".gitignore" in files:
        ignores = parse(os.path.join(dirpath, ".gitignore"))
        files = [file for file in files if not ignores.matches(os.path.join(dirpath, file))]
    pathlist = []
    subfiles = []
    for file in files:
        filepath = os.path.join(dirpath, file)
        if os.path.isdir(filepath):
            subfiles += filterpaths(filepath)
        else:
            pathlist.append(filepath)
    return pathlist + subfiles


class _Ignore:
    def __init__(self, pattern):
        (
            self.pattern,
            self.isnegative,
            self.filetype,
        ) = self._parse_pattern(pattern)

    def matches(self, filename, filetype):
        result = filetype == self.filetype and fnmatch.fnmatch(filename, self.pattern)
        if self.isnegative:
            result = not result
        return result

    @staticmethod
    def _parse_pattern(pattern):
        isnegative = False
        filetype = PathType.file
        if pattern.startswith("\\"):
            pattern = pattern[1:]
        elif pattern.startswith("!"):
            isnegative = True
            pattern = pattern[1:]
        if pattern.endswith("/"):
            filetype = PathType.directory
            pattern = pattern[:-1]
        return (
            pattern,
            isnegative,
            filetype,
        )


def _create_ignore(pattern):
    pattern = pattern.strip()
    if not pattern or pattern.startswith("#") or pattern.startswith("!"):
        # XXX Workaround: ignore negative patterns
        return None
    return _Ignore(pattern)


def _getlastpathpart(path):
    return os.path.basename(os.path.normpath(path))

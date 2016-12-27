#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Algorithm based on
# https://git-scm.com/docs/gitignore#_pattern_format
# not completely


import os
import collections
import enum
import fnmatch


class PatternType(enum.Enum):
    unknown = 0
    file = 1
    directory = 2


class IgnoreList(collections.UserList):
    _ignored = [
        ".git",
    ]

    def __init__(self, patterns):
        super().__init__(patterns)

    def matches(self, filepath):
        filename = _getlastpathpart(filepath)
        if filename in self._ignored:
            return True
        if os.path.isdir(filepath):
            filetype = PatternType.directory
        else:
            filetype = PatternType.file
        for ignore in self.data:
            if ignore.matches(filename, filetype):
                return True
        return False


def parse(filepath):
    with open(filepath, encoding="utf8") as f:
        patterns = f.readlines()
    unfiltered = [_create_ignore(pattern) for pattern in patterns]
    return IgnoreList([pattern for pattern in unfiltered if pattern is not None])


def filterpaths(dirpath):
    files = os.listdir(dirpath)
    if ".gitignore" in files:
        ignores = parse(os.path.join(dirpath, ".gitignore"))
        files = [file for file in files if not ignores.matches(file)]
    pathlist = []
    subfiles = []
    for file in files:
        filepath = os.path.join(dirpath, file)
        if os.path.isdir(filepath):
            subfiles.append(filterpaths(filepath))
        else:
            pathlist.append(filepath)
    return pathlist + subfiles


class _Ignore:
    def __init__(self, pattern):
        (
            self.pattern,
            self.isnegative,
            self.patterntype,
        ) = self._parse_pattern(pattern)

    def matches(self, filename, filetype):
        result = filetype == self.patterntype and fnmatch.fnmatch(filename, self.pattern)
        if self.isnegative:
            result = not result
        return result

    @staticmethod
    def _parse_pattern(pattern):
        isnegative = False
        patterntype = PatternType.file
        if pattern.startswith("\\"):
            pattern = pattern[1:]
        elif pattern.startswith("!"):
            isnegative = True
            pattern = pattern[1:]
        if pattern.endswith("/"):
            patterntype = PatternType.directory
            pattern = pattern[:-1]
        return (
            pattern,
            isnegative,
            patterntype,
        )


def _create_ignore(pattern):
    pattern = pattern.strip()
    if not pattern or pattern.startswith("#"):
        return None
    return _Ignore(pattern)


def _getlastpathpart(path):
    return os.path.basename(os.path.normpath(path))

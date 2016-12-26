#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Algorithm ported from
# https://git-scm.com/docs/gitignore#_pattern_format
# not completely


import os
import collections
import fnmatch


class IgnoreList(collections.UserList):
    def __init__(self, patterns):
        super().__init__(patterns)
        self.ignored = [
            ".git",
        ]

    def matches(self, filepath):
        filename = _getlastpathpart(filepath)
        if filename in self.ignored:
            return True
        for pattern in self.data:
            if pattern.matches(filename):
                return True
        return False


def parse(filepath):
    with open(filepath, encoding="utf8") as f:
        patterns = f.readlines()
    unfiltered = [_create_ignore(pattern) for pattern in patterns]
    return IgnoreList([pattern for pattern in unfiltered if pattern is not None])


class _Ignore:
    def __init__(self, pattern, isnegative):
        self.isnegative = isnegative
        self.pattern = pattern

    def matches(self, filename):
        result = fnmatch.fnmatch(filename, self.pattern)
        if self.isnegative:
            result = not result
        return result


def _create_ignore(pattern):
    pattern = pattern.strip()
    if not pattern or pattern.startswith("#"):
        return None
    isnegative = False
    if pattern.startswith("\\"):
        pattern = pattern[1:]
    elif pattern.startswith("!"):
        isnegative = True
        pattern = pattern[1:]
    if pattern.endswith("/"):
        pattern = pattern[:-1]
    return _Ignore(pattern, isnegative)


def _getlastpathpart(path):
    return os.path.basename(os.path.normpath(path))

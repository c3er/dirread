#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os


def getlastpathpart(path):
    return os.path.basename(os.path.normpath(path))

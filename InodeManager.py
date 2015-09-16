#!/usr/bin/env python
#encoding=utf8

import subprocess
import os

def DirList(path):
    args = 'ls '
    pipe = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE).stdout
    result = pipe.readlines()

    filelist = []
    for item in result:
        filelist.append(item.strip())

    return filelist

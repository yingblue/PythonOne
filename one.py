#!/usr/bin/env python

import InodeManager

path='/home/yt/Code'
result = InodeManager.DirList()

for item in result:
    print item

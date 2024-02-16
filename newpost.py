#!/usr/bin/env python3

import sys
import os
import time

number = str(int(sorted(os.listdir("posts"))[-1][0:4]) + 1)
index = (4 - len(number)) * '0' + number
filename = 'posts/' + index + '-' + '-'.join(sys.argv[1:]).lower() + '.txt'

title = ' '.join(sys.argv[1:])
date = time.strftime("%a, %d %b %Y")
tags = ''
rule = max(len(title), len(time)) * '='

#file = open(filename, "w")
#file.write(title + '\n' + date + '\n' + tags + '\n' + rule)
#file.close()

with open(filename, 'w') as file:
    file.write(title + '\n' + date + '\n' + tags + '\n' + rule)

os.system("vim " + filename)

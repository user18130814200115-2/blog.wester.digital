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
rule = max(len(title), len(date)) * '='

footer = '''\
All of my writing and software projects are available free of
charge under CC-BY unless stated otherwise. I do not accept
monetary donations, but if my work has brought you value I ask
you to donate to a charitable cause or high-impact fund,
organisation, business, institute, or individual driving moral
progress.
'''

#file = open(filename, "w")
#file.write(title + '\n' + date + '\n' + tags + '\n' + rule)
#file.close()

with open(filename, 'w') as file:
    file.write(title + '\n' + date + '\n' + tags + '\n' + rule + '\n' * 3 + footer)

os.system("vim " + filename)

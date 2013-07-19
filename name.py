#!/usr/bin/env python

import random
from sets import Set

word_list = Set()
word_source = open('words.txt', 'r')

for line in word_source:
    word = line.rstrip('\n').replace(' ', '-').capitalize()
    word_list.add(word)

name = random.sample(word_list, 2)

print ''.join(name)



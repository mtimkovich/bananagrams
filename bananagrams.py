#!/usr/bin/env python
import random

# Create list of all the letters and shuffle it
def make_bunch():
    bunch = []

    for l in ['j', 'k', 'q', 'x', 'z']:
        for i in xrange(2):
            bunch.append(l)

    for l in ['b', 'c', 'f', 'h', 'm', 'p', 'v', 'w', 'y']:
        for i in xrange(3):
            bunch.append(l)

    for i in xrange(4):
        bunch.append('g')

    for i in xrange(5):
        bunch.append('l')

    for l in ['d', 's', 'u']:
        for i in xrange(6):
            bunch.append(l)

    for i in xrange(8):
        bunch.append('n')

    for l in ['t', 'r']:
        for i in xrange(9):
            bunch.append(l)

    for i in xrange(11):
        bunch.append('o')

    for i in xrange(12):
        bunch.append('i')

    for i in xrange(13):
        bunch.append('a')

    for i in xrange(18):
        bunch.append('e')

    random.shuffle(bunch)

    return bunch

# Check if a word can be spelt using the letters in your hand
def is_subset(a, b):
    subset = True
    a = sorted(a)
    b = sorted(b)

    a_prev = None
    b_prev = None

    if len(a) > len(b):
        subset = False

    while subset and len(a) > 0 and len(b) > 0:
        if a[-1] == b[-1]:
            a_prev = a.pop()
            b_prev = b.pop()
        elif a[-1] < b[-1]:
            b.pop()
        else:
            subset = False

        if len(a) > len(b):
            subset = False

    return subset

bunch = make_bunch()

hand = []

for i in xrange(21):
    hand.append(bunch.pop())

print sorted(hand)
print

file = open("TWL06.txt")

for line in file:
    line = line.strip()
    
    if is_subset(line, hand):
        print line

file.close()

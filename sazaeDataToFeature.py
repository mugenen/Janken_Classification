# -*- coding: utf-8 -*-

import csv
import collections as cs
import sys

def handNumber(hand):
    number = cs.defaultdict(lambda: -1)
    number['グー'] = 0
    number['チョキ'] = 1
    number['パー'] = 2
    
    return number[hand]

def printFeature(csvData, n = 1):
    history = cs.deque([])
    for index, year, month, day, hand in csv.reader(csvData):
        num = handNumber(hand)
        length = len(history)
        if length >= n:
            if num != -1 and all([h != -1 for h in history]):
                print num,
                for i, h in enumerate(history):
                    print '{}:1'.format(h + 3 * i),
                print
        
            history.popleft()
    
        history.append(num)

if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv < 1:
        print 'Usage: python {} n(>= 1)'.format(sys.argv[0])
        exit()
    else:
        printFeature(sys.stdin, int(sys.argv[1]))


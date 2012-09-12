# -*- coding: utf-8 -*-

#get data from http://www.asahi-net.or.jp/~tk7m-ari/sazae_ichiran.html

import BeautifulSoup as bs
import urllib2
import collections as cs
import datetime as dt

def normalizedYear(year):
    return int(year) + 2000 if year < 91 else int(year) + 1900

def readData():
    result = []
    response = urllib2.urlopen('http://www.asahi-net.or.jp/~tk7m-ari/sazae_ichiran.html')
    soup = bs.BeautifulSoup(response)
    
    for i in soup.body.contents[9].contents:
        if i.string and len(i.string.strip()) != 0:
            split = i.strip().split()
            
            index = int(split[0][1:-1])
            
            year, month, day = map(int, split[1].split('.'))
            year = normalizedYear(year)
            #the data contain illegal date: 91.11.31
            if year == 1991 and month == 11 and day == 31:
                date = dt.date(year, month + 1, 1)
            else:
                date = dt.date(year, month, day)
            
            hand = split[2]
            
            result.append((index, date, hand))
    result.reverse()
    return result


if __name__ == '__main__':
    for index, date, hand in readData():
        print u'{},{},{},{},{}'.format(index, date.year, date.month, date.day, hand).encode('utf-8')

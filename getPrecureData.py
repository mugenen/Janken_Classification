# -*- coding: utf-8 -*-

#get data from http://dic.nicovideo.jp/a/%E3%82%AD%E3%83%A5%E3%82%A2%E3%83%94%E3%83%BC%E3%82%B9vs%E3%82%B5%E3%82%B6%E3%82%A8%E3%81%95%E3%82%93
import BeautifulSoup as bs
import urllib2


def readData():
    result = []
    response = urllib2.urlopen('http://dic.nicovideo.jp/a/%E3%82%AD%E3%83%A5%E3%82%A2%E3%83%94%E3%83%BC%E3%82%B9vs%E3%82%B5%E3%82%B6%E3%82%A8%E3%81%95%E3%82%93')
    soup = bs.BeautifulSoup(response)
    for tr in soup.find('tbody').contents[3:]:
        if tr.contents[2].contents[0].string:
            result.append(tr.contents[2].contents[0].string.strip())
        else:
            if tr.contents[2].contents[0].find('span'):
                result.append(tr.contents[2].contents[0].find('span').string.strip())
    return result


if __name__ == '__main__':
    for hand in readData():
        print u'{}'.format(hand).encode('utf-8')

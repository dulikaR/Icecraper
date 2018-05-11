import threading
from threading import Thread
import datetime
import requests
from bs4 import BeautifulSoup

def scrape(url):
    urlName = url
    soup = BeautifulSoup( requests.get( urlName ).content )
    name = soup.find_all( 'div', attrs={'class': 'a-expander-content a-expander-partial-collapse-content'} )
    review = soup.findAll( 'span', {'class': 'a-size-base a-link-normal review-title a-color-base a-text-bold'} )

    for g in name:
        print g.text

    for l in review:
        print l.text


class myThreadOne(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        # print self.url
        scrape( self.url )
        # time.sleep(5)

class myThreadTwo(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        # print self.url
        # print self.url
        scrape( self.url )
        # time.sleep(5)

class myThreadThree(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        # print self.url
        # print self.url
        scrape( self.url )
        # time.sleep(5)

class myThreadfour(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        # print self.url
        # print self.url
        scrape( self.url )
        # time.sleep(5)

class myThreadfive(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        # print self.url
        # print self.url
        scrape( self.url )
        # time.sleep(5)




def func1(array):
    # print array
    for url in array:
        thread = myThreadOne( url )
        thread.start()
    print " thread one started "

def func2(array):
    # print array
    for url in array:
        thread = myThreadTwo( url )
        thread.start()
    print " thread two started "

def func3(array):
    # print array
    for url in array:
        thread = myThreadThree( url )
        thread.start()
    print " thread three started "

def func4(array):
    # print array
    for url in array:
        thread = myThreadfour( url )
        thread.start()
    print " thread four started "

def func5(array):
    # print array
    for url in array:
        thread = myThreadfive( url )
        thread.start()
    print " thread five started "




def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out


def sendToThreads(array):
    # array = ['https://github.com/jeanphix/Ghost.py/issues/290',
    #          'https://docs.python.org/2/library/functions.html#isinstance',
    #          'http://www.instructables.com/id/View-any-Web-Content-as-Virtual-Reality/',
    #          'https://jsonformatter.curiousconcept.com/', 'https://github.com/jeanphix/Ghost.py/issues/290',
    #          'https://docs.python.org/2/library/functions.html#isinstance',
    #          'http://www.instructables.com/id/View-any-Web-Content-as-Virtual-Reality/',
    #          'https://jsonformatter.curiousconcept.com/', 'https://github.com/jeanphix/Ghost.py/issues/290',
    #          'https://docs.python.org/2/library/functions.html#isinstance',
    #          'http://www.instructables.com/id/View-any-Web-Content-as-Virtual-Reality/',
    #          'https://jsonformatter.curiousconcept.com/', 'https://github.com/jeanphix/Ghost.py/issues/290',
    #          'https://docs.python.org/2/library/functions.html#isinstance',
    #          'http://www.instructables.com/id/View-any-Web-Content-as-Virtual-Reality/',
    #          'https://jsonformatter.curiousconcept.com/', 'https://github.com/jeanphix/Ghost.py/issues/290',
    #          'https://docs.python.org/2/library/functions.html#isinstance',
    #          'http://www.instructables.com/id/View-any-Web-Content-as-Virtual-Reality/',
    #          'https://jsonformatter.curiousconcept.com/']

    a = chunkIt( array, 5 )

    start = datetime.datetime.now()
    Thread(target = func1(a[0])).start()
    Thread(target = func2(a[1])).start()
    Thread( target=func3(a[2]) ).start()
    Thread( target=func4(a[3]) ).start()
    Thread( target=func5(a[4]) ).start()
    end = datetime.datetime.now()

#
# if __name__ == '__main__':
#     sendToThreads()



















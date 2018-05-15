import threading
from threading import Thread
import datetime
from selenium import webdriver


def scrape(url):
    driver = webdriver.Chrome( "C:\chromedriver.exe" )
    driver.get( url )

def func1(array):
    print array
    for url in array:
        scrape( url )
    print " thread one started "

def func2(array):
    print array
    for url in array:
        scrape( url )
    print " thread two started "

def func3(array):
    print array
    for url in array:
        scrape( url )
    print " thread three started "

def func4(array):
    print array
    for url in array:
        scrape( url )
    print " thread four started "

def func5(array):
    print array
    for url in array:
        scrape( url )
    print " thread five started "




def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out


def sendToThreads():
    array = ['https://github.com/jeanphix/Ghost.py/issues/290',
             'https://docs.python.org/2/library/functions.html#isinstance',
             'http://www.instructables.com/id/View-any-Web-Content-as-Virtual-Reality/',
             'https://jsonformatter.curiousconcept.com/', 'https://github.com/jeanphix/Ghost.py/issues/290',
             'https://docs.python.org/2/library/functions.html#isinstance',
             'http://www.instructables.com/id/View-any-Web-Content-as-Virtual-Reality/',
             'https://jsonformatter.curiousconcept.com/', 'https://github.com/jeanphix/Ghost.py/issues/290',
             'https://docs.python.org/2/library/functions.html#isinstance',
             'http://www.instructables.com/id/View-any-Web-Content-as-Virtual-Reality/',
             'https://jsonformatter.curiousconcept.com/', 'https://github.com/jeanphix/Ghost.py/issues/290',
             'https://docs.python.org/2/library/functions.html#isinstance',
             'http://www.instructables.com/id/View-any-Web-Content-as-Virtual-Reality/',
             'https://jsonformatter.curiousconcept.com/', 'https://github.com/jeanphix/Ghost.py/issues/290',
             'https://docs.python.org/2/library/functions.html#isinstance',
             'http://www.instructables.com/id/View-any-Web-Content-as-Virtual-Reality/',
             'https://jsonformatter.curiousconcept.com/']

    a = chunkIt( array, 5 )

    start = datetime.datetime.now()
    Thread(target = func1(a[0])).start()
    Thread(target = func2(a[1])).start()
    Thread( target=func3(a[2]) ).start()
    Thread( target=func4(a[3]) ).start()
    Thread( target=func5(a[4]) ).start()
    end = datetime.datetime.now()


if __name__ == '__main__':
    sendToThreads()



















import threading
from threading import Thread
import datetime
import requests
from bs4 import BeautifulSoup
from scraperjs import scraperjs


class threadone(threading.Thread):
    def __init__(self, url,tagList):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        # print self.url
        scraperjs(self.url, self.tagList)
        # time.sleep(5)

class threadtwo(threading.Thread):
    def __init__(self, url,tagList):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        # print self.url
        # print self.url
        scraperjs(self.url, self.tagList)
        # time.sleep(5)

class threadthree(threading.Thread):
    def __init__(self, url,tagList):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        # print self.url
        # print self.url
        scraperjs(self.url, self.tagList)
        # time.sleep(5)

class threadfour(threading.Thread):
    def __init__(self, url,tagList):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        # print self.url
        # print self.url
        scraperjs(self.url, self.tagList)
        # time.sleep(5)

class threadfive(threading.Thread):
    def __init__(self, url,tagList):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        # print self.url
        # print self.url
        scraperjs(self.url, self.tagList)
        # time.sleep(5)


class createthreads:

    def func1(array,tagList):
        # print array
        for url in array:
            thread = threadone(url, tagList)
            thread.start()
        print " thread one started "

    def func2(array,tagList):
        # print array
        for url in array:
            thread = threadtwo(url, tagList)
            thread.start()
        print " thread two started "

    def func3(array,tagList):
        # print array
        for url in array:
            thread = threadthree(url, tagList)
            thread.start()
        print " thread three started "

    def func4(array,tagList):
        # print array
        for url in array:
            thread = threadfour(url, tagList)
            thread.start()
        print " thread four started "

    def func5(array,tagList):
        # print array
        for url in array:
            thread = threadfive(url, tagList)
            thread.start()
        print " thread five started "


class arraybreaker:

    def chunkIt(seq, num):
        avg = len(seq) / float(num)
        out = []
        last = 0.0

        while last < len(seq):
            out.append(seq[int(last):int(last + avg)])
            last += avg
        return out


    def sendToThreads(array,tagList):

        arrb = arraybreaker()
        crt = createthreads()
        chunckedurls = arrb.chunkIt( array, 5 )

        start = datetime.datetime.now()
        Thread(target = crt.func1(chunckedurls[0],tagList)).start()
        Thread(target = crt.func2(chunckedurls[1],tagList)).start()
        Thread( target= crt.func3(chunckedurls[2],tagList) ).start()
        Thread( target= crt.func4(chunckedurls[3],tagList) ).start()
        Thread( target= crt.func5(chunckedurls[4],tagList) ).start()
        end = datetime.datetime.now()

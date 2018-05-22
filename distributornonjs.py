import threading
from threading import Thread
import datetime
import requests
from bs4 import BeautifulSoup
from scraperjs import scraperjs, scrapeSingleSet, scrapeSequentialSets


class threadone(threading.Thread):
    def __init__(self, url,dataset_id,tagList,methodType):
        threading.Thread.__init__(self)
        self.url = url
        self.dataset_id
        self.tagList = tagList
        self.methodType = methodType

    def run(self):
        single = scrapeSingleSet()
        sequen = scrapeSequentialSets()

        if(self.methodType == 1):
            single.bytagid(self.url, self.tagList)
        elif(self.methodType == 2):
            single.bycommontagid(self.url, self.tagList)
        elif (self.methodType == 3):
            sequen.splitLines(self.url, self.dataset_id, self.tagList)
        elif (self.methodType == 4):
            sequen.bycommontagid(self.url, self.dataset_id, self.tagList)
        else:
            print "wrong method type given"


class threadtwo(threading.Thread):
    def __init__(self, url,dataset_id,tagList,methodType):
        threading.Thread.__init__(self)
        self.url = url
        self.dataset_id
        self.tagList = tagList
        self.methodType = methodType

    def run(self):
        single = scrapeSingleSet()
        sequen = scrapeSequentialSets()

        if(self.methodType == 1):
            single.bytagid(self.url, self.tagList)
        elif(self.methodType == 2):
            single.bycommontagid(self.url, self.tagList)
        elif (self.methodType == 3):
            sequen.splitLines(self.url, self.dataset_id, self.tagList)
        elif (self.methodType == 4):
            sequen.bycommontagid(self.url, self.dataset_id, self.tagList)
        else:
            print "wrong method type given"

class threadthree(threading.Thread):
    def __init__(self, url,dataset_id,tagList,methodType):
        threading.Thread.__init__(self)
        self.url = url
        self.dataset_id
        self.tagList = tagList
        self.methodType = methodType

    def run(self):
        single = scrapeSingleSet()
        sequen = scrapeSequentialSets()

        if(self.methodType == 1):
            single.bytagid(self.url, self.tagList)
        elif(self.methodType == 2):
            single.bycommontagid(self.url, self.tagList)
        elif (self.methodType == 3):
            sequen.splitLines(self.url, self.dataset_id, self.tagList)
        elif (self.methodType == 4):
            sequen.bycommontagid(self.url, self.dataset_id, self.tagList)
        else:
            print "wrong method type given"

class threadfour(threading.Thread):
    def __init__(self, url,dataset_id,tagList,methodType):
        threading.Thread.__init__(self)
        self.url = url
        self.dataset_id
        self.tagList = tagList
        self.methodType = methodType

    def run(self):
        single = scrapeSingleSet()
        sequen = scrapeSequentialSets()

        if(self.methodType == 1):
            single.bytagid(self.url, self.tagList)
        elif(self.methodType == 2):
            single.bycommontagid(self.url, self.tagList)
        elif (self.methodType == 3):
            sequen.splitLines(self.url, self.dataset_id, self.tagList)
        elif (self.methodType == 4):
            sequen.bycommontagid(self.url, self.dataset_id, self.tagList)
        else:
            print "wrong method type given"

class threadfive(threading.Thread):
    def __init__(self, url,dataset_id,tagList,methodType):
        threading.Thread.__init__(self)
        self.url = url
        self.dataset_id
        self.tagList = tagList
        self.methodType = methodType

    def run(self):
        single = scrapeSingleSet()
        sequen = scrapeSequentialSets()

        if(self.methodType == 1):
            single.bytagid(self.url, self.tagList)
        elif(self.methodType == 2):
            single.bycommontagid(self.url, self.tagList)
        elif (self.methodType == 3):
            sequen.splitLines(self.url, self.dataset_id, self.tagList)
        elif (self.methodType == 4):
            sequen.bycommontagid(self.url, self.dataset_id, self.tagList)
        else:
            print "wrong method type given"


class createthreads:

    def func1(array,dataset_id,tagList,methodType):
        for url in array:
            thread = threadone(url,dataset_id, tagList,methodType)
            thread.start()
        print " thread one started "

    def func2(array,dataset_id,tagList,methodType):
        for url in array:
            thread = threadtwo(url,dataset_id, tagList,methodType)
            thread.start()
        print " thread one started "

    def func3(array,dataset_id,tagList,methodType):
        for url in array:
            thread = threadthree(url,dataset_id, tagList,methodType)
            thread.start()
        print " thread one started "

    def func4(array,dataset_id,tagList,methodType):
        for url in array:
            thread = threadfour(url,dataset_id, tagList,methodType)
            thread.start()
        print " thread one started "

    def func5(array,dataset_id,tagList,methodType):
        for url in array:
            thread = threadfive(url,dataset_id, tagList,methodType)
            thread.start()
        print " thread one started "


class arraybreaker:

    def chunkIt(seq, num):
        avg = len(seq) / float(num)
        out = []
        last = 0.0

        while last < len(seq):
            out.append(seq[int(last):int(last + avg)])
            last += avg
        return out


    def sendToThreads(array,dataset_id,tagList,methodType):

        arrb = arraybreaker()
        crt = createthreads()
        chunckedurls = arrb.chunkIt( array, 5 )

        start = datetime.datetime.now()
        Thread(target = crt.func1(chunckedurls[0],dataset_id,tagList,methodType)).start()
        Thread(target = crt.func2(chunckedurls[1],dataset_id,tagList,methodType)).start()
        Thread( target= crt.func3(chunckedurls[2],dataset_id,tagList,methodType)).start()
        Thread( target= crt.func4(chunckedurls[3],dataset_id,tagList,methodType)).start()
        Thread( target= crt.func5(chunckedurls[4],dataset_id,tagList,methodType)).start()
        end = datetime.datetime.now()

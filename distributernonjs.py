import threading
from threading import Thread
import datetime
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from monitarizingmanager import machinePerformance
from scraperjs import scrapeSingleSet, scrapeSequentialSets


class threadone(threading.Thread):
    def __init__(self, url, dataset_id, tagList, methodType):
        threading.Thread.__init__(self)
        self.url = url
        self.dataset_id = dataset_id
        self.tagList = tagList
        self.methodType = methodType

    def run(self):
        single = scrapeSingleSet()
        sequen = scrapeSequentialSets()

        # driver = webdriver.Chrome("C:\chromedriver4.exe")

        if (self.methodType == 1):
            single.bytagid(self.url, self.tagList)
        elif (self.methodType == 2):
            single.bycommontagid(self.url, self.tagList)
        elif (self.methodType == 3):
            sequen.splitLines(self.url, self.dataset_id, self.tagList)
        elif (self.methodType == 4):
            sequen.bycommontagid(self.url, self.dataset_id, self.tagList)
        else:
            print "wrong method type given"


class createthreads:
    def func1(self, array, dataset_id, tagList, methodType):
        for url in array:
            thread = threadone(url, dataset_id, tagList, methodType)
            thread.start()
        print "new thread started "


class arraybreakerNonJS:
    def chunkIt(self, seq, num):
        avg = len(seq) / float(num)
        out = []
        last = 0.0

        while last < len(seq):
            out.append(seq[int(last):int(last + avg)])
            last += avg
        return out

    def sendToThreadsNonJs(self, array, dataset_id, tagList, methodType):

        mp = machinePerformance()
        first_value = next((el for el in array if el is not None), None) #to get the firt not null value in this 'array' list
        chunkTerm = mp.promptmachine(first_value)  # sending url to monitor & do the calculation to decide thread count
        arrb = arraybreakerNonJS()
        crt = createthreads()
        chunckedurls = arrb.chunkIt(array, chunkTerm)

        if(chunkTerm == 0 or chunkTerm >9):
            for incrment_time in range(4):
                start = datetime.datetime.now()
                Thread(target=crt.func1(chunckedurls[incrment_time], dataset_id, tagList, methodType)).start()
                end = datetime.datetime.now()
        else:
            for incrment_time in range(chunkTerm):
                start = datetime.datetime.now()
                Thread(target=crt.func1(chunckedurls[incrment_time], dataset_id, tagList, methodType)).start()
                end = datetime.datetime.now()

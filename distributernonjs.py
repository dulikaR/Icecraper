import threading
from threading import Thread
import datetime
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from uimanager import uimanagerclass
from databasemanager import database
from monitarizingmanager import machinePerformance
from scraperjs import scrapeSingleSet, scrapeSequentialSets


def startScrapingInThreads(url, dataset_id, tagList, methodType):
    single = scrapeSingleSet()
    sequen = scrapeSequentialSets()

    if (methodType == 1):
        result = single.bytagid(url, tagList)
    elif (methodType == 2):
        result = single.bycommontagid(url, tagList)
    elif (methodType == 3):
        result = sequen.splitLines(url, dataset_id, tagList)
    elif (methodType == 4):
        result = sequen.bycommontagid(url, dataset_id, tagList)
    else:
        print "wrong method type given"
    return result

class threadone(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs, Verbose)
        self._return = None

    def run(self):
        if self._Thread__target is not None:
            self._return = self._Thread__target(*self._Thread__args,
                                                **self._Thread__kwargs)

    def join(self):
        Thread.join(self)
        return self._return



class createthreads:

    def func1(self, array, dataset_id, tagList, methodType):
        reult_set_list_one = []
        for url in array:
            thread = threadone(target=startScrapingInThreads, args=(url, dataset_id, tagList, methodType,))
            thread.start()
            reult_set_list_one.append(thread.join())
        print "New Agent started"
        db = database()
        db.json(reult_set_list_one)
        ui = uimanagerclass()
        ui.scrapingstartedui(len(array))




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
        reult_set_list_two_combine = []

        if(chunkTerm == 0 or chunkTerm >9):
            for incrment_time in range(4):
                start = datetime.datetime.now()
                Thread(target=crt.func1,args = (chunckedurls[incrment_time], dataset_id, tagList, methodType)).start()
                end = datetime.datetime.now()
        else:
            for incrment_time in range(chunkTerm):
                start = datetime.datetime.now()
                Thread(target=crt.func1,args = (chunckedurls[incrment_time], dataset_id, tagList, methodType)).start()
                end = datetime.datetime.now()

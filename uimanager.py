# -*- coding: utf-8 -*-
import time
from time import sleep

import datetime
import progressbar as progressbar
import sys
import psutil

class uimanagerclass:

    def startui(self):
        print "######### - '█'IceScraper Started'█' - #########"
        print ""
        print "Started Time : " + str(datetime.datetime.now())

    def startpagingui(self,numOfPages):
        nop = str(numOfPages)
        print "Pages Count : " + nop

    def startextractingproductsurlui(self,numOfproducts):
        nop = str(numOfproducts)
        print "Item Pages Count : " + nop

    def creatingAgentsui(self):
        # agentsBars
        print "'█'AGENT STARETED HIS JOB'█'" + " (sub agents are been creating)"

        for i in range(100):
            sys.stdout.write('\r[{0}{1}] {2}'.format('█' * (i / 10), ' ' * (10 - i / 10), i))
            time.sleep(0.1)

        print "                       "
        print "                       "

    def startmonitorizingui(self,a,l,free_memory,one_page_time,thredsCount):
        print "                       "
        print "                       "
        print "######### - '█' Gathering Machine Performances '█' - #########"
        print "                       "
        # System Info
        print "Single Page Consuming Time : " + str(one_page_time)
        print "Virtual Memory : " + str(l)
        print "Available Memory : " +str(free_memory)
        print "Internet I/O : " + str(l)
        print "Number Of Agents : " + str(thredsCount)
        print "                       "
        print "                       "

    def agentsStartedui(self):
        print "'█'SUB AGENTS ON WORK'█'"
        # red bars
        bar = progressbar.ProgressBar(maxval=20,
                                      widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
        bar.start()
        for i in xrange(10):
            bar.update(i + 1)
            sleep(1)
            bar.finish()
            if (i != 0):
                print "Site No " + str(i + 1) + " successfully scraped"

        print "                       "
        print "                       "

    def scrapingstartedui(self,arrayLength):
        print "######### - '█'Finishing Scraping Job'█' - #########"
        # final finished bar
        bar = progressbar.ProgressBar()
        for i in bar(range(arrayLength)):
            time.sleep(0.57)

        print "                       "
        print "                       "

    def finishingui(self,result,type):

        print "                       "
        print "                       "

        print "'█' Scraped Files -- "+str(result)+"  '█'"
        # print "'█' Failuers      -- 4   '█'"
        print "'█' Saved as      -- "+type+" '█'"
        print datetime.datetime.now()











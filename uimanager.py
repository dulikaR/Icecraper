# -*- coding: utf-8 -*-
import time
from time import sleep

import datetime
import progressbar as progressbar
import sys
import psutil

class ui:

    def startui(self):
        print "######### - '█'IceScraper Started'█' - #########"
        print ""
        print datetime.datetime.now()

    def startpagingui(self):
        print ""

    def startextractingproductsurlui(self):
        print ""

    def creatingAgentsui(self):
        # agentsBars
        print "'█'AGENT STARETED HIS JOB'█'" + " (sub agents are been creating)"

        for i in range(100):
            sys.stdout.write('\r[{0}{1}] {2}'.format('█' * (i / 10), ' ' * (10 - i / 10), i))
            time.sleep(0.1)

        print "                       "
        print "                       "
        print "                       "

    def startmonitorizingui(self):
        print "######### - Gathering Machine Performances - #########"
        print "                       "
        # System Info
        print "'█' CPU Percentage '█'"
        print psutil.cpu_percent()
        print "                       "
        print "'█' Virtual Memory '█'"
        print psutil.virtual_memory()
        print "                       "
        print "'█' Internet I/O   '█'"
        print psutil.net_io_counters(pernic=False)

        print "                       "
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
        print "                       "

    def scrapingstartedui(self):
        print "'█'Finishing Scraping Job'█'"
        # final finished bar
        bar = progressbar.ProgressBar()
        for i in bar(range(100)):
            time.sleep(0.47)

        print "                       "
        print "                       "
        print "                       "

    def finishingui(self):

        print "'█' Scraped Files -- 97  '█'"
        print "'█' Failuers      -- 4   '█'"
        print "'█' Saved as      -- API '█'"

        print datetime.datetime.now()











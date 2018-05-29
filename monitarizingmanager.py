from time import clock

import psutil
from selenium import webdriver

#this file will help to bypass the obstacles while mimicing through web sites
from uimanager import uimanagerclass


class timegap():

    def timeDecider(self): #this will decide the time gap that needed to be among js handling
        print "example"

    def timegapcreater(self): #this will create random or relevent numbers to be
        print "example"


class machinePerformance():

    def promptmachine(self,url): #prompting machine performances to create relevant threads

        memory_status = psutil.virtual_memory()
        free_memory = memory_status[4]

        util = utils()
        start = clock()
        process = psutil.Process(util.selenium_test_run(url)) #run selenium to test the consumptions
        one_page_time = (clock()-start)
        a = process.memory_info().rss
        l = process.io_counters()[2]

        thredsCount = self.decidethreads(a, l,free_memory)
        if(thredsCount == 0):
            thredsCount = 1

        ui = uimanagerclass()
        ui.startmonitorizingui(a,l,free_memory,one_page_time,thredsCount)

        return thredsCount

    def decidethreads(self,a,l,free_memory): #decide the amount of threads
        count_one = (free_memory / a)
        count_two = (l / 100000)
        threads_count = count_one/count_two
        return threads_count


class utils:

    def network_speed_test(self):
        def checkone():
            import time
            import psutil
            import os

            count = 0
            qry = ''

            ul = 0.00
            dl = 0.00
            t0 = time.time()
            connection_details = psutil.net_io_counters(pernic=False)
            upload = connection_details[0]
            download = connection_details[1]
            up_down = (upload, download)

            while True:
                last_up_down = up_down
                connection_details_new = psutil.net_io_counters(pernic=False)
                upload = connection_details_new[0]
                download = connection_details_new[1]
                t1 = time.time()
                up_down = (upload, download)
                try:
                    ul, dl = [(now - last) / (t1 - t0) / 1024.0
                              for now, last in zip(up_down, last_up_down)]
                    t0 = time.time()
                except:
                    pass
                if dl > 0.1 or ul >= 0.1:
                    time.sleep(0.75)
                    os.system('cls')
                    print('UL: {:0.2f} kB/s \n'.format(ul) + 'DL: {:0.2f} kB/s'.format(dl))

            v = input()

    def selenium_test_run(self,url):
        driver = webdriver.Chrome("C:\chromedriver4.exe")
        driver.get(url)
        driver.quit()



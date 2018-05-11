import threading
import time
from selenium import webdriver




threads = []

urlList = ['https://github.com/jeanphix/Ghost.py/issues/290', 'https://docs.python.org/2/library/functions.html#isinstance', 'http://www.instructables.com/id/View-any-Web-Content-as-Virtual-Reality/', 'https://jsonformatter.curiousconcept.com/']

class myThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        print self.url
        driver = webdriver.Chrome( "C:\chromedriver.exe" )
        driver.get( self.url )
        # time.sleep(5)

for url in urlList:
    thread = myThread(url)
    thread.start()
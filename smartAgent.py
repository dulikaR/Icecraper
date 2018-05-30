from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random

#sitemap.xml
#robots.txt
from scraperjs import scrapeSingleSet

class smartAgentClass:


    def start_agent(self, driver, UL,tag_list):
        chrome_options = Options()
        chrome_options.add_extension('Testings\SetupVPN - Lifetime Free VPN.crx')
        driver = webdriver.Chrome(executable_path="C:\chromedriver4.exe", chrome_options=chrome_options)

        driver.get(UL)
        wait = random.uniform(0, 1)
        sleep(wait)

        sss = scrapeSingleSet()
        sss.bycommontagid(UL,tag_list,driver)


    def load_data(self,tag_list):

        driver = webdriver.Chrome("C:\chromedriver4.exe")

        urlList = ['https://www.everlane.com/products/womens-bikini-palepink?collection=womens-underwear',
                   'https://www.everlane.com/products/womens-bikini-black?collection=womens-underwear',
                   'https://www.everlane.com/products/womens-bikini-white?collection=womens-underwear',
                   'https://www.everlane.com/products/womens-bikini-heathergrey?collection=womens-underwear',
                   'https://www.everlane.com/products/womens-hipster-black?collection=womens-underwear']


        for UL in urlList:
            self.start_agent(driver, UL, tag_list)






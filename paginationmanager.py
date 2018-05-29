from time import sleep
from selenium import webdriver


class pagination:

    def startPaging(self, url, xpath):
        headerUrls = []

        driver = webdriver.Chrome("C:\chromedriver4.exe")
        driver.get(url)
        stop = False

        while stop == False:
            try:
                headerUrls.append(driver.current_url)
                sleep(3)
                element = driver.find_element_by_css_selector(xpath)
                driver.execute_script("arguments[0].click();", element)
                # headerUrls.append(driver.current_url)
                # print driver.current_url
            except:
                stop = True

        driver.quit()
        return headerUrls


    def getItemPages(self, pageUrls, xpath):

        itemListUrl = []
        i = 0
        driver = webdriver.Chrome("C:\chromedriver4.exe")
        for page in pageUrls:

            try:
                driver.get(page)
                itemList = driver.find_elements_by_css_selector(xpath)  # .get_attribute( 'href' )

                for item in itemList:
                    itemUrl = item.get_attribute('href')
                    # print itemUrl
                    itemListUrl.append(itemUrl)
            except:
                print ""
            driver.quit()

        return itemListUrl


    def getItemPagesTwoForALLProducts(self,driver, page, xpath):

        itemListUrl = []
        i = 0
        try:
            driver.get(page)
            itemList = driver.find_elements_by_css_selector(xpath)  # .get_attribute( 'href' )

            for item in itemList:
                itemUrl = item.get_attribute('href')
                # print itemUrl
                itemListUrl.append(itemUrl)
        except:
            print "error in item urls scraping"

        i += 1
        a = itemListUrl
        return itemListUrl


    def pageingAndProducts(self, url, xpath,productXpath):
        allItems = []

        driver = webdriver.Chrome("C:\chromedriver4.exe")
        driver.get(url)
        stop = False
        newUrl = ''
        i=0

        while stop == False:
            try:
                newUrl = driver.current_url
                itemList = self.getItemPagesTwoForALLProducts(driver, newUrl, productXpath)
                allItems.append(itemList)
                driver.find_element_by_css_selector(xpath).click()  # .get_attribute('href')
                sleep(2)
            except:
                stop = True

        driver.quit()
        return allItems



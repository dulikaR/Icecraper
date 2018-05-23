from time import sleep
from selenium import webdriver


class pagination:

    def startPaging(url, xpath):
        headerUrls = []

        driver = webdriver.Chrome("C:\chromedriver4.exe")
        driver.get(url)
        stop = False

        while stop == False:
            try:
                headerUrls.append(driver.current_url)
                newUrl = driver.find_element_by_css_selector(xpath).get_attribute('href')
                sleep(2)
                driver.get(newUrl)
                headerUrls.append(driver.current_url)
                # print driver.current_url
            except:
                stop = True
        return headerUrls


    def getItemPages(pageUrls, xpath):

        itemListUrl = []
        i = 0
        for page in pageUrls:

            try:
                driver = webdriver.Chrome("C:\chromedriver4.exe")
                driver.get(page)
                itemList = driver.find_elements_by_css_selector(xpath)  # .get_attribute( 'href' )

                for item in itemList:
                    itemUrl = item.get_attribute('href')
                    # print itemUrl
                    itemListUrl.append(itemUrl)
            except:
                print "error in item urls scraping"
            driver.quit()

        i += 1

        return itemListUrl

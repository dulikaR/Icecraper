from time import sleep
from selenium import webdriver
from arrayBreakerJs import sendToThreads


def startPaging(url,xpath):
    print "Paging started for the site "
    # url  = "https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=amante&rh=i%3Aaps%2Ck%3Aamante"
    # xpath = "#pagnNextLink"
    headerUrls = []

    driver = webdriver.Chrome( "C:\chromedriver4.exe" )
    driver.get( url )
    stop = False

    while stop == False:
        try:
            headerUrls.append( driver.current_url )
            newUrl = driver.find_element_by_css_selector( xpath ).get_attribute( 'href' )
            sleep( 2 )
            driver.get( newUrl )
            headerUrls.append( driver.current_url )
            # print driver.current_url
        except:
            stop = True
    print "Paging ended for the site "
    return headerUrls


def getItemPages(pageUrls,xpath):

    print "items urls grabbing started for the site "
    # xpath = ".a-size-small.a-text-normal"   #.a-size-small.a-text-normal
    # pageUrls = ["https://www.amazon.in/s/ref=sr_pg_9?rh=i%3Aaps%2Ck%3Aamante&page=9&keywords=amante&ie=UTF8&qid=1525949240,https://www.amazon.in/s/ref=sr_pg_10?rh=i%3Aaps%2Ck%3Aamante&page=10&keywords=amante&ie=UTF8&qid=1525949243"]
    # itemList = []
    itemListUrl = []
    i = 0
    for page in pageUrls:

        try:
            driver = webdriver.Chrome( "C:\chromedriver4.exe" )
            driver.get( page )
            itemList = driver.find_elements_by_css_selector( xpath )#.get_attribute( 'href' )

            for item in itemList:
                itemUrl = item.get_attribute( 'href' )
                # print itemUrl
                itemListUrl.append(itemUrl)
        except:
            print "error in item urls scraping"
        driver.quit()

    i += 1
    print i

    print "items urls grabbing ended for the site "
    return itemListUrl


def startScraping(urlArray):
    print "scraping started for the site "
    sendToThreads(urlArray)
    print "scraping ended for the site "







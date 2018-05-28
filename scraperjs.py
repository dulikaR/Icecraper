from time import sleep

import requests
from bs4 import BeautifulSoup
import unicodedata
from selenium import webdriver
from databasemanager import database



class scrapeSingleSet:

    def bytagid(self,urls,tag_list):
        finalResult = []
        urlName = urls
        soup = BeautifulSoup(requests.get(urlName).content, "lxml")

        name = soup.find('div', attrs={'class': 'item-top col-12 lg-8'})
        price = soup.find('div', attrs={'class': 'ui-price-tag'})
        details = soup.find('div', attrs={'class': 'item-description'})

        element_one = 'NULL'
        element_three = 'NULL'
        element_four = 'NULL'

        element_one = str(unicodedata.normalize('NFKD', (name.text)).encode('ascii', 'ignore'))
        element_three = str(unicodedata.normalize('NFKD', (price.text)).encode('ascii', 'ignore'))
        element_four = str(unicodedata.normalize('NFKD', (details.text)).encode('ascii', 'ignore'))



        finalResult.append(element_one)
        finalResult.append(element_three)
        finalResult.append(element_four)

        # db = database()
        # db.json(finalResult)
        return finalResult


    def bycommontagid(self,url,tag_list,driver):

        finalResultikman = []
        urlName = url
        soup = BeautifulSoup(requests.get(urlName).content)

        name = soup.find('div', attrs={'class': 'item-top col-12 lg-8'})
        price = soup.find('div', attrs={'class': 'ui-price-tag'})
        details = soup.find('div', attrs={'class': 'item-description'})

        element_one = 'NULL'
        element_three = 'NULL'
        element_four = 'NULL'

        element_one = str(name.text)

        element_three = str(price.text)

        element_four = str(details.text)

        finalResultikman.append(element_one, element_three, element_four)

        db = database()
        db.json(finalResultikman)


class scrapeSequentialSets:

    def splitLines(self,urls, data_set_id, data_list,driver): #gather data by data sets & split the lines to find required variables

        urls = filter(None, urls)
        for url in urls:
            split_line_list = []
            driver.get(str(url))

            DataSet = driver.find_elements_by_xpath(data_set_id) #"//div[@class='review review-index__review']"
            full_data_set = []

            for rs in DataSet:

                data1 = rs.text
                data = str(unicodedata.normalize('NFKD', data1).encode('ascii', 'ignore')).splitlines()
                data_set_part = []

                for dl in data:
                    data_set_part.append(dl)

                data_set_part = filter(None, data_set_part)
                full_data_set.append(data_set_part)

            split_line_list.append(full_data_set)

            # print split_line_list
            db = database()
            db.json(split_line_list)
            sleep(2)


    def bycommontagid(self, urls, tag_list, common_tag,driver):
        for url in urls:
            by_common_tag_id_list = []

            driver.get(url)

            common_tag_object_list = driver.find_elements_by_xpath(common_tag)

            resultList = []

            for ctol in common_tag_object_list:

                result_sub_list = []

                for tl in tag_list:
                    list_attribute = ctol.find_elements_by_xpath(tl[1])
                    result_sub_list.append(tl[0], list_attribute)

                    by_common_tag_id_list.append(result_sub_list)

        return by_common_tag_id_list



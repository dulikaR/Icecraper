import requests
from bs4 import BeautifulSoup
import unicodedata
from selenium import webdriver


class scrapeSingleSet:

    def bytagid(self,url,tag_list):
        by_tag_id_list = []

        return by_tag_id_list

    def bycommontagid(self,url,tag_list):
        by_common_tag_id_list = []

        driver = webdriver.Chrome("C:\chromedriver4.exe")
        driver.get(url)

        result_sub_list = []

        for tl in tag_list:
            list_attribute = driver.find_elements_by_xpath(tl[1])
            result_sub_list.append(tl[0], list_attribute)

            by_common_tag_id_list.append(result_sub_list)

        return by_common_tag_id_list


class scrapeSequentialSets:

    def splitLines(self,url, data_set_id, data_list): #gather data by data sets & split the lines to find required variables

        split_line_list = []
        driver = webdriver.Chrome("C:\chromedriver4.exe")
        driver.get(url)

        DataSet = driver.find_elements_by_xpath(data_set_id) #"//div[@class='review review-index__review']"
        i=0
        full_data_set = []

        for rs in DataSet:

            data1 = rs.text
            data = str(unicodedata.normalize('NFKD', data1).encode('ascii', 'ignore')).splitlines()
            data_set_part = []

            i+=1
            k=0

            for dl in data_list:
                k+=1
                data_set_part.append(data[k])

            full_data_set.append(data_set_part)

        split_line_list.append(full_data_set)

        return split_line_list

    def bycommontagid(self, url, tag_list, common_tag):
        by_common_tag_id_list = []

        driver = webdriver.Chrome("C:\chromedriver4.exe")
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



from time import sleep

import requests
from bs4 import BeautifulSoup
import unicodedata
from selenium import webdriver


class scrapeSingleSet:

    def bytagid(self,urls,tag_list,driver):
        by_tag_id_list = []

        return by_tag_id_list

    def bycommontagid(self,urls,tag_list,driver):
        for url in urls:
            by_common_tag_id_list = []

            driver.get(url)

            result_sub_list = []

            for tl in tag_list:
                list_attribute = driver.find_elements_by_xpath(tl[1])
                result_sub_list.append(tl[0], list_attribute)

                by_common_tag_id_list.append(result_sub_list)

        return by_common_tag_id_list


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

                full_data_set.append(data_set_part)

            split_line_list.append(full_data_set)

            print split_line_list

            sleep(7)

        return split_line_list

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



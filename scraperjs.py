import requests
from bs4 import BeautifulSoup
import unicodedata
from selenium import webdriver




class scrapeSingleSet:

    def bytagid(self):
        by_tag_id_list = []

        return by_tag_id_list

    def bycommontagid(self,url,tag_list):
        by_common_tag_id_list = []

        driver = webdriver.Chrome("C:\chromedriver4.exe")
        driver.get(url)

        resultList = []

        for ts in tag_list:
            reult_sub_list = []
            list_attribute = driver.find_element_by_xpath("//" + ts.tag + "[@" + ts.tag_id + "=" + ts.tag_variable + "]")
            reult_sub_list.append(ts.name, list_attribute)

            by_common_tag_id_list.append(reult_sub_list)

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


    def bytagid(self,url,tag_list):  # gather data by data sets & get requiered variables by tag ids

        by_tag_id_list = []
        driver = webdriver.Chrome("C:\chromedriver4.exe")
        driver.get(url)

        resultList = []

        for ts in tag_list:
            reult_sub_list = []
            list_attribute =  driver.find_element_by_xpath( "//"+ts.tag+"[@"+ts.tag_id+"="+ts.tag_variable+"]")
            reult_sub_list.append(ts.name , list_attribute)

            by_tag_id_list.append(reult_sub_list)

        return by_tag_id_list

class Taglist:

    def __init__(self, name, tag, tag_id, tag_variable):
        self.name = name
        self.tag = tag
        self.tag_id = tag_id
        self.tag_variable = tag_variable


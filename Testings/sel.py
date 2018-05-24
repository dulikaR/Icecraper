import unicodedata
from selenium import webdriver


driver = webdriver.Chrome("C:\chromedriver4.exe")

url = "https://www.amazon.in/English-General-Competitions-Neetu-Singh/dp/9384636568/ref=sr_1_4?ie=UTF8&qid=1527153178&sr=8-4&keywords=kd+campus+english"

driver.get(url)

DataSet = driver.find_elements_by_xpath("//div[@class='a-section review']")

for rs in DataSet:
    data1 = rs.text
    data = str(unicodedata.normalize('NFKD', data1).encode('ascii', 'ignore')).splitlines()
    print data
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options



chrome_options = Options()
chrome_options.add_extension('SetupVPN - Lifetime Free VPN.crx')

driver = webdriver.Chrome(executable_path="C:\chromedriver4.exe", chrome_options=chrome_options)

driver.get('https://www.techopedia.com/definition/5393/site-map')

sleep(10)
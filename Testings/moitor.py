import sys
import psutil
from selenium import webdriver

url = "https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=amante&rh=i%3Aaps%2Ck%3Aamante"
#
# cpu_percent =  psutil.cpu_percent()
b =  psutil.virtual_memory()
total = b[0]
# available = b[1]
# percent = b[2]
used = b[3]
free = b[4]
#
#
# c=  psutil.net_io_counters(pernic=False, nowrap=True)
#
# bytes_sent = c[0]
# bytes_recv = c[1]
# packets_sent = c[2]
# packets_recv = c[3]
# errin = c[4]
# errout = c[5]
# dropin = c[6]
# dropout = c[7]
#
#
# l = psutil.cpu_percent(interval=10)
#
#
# driver = webdriver.Chrome("C:\chromedriver4.exe")
# driver.get(url)
# print 'loaded'
# d =  psutil.net_io_counters(pernic=False)
#
#
# bytes_sent2 = d[0]
# bytes_recv2 = d[1]
#
#
# print bytes_sent
# print bytes_sent2
#
# print ""
#
# print bytes_recv
# print bytes_recv2
#
# print ""
#
# print percent
# abcdg = l[2]
#
# print abcdg
#
#
# print 'done'

#snetio(bytes_sent=27956116L, bytes_recv=313745371L, packets_sent=159652L, packets_recv=674365L, errin=0L, errout=0L, dropin=0L, dropout=0L)

#svmem(total=8463278080L, available=2957225984L, percent=65.1, used=5506052096L, free=2957225984L)

print total
print used
print free

def selenium():
    driver = webdriver.Chrome("C:\chromedriver4.exe")
    driver.get(url)
    driver.quit()


process = psutil.Process(selenium())
a = process.memory_info().rss
l= process.io_counters()
print(process.memory_info().rss)

vone = (free/a)
vtwo = (l[2]/100000)

print vone
print vtwo


print "number of threads =  " + str((free/a)/(l[2]/100000))


print l


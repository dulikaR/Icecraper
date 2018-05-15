import requests
from bs4 import BeautifulSoup


def scraperjs(url, tagList):
    urlName = url

    for tags in tagList:

        soup = BeautifulSoup(requests.get(urlName).content)
        name = soup.find_all('div', attrs={'class': 'a-expander-content a-expander-partial-collapse-content'})
        review = soup.findAll('span', {'class': 'a-size-base a-link-normal review-title a-color-base a-text-bold'})
        tags[0] = soup.find_all(tags[1], attrs={tags[2]: tags[3]})

        for g in name:
            print g.text

        for l in review:
            print l.text

class jsscraper:


    def scrapeSingleSet(self):
        print ""


    def scrapeSequentialSets(self):
        print ""




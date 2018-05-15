from paginationmanager import startPaging, getItemPages, startScraping




class simpleScrape:
    def scrapeStart(self):
        tagList = [('name', 'div', 'class', 'a-expander-content a-expander-partial-collapse-content'),
                   ('review', 'span', 'class', 'a-size-base a-link-normal review-title a-color-base a-text-bold')]

        url = "https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=amante&rh=i%3Aaps%2Ck%3Aamante"
        a = startPaging(url, "#pagnNextLink")
        b = getItemPages(a, ".a-size-small.a-text-normal")
        startScraping(b,tagList)  # (b, xpathlist, output)

if __name__ == '__main__':
    s = simpleScrape()
    s.scrapeStart()


# class Tags:
#     def autoLankaScrapper(self, carName):
#         finalResultautoLanka = []
#
#         y = 'NULL'
#         u = 'NULL'
#         i = 'NULL'
#         o = 'NULL'
#
#         finalResultautoLanka.append( Cars( y, u, i, o ) )
#         return finalResultautoLanka
#
# class Tags:
#
#     def __init__(self, name, link, price, url):
#         self.name = name
#         self.link = link
#         self.price = price
#         self.url = url
# #








from IceAgent import Agent




# class simpleScrape:
#     def scrapeStart(self):
#         tagList = [('name', 'div', 'class', 'a-expander-content a-expander-partial-collapse-content'),
#                    ('review', 'span', 'class', 'a-size-base a-link-normal review-title a-color-base a-text-bold')]
#
#         url = "https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=amante&rh=i%3Aaps%2Ck%3Aamante"
#         a = startPaging(url, "#pagnNextLink")
#         b = getItemPages(a, ".a-size-small.a-text-normal")
#         startScraping(b,tagList)  # (b, xpathlist, output)

if __name__ == '__main__':

    print 'starting'

    url = "https://www.amazon.in/s/ref=nb_sb_ss_i_3_2/257-1071178-2985039?url=search-alias%3Daps&field-keywords=kd+campus+english&sprefix=kd%2Caps%2C461&crid=3SF45KNVERQC6&rh=i%3Aaps%2Ck%3Akd+campus+english"

    tagList = [('name', 'div', 'class', 'a-expander-content a-expander-partial-collapse-content'),
               ('review', 'span', 'class', 'a-size-base a-link-normal review-title a-color-base a-text-bold')]

    agent = Agent()

    a = agent.start_paging(url, "#pagnNextLink")
    b = agent.get_product_in_pages(a,".a-size-small.a-text-normal")
    agent.scrape_sequential_sests_with_split_lines(b,"//div[@class='a-section review']",[(a),(b)])
    print "finish"




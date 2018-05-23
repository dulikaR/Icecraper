from IceAgent import Agent
from paginationmanager import startPaging, getItemPages, startScraping




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

    url = "https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=amante&rh=i%3Aaps%2Ck%3Aamante"

    tagList = [('name', 'div', 'class', 'a-expander-content a-expander-partial-collapse-content'),
               ('review', 'span', 'class', 'a-size-base a-link-normal review-title a-color-base a-text-bold')]

    agent = Agent()

    a = agent.start_paging(url, "#pagnNextLink")
    b = agent.get_product_in_pages(a,".a-size-small.a-text-normal")
    agent.scrape_single_sests_with_common_tag_id(b,tagList)




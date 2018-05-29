import datetime

from IceAgent import Agent


def startAmazon():

    url = "https://www.amazon.in/s/ref=nb_sb_ss_i_3_2/257-1071178-2985039?url=search-alias%3Daps&field-keywords=kd+campus+english&sprefix=kd%2Caps%2C461&crid=3SF45KNVERQC6&rh=i%3Aaps%2Ck%3Akd+campus+english"

    tagList = [('name', 'div', 'class', 'a-expander-content a-expander-partial-collapse-content'),
               ('review', 'span', 'class', 'a-size-base a-link-normal review-title a-color-base a-text-bold')]

    agent = Agent()

    a = agent.start_paging(url, "#pagnNextLink")
    b = agent.get_items_in_pages(a,".a-size-small.a-text-normal")
    agent.scrape_sequential_sests_with_split_lines(b,"//div[@class='a-section review']",tagList)
    print "finish"


def startIkman():

    url = "https://ikman.lk/en/ads/dehiwala/rooms-annexes?categoryType=ads&categoryName=Rooms+%26+Annexes&type=for_rent"

    tag_list = [['name', 'div', 'class', 'item-top col-12 lg-8'], ['price', 'div', 'class', 'ui-price-tag'],
                ['details', 'div', 'class', 'item-description']]

    agent = Agent()

    b = agent.start_paging_and_get_all_items(url,".pag-next span",".item-title")
    agent.scrape_single_sests_with_tag_id(b,tag_list)
    xx = agent.get_json_obj()
    print xx


if __name__ == '__main__':
    # startIkman()
    startAmazon()





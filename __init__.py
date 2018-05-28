import datetime

from IceAgent import Agent




if __name__ == '__main__':

    # print 'starting'
    # print datetime.datetime.now()
    #
    # url = "https://www.amazon.in/s/ref=nb_sb_ss_i_3_2/257-1071178-2985039?url=search-alias%3Daps&field-keywords=kd+campus+english&sprefix=kd%2Caps%2C461&crid=3SF45KNVERQC6&rh=i%3Aaps%2Ck%3Akd+campus+english"
    #
    # tagList = [('name', 'div', 'class', 'a-expander-content a-expander-partial-collapse-content'),
    #            ('review', 'span', 'class', 'a-size-base a-link-normal review-title a-color-base a-text-bold')]
    #
    # agent = Agent()
    #
    # a = agent.start_paging(url, "#pagnNextLink")
    # b = agent.get_items_in_pages(a,".a-size-small.a-text-normal")
    # agent.scrape_sequential_sests_with_split_lines(b,"//div[@class='a-section review']",[(a),(b)])
    # print "finish"


    url = "https://ikman.lk/en/ads/dehiwala/rooms-annexes?categoryType=ads&categoryName=Rooms+%26+Annexes&type=for_rent"

    tagList = [('name', 'div', 'class', 'a-expander-content a-expander-partial-collapse-content'),
               ('review', 'span', 'class', 'a-size-base a-link-normal review-title a-color-base a-text-bold')]

    agent = Agent()


    a = agent.start_paging(url,".pag-next span")
    b = agent.get_items_in_pages(a,".item-title")
    agent.scrape_single_sests_with_tag_id(b,[])
    xx = agent.get_json_obj()
    print "finish"




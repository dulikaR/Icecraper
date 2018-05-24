from paginationmanager import pagination
from distributorjs import arraybreaker


class Agent:

    def start(self):
        print ""

    def get_product_in_pages(self,page_list, tag_id):
        p = pagination()
        product_list = p.getItemPages(page_list, tag_id)
        return product_list


    def start_paging(self,page_link,tag_id):
        p = pagination()
        page_list = p.startPaging(page_link, tag_id)
        return page_list


    def scrape_single_sests_with_tag_id(self,array,tagList):
        ab = arraybreaker()
        dataset_id = ""
        ab.sendToThreads(array,dataset_id,tagList,1)
        print ""

    def scrape_single_sests_with_common_tag_id(self,array,tagList):
        ab = arraybreaker()
        dataset_id = ""
        ab.sendToThreads(array, dataset_id, tagList, 2)
        print ""

    def scrape_sequential_sests_with_split_lines(self,array,dataset_id,tagList):
        ab = arraybreaker()
        ab.sendToThreads(array, dataset_id, tagList, 3)
        print ""

    def scrape_sequential_sests_with_common_tag_id(self,array,dataset_id,tagList):
        ab = arraybreaker()
        ab.sendToThreads(array, dataset_id, tagList, 4)
        print ""



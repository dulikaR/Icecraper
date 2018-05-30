from smartAgent import smartAgentClass
from uimanager import uimanagerclass
from databasemanager import jsonObjects, database
from distributernonjs import arraybreakerNonJS
from paginationmanager import pagination
from distributorjs import arraybreaker


class Agent:

    def start(self):
        print ""

    def get_items_in_pages(self,page_list, tag_id):
        p = pagination()
        product_list = p.getItemPages(page_list, tag_id)
        ui = uimanagerclass()
        ui.startextractingproductsurlui(len(product_list))
        return product_list


    def start_paging(self,page_link,tag_id):
        p = pagination()
        ui = uimanagerclass()
        ui.startui()
        page_list = p.startPaging(page_link, tag_id)
        ui.startpagingui(len(page_list))
        return page_list

    def start_paging_and_get_all_items(self,page_link,tag_id,item_id):
        p = pagination()
        ui = uimanagerclass()
        ui.startui()
        all_items = p.pageingAndProducts(page_link, tag_id,item_id)
        all_items_flat_list = [item for sublist in all_items for item in sublist]
        ui.startextractingproductsurlui(len(all_items_flat_list))
        return all_items_flat_list


    def scrape_single_sests_with_tag_id(self,array,tagList):
        ab = arraybreakerNonJS()
        dataset_id = ""
        ab.sendToThreadsNonJs(array,dataset_id,tagList,1)
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

    def get_json_obj(self):
        db = jsonObjects()
        object = db.get_json_from_file()
        ui = uimanagerclass()
        ui.finishingui(len(object),"JSON")
        return object

    def create_mysql(self,jsonFile, db_name, table_name):
        db = database()
        db.sql(jsonFile, db_name, table_name)
        ui = uimanagerclass()
        ui.finishingui(len(jsonFile), "SQL TABLE CREATED")

    def write_to_csv(self,table_name,db_name):
        db = database()
        db.toCsv(table_name,db_name)
        ui = uimanagerclass()
        ui.finishingui(len(0), "CSV FILE CREATED")

    def start_smart_agent(self,tag_list):
        sac = smartAgentClass()
        sac.load_data(tag_list)







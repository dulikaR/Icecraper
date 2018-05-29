import datetime
import json
import os
import sys
import json
# from IPy import IP

class database:

    def sql(self):
        print ""


    def json(self,final_data_set):
        if not final_data_set:
            print""
        else:
            for list_one in final_data_set:
                print list_one

        with open('data.txt', 'w') as outfile:
            json.dump(final_data_set, outfile)

        print datetime.datetime.now()


class jsonObjects:

    def get_json_from_file(self):
        with open('data.txt', 'r') as jobj:
            data = json.load(jobj)

        return data
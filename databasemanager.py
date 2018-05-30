import csv
import datetime
import json
import MySQLdb

# from IPy import IP

class database:

    def sql(self, jsonFile, db_name, table_name):

        str_list = []
        if(len(jsonFile) < 2):
            str_list = jsonFile[0]
        else:
            str_list = jsonFile

        str_list_clean = filter(None, str_list)
        column_list = []
        for jf in str_list_clean[1]:
            column_list.append(jf[0])

        db = MySQLdb.connect("localhost", "root", "", db_name, charset='utf8')

        table_name = table_name
        createsqltable = """CREATE TABLE IF NOT EXISTS """ + table_name + " (" + " VARCHAR(2050),".join(
            column_list) + " VARCHAR(2050))"
        cursor = db.cursor()
        cursor.execute(createsqltable)
        db.commit()

        self.insertToSql(str_list_clean,db,table_name)

    def insertToSql(self,str_list_clean,db,table_name):

        column_list = []
        value_list = []
        for jf in str_list_clean:
            column_list = []
            value_list = []
            for val in jf:
                column_list.append(val[0])
                value_list.append(val[1])

            query_placeholders = ', '.join(['%s'] * len(value_list))
            query_columns = ', '.join(column_list)

            try:
                insert_query = ''' INSERT INTO ''' + table_name + ''' (%s) VALUES (%s) ''' % (query_columns, query_placeholders)
                cursor = db.cursor()
                cursor.execute(insert_query, value_list)
                db.commit()
            except:
                some = "error"









    def json(self,final_data_set):
        if not final_data_set:
            print""
        else:
            for list_one in final_data_set:
                fgh = ""

        with open('data.txt', 'w') as outfile:
            json.dump(final_data_set, outfile)

        print datetime.datetime.now()

    def toCsv(self,table_name,db_name):

        db = MySQLdb.connect("localhost", "root", "", db_name, charset='utf8')
        cursor = db.cursor()

        cursor.execute("select * from "+table_name)

        res = cursor.fetchall()
        with open('output.csv', 'w') as fw:
            writer = csv.writer(fw)
            writer.writerows(res)



class jsonObjects:

    def get_json_from_file(self):
        with open('data.txt', 'r') as jobj:
            data = json.load(jobj)

        return data
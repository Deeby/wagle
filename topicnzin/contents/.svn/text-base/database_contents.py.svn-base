#-*- coding: utf-8 -*-
import MySQLdb

class DataBaseContents:
    def __init__(self, host="indf.net", user="tastingplace", passwd="tastingplace",db="tastingplace"):
        self._connect = MySQLdb.connect(host=host,user=user,passwd=passwd,db=db)

    def create_cursor(self):
        return self._connect.cursor(MySQLdb.cursors.DictCursor)

    def document(self, docid):
        cursor = self.create_cursor()
        cursor.execute("set names utf8")
        cursor.execute("select entry_id as docid, date_format(entry_pub_date,'%Y%m%d') as regdate, entry_content as contents, entry_title as title from tastingplace.tb_entry where entry_id = " + str(docid))
        content = cursor.fetchone()
        cursor.close()
        if not content:
            return ""

        return content

    def documents(self, docids):
        cursor = self.create_cursor()
        cursor.execute("set names utf8")

        for docid in docids:
            cursor.execute("select entry_id as docid, date_format(entry_pub_date,'%Y%m%d') as regdate, entry_content as contents , entry_title as title from tastingplace.tb_entry where entry_id = " + str(docid))
            content = cursor.fetchone()
            yield content

        cursor.close()

    # def documents(self, start_yyyymmdd, end_yyyymmdd):
    #     sql = 'select entry_content from tastingplace.tb_entry'
    #     sql = sql + " where "
    #     sql = sql + " entry_register_time between str_to_date('"+start_yyyymmdd+" 000000','%Y%m%d %H%i%s')"
    #     sql = sql + " and "
    #     sql = sql + " str_to_date('"+end_yyyymmdd+" 235959','%Y%m%d %H%i%s') limit 5"
    #
    #     print "11 "
    #
    #     cursor = self.create_cursor()
    #
    #     print "22-0"
    #     cursor.execute("set names utf8")
    #     print "22-01"
    #     print sql
    #     cursor.execute(sql)
    #     print "22-1"
    #     contents = cursor.fetchall()
    #     print "22-2"
    #     output = [contents['entry_content'] for row in contents]
    #     cursor.close()
    #
    #     print "33 "
    #
    #     return output


if __name__ == "__main__":
    dbs = DataBaseContents()
    seq = 1
    for doc in dbs.documents([1,2,3,4,5]):
        print seq , doc["contents"]
        seq += 1
    print "end"
# -*- coding: utf-8 -*-
import MySQLdb

#DB 처리 관련 클래스 
class dbhandler(object):
    
    db = ""
    
    def __init__(self, db):
        self.db = db;
        
    
 
    #make select sql, later groupy by, having 
    def createSelectSql(self, sql):

        columnStm = sql["columnStm"] 
        fromStm = sql["fromStm"]
        whereStm = sql["whereStm"]
        orderbyStm = sql["orderbyStm"]
        etcStm = sql["etcStm"]


        sqlStm = "select "
        columnSize = len(columnStm)
 

        for i in range(0, columnSize): 

            if i != columnSize-1:
                sqlStm += columnStm[i]+","
            else:
                sqlStm += columnStm[i] 



        if len(fromStm) !=0:
            sqlStm += " from " + fromStm
        else:
            print("select sql stm : no from")

        if len(whereStm)!=0:
            sqlStm +=" where " + whereStm
        
        if len(orderbyStm)!=0:
            sqlStm +=" order by " + orderbyStm

        if len(etcStm)!=0: 
            sqlStm +=" " + etcStm
        


        sqlStm+=";"
         
        return sqlStm

    def runSql(self, sql):
        db = MySQLdb.connect(host="indf.net",user="tastingplace",passwd="tastingplace",db=self.db,charset="utf8",use_unicode=True)
        cursor = db.cursor(MySQLdb.cursors.DictCursor)

        sqlStm = self.createSelectSql(sql) 
         
        cursor.execute(sqlStm)
        result = cursor.fetchall()
        cursor.close()

        size = len(result)
        
        keyList = sql["columnStm"];

    
        rowList =[]
        for i in range(0, size):
            row={}
            for col in keyList:
                if "as" in col: #as 구문 처리 
                    colSplit = col.split("as")
                    col = colSplit[len(colSplit)-1].strip()

                row[col] = result[i][col]
            
            rowList.append(row)

        return rowList; 


         
 
if __name__ == '__main__':
    dc = dbhandler();
    column = ["count(entry_id)"]
    fromStm ="tb_entry"
    whereStm ="" 
    orderbyStm =""
    etcStm = ""
 
    sql={"columnStm":column, 
        "fromStm":fromStm, 
        "whereStm":whereStm,
        "orderbyStm":orderbyStm,
        "etcStm":etcStm}
    

    print(dc.runSql(sql))



# -*- coding: utf-8 -*- 

from dbhandler import *; 
from place import *; 

#FoodSpot 관련 데이터베이스 처리 클래스 
class foodspot_controller(object):
    dbh = dbhandler("FoodSpot");
    
    column = []
    fromStm =""
    whereStm ="" 
    orderbyStm =""
    etcStm = ""
 
    sql={}
    
  
    def __init__(self):
        pass
    
    
    
    def getPlaceBySpotId(self, spotId):
    #spotID 로 맛집 정보를 가져온다. 
        
        tastingplace = place();
        
        self.column = ["spot_id", "name", "addr", "tel", "detail", "close_day", "business_hour", "budget", "parking", "links", "second_info", "popular_menu"]
        self.fromStm ="tb_food_spot"
        self.whereStm ="spot_id= " + str(spotId) 
        self.orderbyStm =""
        self.ectStm = ""
        self.sql={"columnStm":self.column, 
             "fromStm":self.fromStm, 
             "whereStm":self.whereStm,
             "orderbyStm":self.orderbyStm,
             "etcStm":self.etcStm}
        
        
        foodSpotResult = self.dbh.runSql(self.sql)[0]
        
        tastingplace.spotId = int(foodSpotResult["spot_id"])
        tastingplace.name = foodSpotResult["name"]
        tastingplace.addr = foodSpotResult["addr"]
        tastingplace.tel = foodSpotResult["tel"]
        tastingplace.detail = foodSpotResult["detail"]
        tastingplace.close_day = foodSpotResult["close_day"]
        tastingplace.business_hour = foodSpotResult["business_hour"]
        tastingplace.budget = foodSpotResult["budget"]
        tastingplace.parking = foodSpotResult["parking"]
        tastingplace.links = foodSpotResult["links"] 
        
        if foodSpotResult["second_info"] is not None:
            tastingplace.second_info = foodSpotResult["second_info"].split("^")
         
        tastingplace.popularmenu = foodSpotResult['popular_menu']
     
        
        self.column = ["bus", "subway"] 
        self.fromStm ="tb_spot_transport"
        self.whereStm ="spot_id = " + str(tastingplace.spotId) 
        self.orderbyStm =""
        self.ectStm = ""
        self.sql={"columnStm":self.column, 
             "fromStm":self.fromStm, 
             "whereStm":self.whereStm,
             "orderbyStm":self.orderbyStm,
             "etcStm":self.etcStm}
        
        transportResult = self.dbh.runSql(self.sql)[0]
        tastingplace.bus = transportResult['bus'].split(",")
        tastingplace.subway = transportResult['subway'].split(",")
        
        return tastingplace;
        
    def getPlaceById(self, id):
    #id 로 맛집 정보를 가져온다.
        tastingplace = place();
        
        self.column = ["spot_id", "name", "addr", "tel", "detail", "close_day", "business_hour", "budget", "parking", "links", "second_info", "popular_menu","latitude","longitude"]
        self.fromStm ="tb_food_spot"
        self.whereStm ="id = " + id 
        self.orderbyStm =""
        self.ectStm = "" 
        self.sql={"columnStm":self.column, 
             "fromStm":self.fromStm, 
             "whereStm":self.whereStm,
             "orderbyStm":self.orderbyStm,
             "etcStm":self.etcStm}
        
        
        foodSpotResult = self.dbh.runSql(self.sql)[0]
        
        tastingplace.spotId = int(foodSpotResult["spot_id"])
        tastingplace.name = foodSpotResult["name"]
        tastingplace.addr = foodSpotResult["addr"]
        tastingplace.tel = foodSpotResult["tel"]
        tastingplace.detail = foodSpotResult["detail"]
        tastingplace.close_day = foodSpotResult["close_day"]
        tastingplace.business_hour = foodSpotResult["business_hour"]
        tastingplace.budget = foodSpotResult["budget"]
        tastingplace.parking = foodSpotResult["parking"]
        tastingplace.links = foodSpotResult["links"] 
        tastingplace.latitude = foodSpotResult["latitude"]
        tastingplace.longitude = foodSpotResult["longitude"]
        
        
        if foodSpotResult["second_info"] is not None:
            tastingplace.second_info = foodSpotResult["second_info"].split("^")
         
        tastingplace.popularmenu = foodSpotResult['popular_menu']
     
        
        self.column = ["bus", "subway"] 
        self.fromStm ="tb_spot_transport"
        self.whereStm ="spot_id = " + str(tastingplace.spotId) 
        self.orderbyStm =""
        self.ectStm = ""
        self.sql={"columnStm":self.column, 
             "fromStm":self.fromStm, 
             "whereStm":self.whereStm,
             "orderbyStm":self.orderbyStm,
             "etcStm":self.etcStm}
        
        transportResult = self.dbh.runSql(self.sql)[0]
        tastingplace.bus = transportResult['bus'].split(",")
        tastingplace.subway = transportResult['subway'].split(",")
        
        return tastingplace;
        
        
        
    def getIdByFood(self, foodName):
    #음식이름에 해당하 spotId를 가져온다. 
    
        self.column = ["spot_id"];
        self.fromStm ="tb_spot_category"
        self.whereStm ="category_detail like  '%" + foodName +"%'"; 
        self.orderbyStm =""
        self.ectStm = ""
        self.sql={"columnStm":self.column, 
             "fromStm":self.fromStm, 
             "whereStm":self.whereStm,
             "orderbyStm":self.orderbyStm,
             "etcStm":self.etcStm}
        
        spotIdList = self.dbh.runSql(self.sql);
        return spotIdList; 
    
    
    
    
    def getPlaceByLocation(self, lat, lng):
        #주어진 위치에서 가장 가까운 순으로 가게 10개를 찾는다. 
         

        distance_sql = "SQRT(power((" + lat+" - latitude),2) + power(("+lng+"-longitude), 2)) as distance"

        
        self.column = ["tb_food_spot.id as id", "tb_food_spot.spot_id as spot_id", "name", "addr",distance_sql, "popular_menu"]
        self.fromStm ="tb_food_spot"
        self.orderbyStm ="distance asc limit 10"
        self.whereStm = ""
        self.ectStm = ""
        self.sql={"columnStm":self.column, 
             "fromStm":self.fromStm, 
             "whereStm":self.whereStm,
             "orderbyStm":self.orderbyStm,
             "etcStm":self.etcStm}
        
        
        foodSpotResultList = self.dbh.runSql(self.sql)
        tastingplaceList = []
        
        for foodSpotResult in foodSpotResultList:
            tastingplace = place();
            tastingplace.id = int(foodSpotResult["id"])
            tastingplace.spotId = int(foodSpotResult["spot_id"])
            tastingplace.name = foodSpotResult["name"]
            tastingplace.addr = foodSpotResult["addr"]
            tastingplace.popularmenu = foodSpotResult["popular_menu"] 
            tastingplaceList.append(tastingplace)
        
        return tastingplaceList;
    
         
    
    def getPlaceByFoodLocation(self, food, lat, lng):
        #주어진 음식에 관련된 가게중에서 가장 가까운 순으로 10개를 찾는다. 
        
 

        distance_sql = "SQRT(power((" + lat+" - latitude),2) + power(("+lng+"-longitude), 2)) as distance"

        
        self.column = ["tb_food_spot.id as id", "tb_food_spot.spot_id as spot_id", "name", "addr",distance_sql, "popular_menu"]
        self.fromStm ="tb_food_spot"
        self.whereStm ="tb_food_spot.spot_id in ( select tb_food_spot.spot_id from tb_food_spot, tb_spot_category"
        self.whereStm+=" where tb_food_spot.spot_id = tb_spot_category.spot_id and (tb_spot_category.category_detail like '"+food+"%' or tb_food_spot.detail like '%"+food+"%'))"
        self.orderbyStm=" distance asc limit 10"
        self.sql={"columnStm":self.column, 
             "fromStm":self.fromStm, 
             "whereStm":self.whereStm,
             "orderbyStm":self.orderbyStm,
             "etcStm":self.etcStm}
        
        
        foodSpotResultList = self.dbh.runSql(self.sql)
        tastingplaceList = []
        
        for foodSpotResult in foodSpotResultList:
            tastingplace = place();
            tastingplace.id = int(foodSpotResult["id"])
            tastingplace.spotId = int(foodSpotResult["spot_id"])
            tastingplace.name = foodSpotResult["name"]
            tastingplace.addr = foodSpotResult["addr"]  
            tastingplace.popularmenu = foodSpotResult["popular_menu"] 
            tastingplaceList.append(tastingplace)
        
        return tastingplaceList;
        
        pass  
    
    
    
    def getTastingPlaceListByFoodName(self, foodName):
        #음식이름으로 가게의 이름과 주소를 가져온다. 
        
        self.column = ["tb_food_spot.id as id", "tb_food_spot.spot_id as spot_id", "name", "addr", "popular_menu"]
        self.fromStm ="tb_food_spot, tb_spot_category"
        self.whereStm ="tb_food_spot.spot_id= tb_spot_category.spot_id and "
        self.whereStm += "(tb_spot_category.category_detail like '"+foodName+"%'"
        self.whereStm += " or tb_food_spot.detail like '%"+foodName+"%')"
        self.whereStm += " limit 10"
        
        self.orderbyStm =""
        self.ectStm = ""
        self.sql={"columnStm":self.column, 
             "fromStm":self.fromStm, 
             "whereStm":self.whereStm,
             "orderbyStm":self.orderbyStm,
             "etcStm":self.etcStm}
        
        
        foodSpotResultList = self.dbh.runSql(self.sql)
        tastingplaceList = []
        
        for foodSpotResult in foodSpotResultList:
            tastingplace = place();
            tastingplace.id = int(foodSpotResult["id"])
            tastingplace.spotId = int(foodSpotResult["spot_id"])
            tastingplace.name = foodSpotResult["name"]
            tastingplace.addr = foodSpotResult["addr"]  
            tastingplace.popularmenu = foodSpotResult["popular_menu"]
            tastingplaceList.append(tastingplace)
        
        return tastingplaceList;
        
        
    
    
    def getPlaceByFood(self, foodName):
    #음식이름에 해당하는 가게를 가져온다. 
        return self.getTastingPlaceListByFoodName(foodName); 

    def getPlaceByName(self, tpName): #가게이름으로 찾아라. 
        self.column = ["tb_food_spot.id as id", "tb_food_spot.spot_id as spot_id", "name", "addr", "popular_menu"]
        self.fromStm ="tb_food_spot"
        self.whereStm ="tb_food_spot.name like '"+tpName+"%'";
        self.orderbyStm =""
        self.ectStm = ""
        self.sql={"columnStm":self.column, 
             "fromStm":self.fromStm, 
             "whereStm":self.whereStm,
             "orderbyStm":self.orderbyStm,
             "etcStm":self.etcStm}
        
        
        foodSpotResultList = self.dbh.runSql(self.sql)
        tastingplaceList = []
        
        for foodSpotResult in foodSpotResultList:
            tastingplace = place();
            tastingplace.id = int(foodSpotResult["id"])
            tastingplace.spotId = int(foodSpotResult["spot_id"])
            tastingplace.name = foodSpotResult["name"]
            tastingplace.addr = foodSpotResult["addr"]  
            tastingplace.popularmenu = foodSpotResult["popular_menu"]
            tastingplaceList.append(tastingplace)
        
        return tastingplaceList;
        
             
if __name__ == '__main__':
    fd = foodspot_controller()
    fd.getTastingPlaceListByFoodName("생맥주")
        
        
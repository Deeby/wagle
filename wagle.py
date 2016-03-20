# -*- coding: utf-8 -*- 

import sys
import json
from topicnzin.engine.word_counter import WordCounter
reload(sys)
sys.setdefaultencoding("UTF-8")  # @UndefinedVariable

# flask
from flask import Flask, url_for  # @UnresolvedImport
from flask import render_template  # @UnresolvedImport
from flask import redirect, request  # @UnresolvedImport


# wagle
from db.foodspot_controller import *; 
from db.place import *; 
from API.openapicontroller import *; 
from common.textutils import *; 
from common.imgutils import *; 

# tornado
from tornado.wsgi import WSGIContainer  # @UnresolvedImport
from tornado.httpserver import HTTPServer  # @UnresolvedImport
from tornado.ioloop import IOLoop  # @UnresolvedImport



from API.wagle_topic import wagle_group, isFood, isLocal, isShop, wagle_token,\
	wagle_group_top_twitter
from API.friend_word import FriendWord
from topicnzin.common.utils import toUnicode, toStr
from API.daum_twitter import DaumTwitter

from data.Twitter import *; 




app = Flask(__name__)

tbFoodSpotController = foodspot_controller();
openApiController = OpenAPIController();

@app.route('/')
def home(): 
	return redirect(url_for('twitterui'))

@app.route('/food')
def food():
	
	keywordList = []
	for words in sorted( filter(lambda x: isFood(x[0]), wagle_group_top_twitter(500)) , key=lambda a : a[2], reverse=True):  # 음식만 필터링함.    
		word, word_cnt, doc_cnt = words
		
		if isFood(word) is True:
			keywordList.append(word)
 
	
	if len(keywordList) > 20:
		keywordList = keywordList[:20];
		
		
	foodImage = openApiController.getFoodImage(keywordList[:5])
	
	i = 0; 
	for foodImg in foodImage:
		foodImg.image = getBase64StringFromUrl(foodImg.image);
		foodImg.tag = keywordList[i]; 
		i += 1;  
		 
	return render_template("food.html",
						mainImg=foodImage[0],
						subImg1=foodImage[1],
						subImg2=foodImage[2],
						subImg3=foodImage[3],
						subImg4=foodImage[4],
						keywordList=keywordList);
						
						 
 
@app.route('/tplist/', methods=['POST', 'GET'])
def tplist():
	   
	  
	food = request.args.get(u"food")
	lat = request.args.get(u"lat")
	lng = request.args.get(u"lng") 
	tp = request.args.get(u"tp")
	
	
	title =""  
	realtedKeyword = None
	tastingplaceList = []
	relatedFoodList = None; 
	relatedShopList = None;
	isLocalData = False; 
	
	if food is not None and  lat is None and lng is None:#음식을 누른 경우
		realtedKeyword = food; 
		title= food+" 맛집";
		tastingplaceList.extend(tbFoodSpotController.getPlaceByFood(food))
		relatedFoodList = getFood2Food(food)
		relatedShopList = getFood2Shop(food)
	
	elif food is None and lat is not None and lng is not None:
		title= "근처 맛집";
		food = None
		
		tastingplaceList.extend(tbFoodSpotController.getPlaceByLocation(lat, lng))
	
	elif food is not None and lat is not None and lng is not None: #모두다 있는 경우
		realtedKeyword = food
		title= "근처 "+food+" 맛집";
		tastingplaceList.extend(tbFoodSpotController.getPlaceByFoodLocation(food, lat, lng))
		relatedFoodList = getFood2Food(food)
		relatedShopList = getFood2Shop(food) 
	
	elif tp is not None:
		realtedKeyword = tp 
		title = tp +" 지점"
		tastingplaceList.extend(tbFoodSpotController.getPlaceByName(tp))
		
		if len(tastingplaceList) == 0:
			tastingplaceList.extend(getLocalInfoList(tp))
			isLocalData = True; 
			
		
		relatedFoodList = getShop2Food(tp)
		relatedShopList = getShop2Shop(tp) 
		
		
	
	
	#GET image
	for i in range(0, len(tastingplaceList)):
		
		keyword = ""
		if isLocalData == False:
			keyword = extractDong(tastingplaceList[i].addr) + " " + removeText(tastingplaceList[i].name, "(", ")")
		else:
			keyword = tp 
			 
		tmpImageList = openApiController.getTastingPlaceImage(keyword, 1); 
		
		
		if len(tmpImageList)>0 and tmpImageList[0] is not None:
			tastingplaceList[i].thumbnailImage = getBase64StringFromUrl(tmpImageList[0].thumbnail);
			 
	
	if isLocalData is True:
		return render_template("local_list.html", 
						realtedKeyword=realtedKeyword, 
						tastingplaceList = tastingplaceList, 
						title = title, 
						relatedFoodList = relatedFoodList, 
						relatedShopList = relatedShopList)
		
		
	else:
		return render_template("tastingplace_list.html", 
						realtedKeyword=realtedKeyword, 
						tastingplaceList = tastingplaceList, 
						title = title, 
						relatedFoodList = relatedFoodList, 
						relatedShopList = relatedShopList)
	



def getLocalInfoList(tp):
	
	tastingplaceList = []
	resultDictList = openApiController.getLocalInfoList(tp)
	 
	for resultDict in resultDictList:
		tastingplace = place()
		tastingplace.name = (resultDict["name"]).strip()
		tastingplace.addr = resultDict["addr"].strip()
		tastingplace.detail = resultDict["detail"].strip()
		tastingplace.second_info = resultDict["second_info"].strip()
		tastingplace.latitude = resultDict["latitude"].strip()
		tastingplace.longitude = resultDict["longitude"].strip()
		tastingplace.tel = resultDict["tel"].strip()
		
		tastingplaceList.append(tastingplace)
	return tastingplaceList;



@app.route('/local/<kwd>')
def local(kwd):
	
	 
	
 	tastingplace = getLocalInfoList(kwd)[0]
 				
 	#트위터데이터 가져오기 
 	twitterList = getTwitterData(tastingplace.name)
 	
 	
 	#블로그데이터 가져오기 
 	tpBlog = openApiController.getBlogData(kwd, 5)
 	
 	#이미지 가져오기 
 	tpImgList = openApiController.getTastingPlaceImage(kwd, 1);
 	
 	#연관음식 가져오기
 	relatedFoodList = getShop2Food(tastingplace.name)
 	if len(relatedFoodList) == 0:
 		relatedFoodList = None; 
 	
 	#연관가게 가져오기 
 	relatedShopList = getShop2Shop(tastingplace.name)
 	if len(relatedShopList) == 0:
 		relatedShopList = None; 
 
 	
 	if len(tpImgList) == 0:
 		tpImg = None
 	else:
 		tpImg = tpImgList[0]
 		if tpImg.image is not None:
 			tastingplace.mainImage = getBase64StringFromUrl(tpImg.image);	

 	return render_template("local.html", 
 						tastingplace=tastingplace, 
 						tpBlog=None, 
 						twitterList = None,
 						relatedFoodList = None,
 						relatedShopList = None 
 						);
	
	

@app.route('/tastingplace/<id>')
def tastingplace(id):
	
	tastingplace = tbFoodSpotController.getPlaceById(str(id))
	keyword = extractDong(tastingplace.addr) + " " + removeText(tastingplace.name, "(", ")")
	
	
	#트위터데이터 가져오기 
	twitterList = getTwitterData(tastingplace.name)
	
	
	#블로그데이터 가져오기 
	tpBlog = openApiController.getBlogData(keyword, 5)
	
	#이미지 가져오기 
	tpImgList = openApiController.getTastingPlaceImage(keyword, 1);
	
	#연관음식 가져오기
	relatedFoodList = getShop2Food(tastingplace.name)
	if len(relatedFoodList) == 0:
		relatedFoodList = None; 
	
	#연관가게 가져오기 
	relatedShopList = getShop2Shop(tastingplace.name)
	if len(relatedShopList) == 0:
		relatedShopList = None; 
	
	
	
	if len(tpImgList) == 0:
		tpImg = None
	else:
		tpImg = tpImgList[0]
		if tpImg.image is not None:
			tastingplace.mainImage = getBase64StringFromUrl(tpImg.image);	
	
	return render_template("tastingplace.html", 
						tastingplace=tastingplace, 
						tpBlog=tpBlog, 
						twitterList = twitterList,
						relatedFoodList = relatedFoodList,
						relatedShopList = relatedShopList 
						);
						
				
	
	
def getFood2Shop(food):
	friendword = FriendWord()
	
	shopWordList = []
	for results in friendword.food2shop(toUnicode(food), 10):
		word, cnt = results
		shopWordList.append(word)
   
	return shopWordList
			
				
def getFood2Food(food):
	friendword = FriendWord()
	
	foodWordList = []
	for results in friendword.food2food(toUnicode(food), 10):
		word, cnt = results
		foodWordList.append(word)

	return foodWordList

		
def getShop2Food(shop):
	friendword = FriendWord()
	
	foodWordList = []
	for results in friendword.shop2food(toUnicode(shop), 10):
		word, cnt = results
		foodWordList.append(word)

	return foodWordList


def getShop2Shop(shop):
	friendword = FriendWord()
	
	shopWordList = []
	for results in friendword.shop2shop(toUnicode(shop), 10):
		word, cnt = results
		shopWordList.append(word)

	return shopWordList



def getTwitterData(keyword):
	twitterList = []
	 
	for row in  DaumTwitter.search(keyword, 10): # 10
		twit = Twitter()
		twit.date = row["pub_date"]
		twit.user_name = row["user_name"]
		twit.url = row["doc_url"]
		twit.thumbnail_image = row["thumbnail_image"]
		twit.content = row["text"]
		twitterList.append(twit)
		
	return twitterList;  



@app.route('/twitterui')
def twitterui():
	limit = 500
	seed_keyword = ["강추","추천","먹네","맛집","먹고","맛있","땡긴다", "먹을","먹자", "맛난", "마시고싶다","마시자", "음식" ,"요리", "폭풍흡입", "푸짐", "무한리필", "사줘", "냠냠","할인","주문","신메뉴"]
	

	twitterList = []
	for row  in DaumTwitter.searchs(seed_keyword, limit):
		twitterList.append(row)


	counter = WordCounter(True)
	filter_twitterList = []
	
	for twit in twitterList:
		find_num = 0
		find_words = []
		for item in wagle_group(twit["text"]):			
			word, word_cnt, doc_cnt = item
			counter.add(word)
			tagword = None
			if isFood(word):
				tagword = '@' + word
				find_num = find_num | 2
			elif isShop(word):
				tagword = '$' + word
				find_num = find_num | 4
			elif isLocal(word):
				tagword = '+' + word
				find_num = find_num | 1
			else:
				continue
			
			if tagword:
				find_words.append(tagword)
				
				
		counter.groupEnd()
# 	
# 			rankList.append((word, word_cnt, doc_cnt, tagword,))
			
		if find_num in [2,4,6,3,5]:
			twit["find_tags"] = ",".join(find_word for find_word in find_words)
			filter_twitterList.append(twit)

	rankList=[]  # 없는애는 걸러내기도 해야함.
	for key in counter.keys():
		word = key
		word_cnt, doc_cnt = counter.get(key)
		tagword = None
		if isFood(word):
			tagword = '@' + word
			find_num = find_num | 2
		elif isShop(word):
			tagword = '$' + word
			find_num = find_num | 4
		elif isLocal(word):
			tagword = '+' + word
			find_num = find_num | 1
		else:
			continue
			
		rankList.append( (key, word_cnt,doc_cnt, tagword,) )
		
		
	return render_template('twitterui.html',rankList=rankList, twitterList=filter_twitterList)


@app.route('/friend_word/<keyword>')
def friend_word(keyword):
	keyword = toUnicode(keyword)
	word = toUnicode(keyword[1:len(keyword)])
	result = None
	title = "없음"

	friend_word = FriendWord()
	head = ""
	if keyword.startswith("$"):             # shop=>food
		result = friend_word.shop2food(toUnicode(word),15)
		title = "'"+word+"' 와 같이 이야기된 음식"
		head = "@"        
	elif keyword.startswith("@"):       # food=>shop
		result = friend_word.food2shop(toUnicode(word),15)
		title = "'"+word+"' 의 음식과 많이 이야기된 가게"
		head = "$"
	elif keyword.startswith("+"):       # local=>shop
		result = friend_word.local2shop(toUnicode(word),15)
		title = "'"+word+"' 의 지역과 같이 이야기된  가게"
		head = "$"
	else:
		result = ["결과가없음"]
		head = ""
		
	result=[] if not result else result
	
	
	#트윗결과
	twitterList = []
	for row  in DaumTwitter.search(word, 20):
		twitterList.append(row)

	
	return render_template('friend_word.html', title=title,result=result, twitterList=twitterList, head=head,word=word)



@app.route('/test')
def test():
	return render_template('test.html')

@app.route("/goc/", methods = ["get"])
def goc(): 
	  
	keyword = request.args.get(u"keyword")
	lat = request.args.get(u"lat")
	lng = request.args.get(u"lng") 
	
	tastingplaceList = []
	resultDictList = openApiController.getLocalInfoList(keyword)
	 
	
	return render_template('goc.html', result = json.dumps(resultDictList));
	
if __name__ == "__main__": 
	http_server = HTTPServer(WSGIContainer(app))
	http_server.listen(9200) #port
	IOLoop.instance().start() 
	
#  	app.run(host="0.0.0.0", port=9200, debug=True)
	
	


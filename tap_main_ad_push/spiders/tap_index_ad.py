# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from tap_main_ad_push.items import TapMainAdPushItem
from pymongo import MongoClient
from bs4 import BeautifulSoup
import scrapy
import json
import requests
import redis
import time

class get_index_ad(Spider):
    name = "get_index_ad"
    start_urls = []
    print "爬虫1启动..."
    client = MongoClient('127.0.0.1', 27017)
    # 连接所需数据库, test为数据库名
    db = client.local

    def start_requests(self):
        while True:
            job_redis = redis.Redis(host="127.0.0.1", port="6379", db="8")
            yield scrapy.Request(url=job_redis.spop("detailUrl"), callback=self.parse)

    def save_data(self, data):
        client = MongoClient('127.0.0.1', 27017)
        # 连接所需数据库,test为数据库名
        db = client.local
        db_name_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        db_name_time = db_name_time.replace("-", "")
        db_name = "taptapGameIndexAd" + str(db_name_time)
        if len(list(db[db_name].find({"game_id": data["game_id"]}))) < 1:
            db[db_name].insert(data)
        else:
            show_times = list(db[db_name].find({"game_id": data["game_id"]}))[0]["show_times"]
            db[db_name].update({"game_id": data["game_id"]}, {"$set": {"show_times": int(show_times) + 1}})

    def get_ad_message(self, url):
        r = requests.get(url)
        if r.status_code == 200:
            result = json.loads(r.text)
            gameObjPush = {}
            gameObjPush["game_url"] = result["info"]["uri"]  # 游戏url
            gameObjPush["game_id"] = result["product"]  # 游戏id
            gameObjPush["game_name"] = result["info"]["title"]  # 游戏名称
            gameObjPush["game_icon"] = result["info"]["icon"]  # 游戏名称
            gameObjPush["time"] = time.time()
            gameObjPush["type"] = "ad"
            gameObjPush["show_times"] = 1
            self.save_data(gameObjPush)
        else:
            print "页面信息获取失败"
        print "3424:", gameObjPush


    def parse(self, response):
        bs = BeautifulSoup(response.text, 'html5lib')
        gameObjPush = {}
        gameObjPush["game_url"] = bs.select(".index-header .feed-rec-title")[0].get("href")  # 游戏id
        gameObjPush["game_id"] = gameObjPush["game_url"] .split("/")[-1]  # 游戏id
        gameObjPush["game_name"] = bs.select(".index-header .feed-rec-title h2")[0].text # 游戏名称
        gameObjPush["game_icon"] = bs.select(".index-header .feed-rec-image img")[0].get("data-src")  # 游戏名称
        gameObjPush["time"] = time.time()
        gameObjPush["type"] = "top"
        gameObjPush["show_times"] = 1
        self.save_data(gameObjPush)
        self.get_ad_message("https://sense.tapdb.com/api/v1/sales/retrieve?tapAdId=098d2c7b-9332-f092-41ea-9df55318d3ce&device=2&version=0.1.1")
        items = TapMainAdPushItem()
        items['name'] = gameObjPush
        return items


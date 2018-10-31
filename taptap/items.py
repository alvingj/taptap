# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaptapItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 应用名称
    appName = scrapy.Field()
    # 应用类型
    appType = scrapy.Field()
    # 应用标签
    appTags = scrapy.Field()
    # 应用评分
    appScore = scrapy.Field()
    # 应用iconUrl
    appIconUrl = scrapy.Field()
    # 应用下载次数
    appTimes = scrapy.Field()
    # 应用详情url
    appDetailUrl = scrapy.Field()
    # 应用appId
    appId = scrapy.Field()
    # 应用开发者Id
    appDeveloperId = scrapy.Field()
    # 应用开发者Id主页
    appDeveloperIdUrl = scrapy.Field()
    # 应用开发者名称
    appDeveloperName = scrapy.Field()
    # 应用包名
    appPackageName = scrapy.Field()
    # 应用更新时间
    appUpdateTime = scrapy.Field()

    # pass
# -*- coding: utf-8 -*-
import scrapy
import json

from lxml import etree

from taptap.items import TaptapItem


class TaptapsinglegameSpider(scrapy.Spider):
    name = 'tapTapSingleGame'
    allowed_domains = ['taptap.com']
    url = 'https://www.taptap.com/ajax/search/tags?&kw=%E5%8D%95%E6%9C%BA&sort=hits&page='
    offset = 1
    start_urls = [url + str(offset)]

    def parse(self, response):
        js = json.loads(response.body)
        data = js["data"]
        html = data["html"]
        selector = etree.HTML(str(html))
        for each in selector.xpath("//div[@class=\"taptap-app-card\"]"):
            # 初始化模型对象
            item = TaptapItem()
            # 详情url
            detailUrl = each.xpath("./a/@href")
            item['appDetailUrl'] = detailUrl[0]
            # 访问详情页
            yield scrapy.Request(item['appDetailUrl'], meta={'meta_1': item}, callback=self.parseAppDetail)
            # yield item
        if self.offset < 300:
            self.offset += 1
        # 每次处理完一页的数据之后，重新发送下一页页面请求
        # self.offset自增1，同时拼接为新的url，并调用回调函数self.parse处理Response
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

    def parseAppDetail(self, response):
        meta_1 = response.meta['meta_1']

        for each in response.xpath("/html/body/div[1]/div/div/section[1]"):
            item = TaptapItem()
            item['appDetailUrl'] = meta_1['appDetailUrl']
            # 应用appId
            item['appId'] = item['appDetailUrl'][27:]
            # 应用名称
            appNameList = each.xpath("/html/body/div[1]/div/div/section[1]/div[1]/div[2]/h1/text()").extract()[0]
            item['appName'] = appNameList.strip()
            # 开发者
            item['appDeveloperName'] = \
            each.xpath("/html/body/div[1]/div/div/section[1]/div[1]/div[2]/div[1]/a/span[2]/text()").extract()[0]
            # 应用开发者Id主页
            item['appDeveloperIdUrl'] = \
            each.xpath("/html/body/div[1]/div/div/section[1]/div[1]/div[2]/div[1]/a/@href").extract()[0]
            # 应用开发者Id
            item['appDeveloperId'] = item['appDeveloperIdUrl'][33:]

            # 应用评分
            # item['appScore'] = each.xpath("/html/body/div[1]/div/div/section[1]/div[1]/span/span/span")
            # 安装次数
            # item['appTimes'] = each.xpath("/html/body/div[1]/div/div/section[1]/div[1]/div[2]/div[2]/div[1]/p/span[1]/text()")
            # 发布时间
            # item['appUpdateTime'] = each.xpath("/html/body/div[1]/div/div/section[1]/div[2]/div[8]/ul/li[3]/span[2]")
            # 应用包名
            item['appPackageName'] = each.xpath(
                "/html/body/div[1]/div/div/section[1]/div[1]/div[2]/div[@class=\"header-text-download\"]/div[2]/div[1]/@data-app-identifier").extract()[
                0]
            yield item
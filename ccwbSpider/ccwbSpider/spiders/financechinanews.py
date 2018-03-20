# -*- coding: utf-8 -*-
import scrapy
import datetime
from scrapy.http import Request
from urllib import parse
from scrapy.exceptions import CloseSpider
from ccwbSpider.items import ArticleItem
from ccwbSpider.utils.common import get_md5

class FinancechinanewsSpider(scrapy.Spider):
    name = 'financechinanews'
    allowed_domains = ['finance.chinanews.com']
    start_urls = ['http://finance.chinanews.com/cj/gd.shtml']
    # start_urls = ['http://finance.chinanews.com/cj/2018/03-19/8471340.shtml']
    node_url = 'http://finance.chinanews.com'

    def parse(self, response):
        post_nodes = response.xpath('//*[@id="content_right"]/div/ul/li/div/a')
        # print(len(post_nodes))
        for post_node in post_nodes:
            post_url = self.node_url+post_node.css("::attr(href)").extract_first("")
            # print(post_url)
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail)
    # 文章详情
    def parse_detail(self, response):
        article_item = ArticleItem()
        article_item['title'] =  response.css(".content h1::text").extract()[0]
        add_time = response.css('div.left-t::text').extract()[0].strip().split("\u3000来源：")
        if add_time[1] != "":
            article_item['source_article'] = add_time[1]
        else:
            article_item['source_article'] = response.css('div.left-t a::text').extract()[0]
        article_item['content'] = response.css('div.left_zw').extract()[0]
        article_item['url'] = response.url
        article_item['type_article'] = 1
        article_item['url_object_id'] = get_md5(response.url)
        article_item['create_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        article_item['update_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        article_item['add_time'] = datetime.datetime.strptime(add_time[0], '%Y年%m月%d日 %H:%M').strftime('%Y-%m-%d %H:%M:%S')
        now_day = datetime.datetime.now().strftime('%d')        
        spider_day = datetime.datetime.strptime(add_time[0], '%Y年%m月%d日 %H:%M').strftime('%d')
        if now_day == spider_day:
        #     raise CloseSpider('enough')
            yield article_item
        else:
            pass
        

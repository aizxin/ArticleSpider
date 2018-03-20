# -*- coding: utf-8 -*-
import scrapy
import datetime
from scrapy.http import Request
from urllib import parse
from scrapy.exceptions import CloseSpider
from ccwbSpider.items import ArticleItem
from ccwbSpider.utils.common import get_md5

class FinanceSpider(scrapy.Spider):
    name = 'finance'
    allowed_domains = ['finance.ifeng.com']
    start_urls = ['http://finance.ifeng.com/listpage/1/marketlist.shtml']

    def parse(self, response):
        post_nodes = response.xpath('//*[@id="list01"]/li/div/div[2]/h2/a')
        for post_node in post_nodes:
            post_url = post_node.css("::attr(href)").extract_first("")
            # print(post_url)
            if self.name in post_url:
                yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail)
        next_url = response.xpath('//*[@id="pagenext"]/@href').extract_first("")
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)
    # 文章详情
    def parse_detail(self, response):
        article_item = ArticleItem()

        article_item['title'] = response.xpath('//*[@id="artical_topic"]/text()').extract_first("")
        article_item['add_time'] = response.xpath('//*[@id="artical_sth"]/p/span[1]/text()').extract_first("")
        source_article = response.css('#artical_sth .ss03::text').extract_first("")
        if  source_article == "":
            article_item['source_article'] = response.css('#artical_sth .ss03 a::text').extract_first("")
        else:
            article_item['source_article'] = source_article
        article_item['content'] = response.css("div.js_selection_area").extract()[0]
        article_item['url'] = response.url
        article_item['type_article'] = 1
        article_item['url_object_id'] = get_md5(response.url)
        article_item['create_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        article_item['update_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        now_day = datetime.datetime.now().strftime('%d')        
        spider_day = datetime.datetime.strptime(article_item['add_time'], '%Y-%m-%d %H:%M:%S').strftime('%d')
        if now_day == spider_day:
            yield article_item
        else:
            raise CloseSpider('enough')
            pass
        
        



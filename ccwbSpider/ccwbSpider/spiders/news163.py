# -*- coding: utf-8 -*-
import scrapy
import datetime
from scrapy.http import Request
from urllib import parse
from scrapy.exceptions import CloseSpider
from ccwbSpider.items import ArticleItem
from ccwbSpider.utils.common import get_md5


class News163Spider(scrapy.Spider):
    name = 'news163'
    allowed_domains = ['news.163.com',"temp.163.com"]
    start_urls = ['http://temp.163.com/special/00804KVA/cm_shehui.js?callback=data_callback']
    # start_urls = ['http://news.163.com/18/0320/16/DDBU0LBA0001875P.html']
    def parse(self, response):
        post_nodes = response.body_as_unicode()
        print(post_nodes)
        # for post_node in post_nodes:
            # post_url = post_node.css("::attr(href)").extract_first("")

    def parse_info(self, response):
        article_item = ArticleItem()

        article_item['title'] = response.css('#epContentLeft h1::text').extract_first("")
        article_item['add_time'] = response.css('.post_time_source::text').extract_first("").replace("来源:",'').strip()
        article_item['source_article'] = response.css(".post_time_source a::text").extract_first("")
        article_item['content'] = response.css('#endText').extract()[0]
        article_item['url'] = response.url
        article_item['type_article'] = 2
        article_item['url_object_id'] = get_md5(response.url)
        article_item['create_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        article_item['update_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        now_day = datetime.datetime.now().strftime('%d')        
        spider_day =datetime.datetime.strptime(article_item['add_time'].strip(), '%Y-%m-%d %H:%M:%S').strftime('%d')
        # print(article_item)
        if now_day == spider_day:
            yield article_item
        else:
            pass

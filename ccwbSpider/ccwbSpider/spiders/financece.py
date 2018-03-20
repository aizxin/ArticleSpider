# -*- coding: utf-8 -*-
import scrapy
import datetime
from scrapy.http import Request
from urllib import parse
from scrapy.exceptions import CloseSpider
from ccwbSpider.items import ArticleItem
from ccwbSpider.utils.common import get_md5


class FinanceceSpider(scrapy.Spider):
    name = 'financece'
    allowed_domains = ['finance.ce.cn']
    start_urls = ['http://finance.ce.cn/rolling']
    node_url = 'http://finance.ce.cn/rolling'
    def parse(self, response):
        post_nodes = response.css('.list_left .font14 a')
        for post_node in post_nodes:
            post_url = self.node_url+post_node.css("::attr(href)").extract_first("").replace('./','/')
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail)
    # 文章详情
    def parse_detail(self, response):
        article_item = ArticleItem()

        article_item['title'] = response.xpath('//*[@id="articleTitle"]/text()').extract_first("")
        add_time = response.xpath('//*[@id="articleTime"]/text()').extract_first("")
        article_item['add_time'] = datetime.datetime.strptime(add_time.strip(), '%Y年%m月%d日 %H:%M').strftime('%Y-%m-%d %H:%M:%S')
        article_item['source_article'] = response.css("#articleSource::text").extract_first("").replace("来源：",'').strip()
        article_item['content'] = response.xpath('//*[@id="articleText"]').extract()[0]
        article_item['url'] = response.url
        article_item['type_article'] = 1
        article_item['url_object_id'] = get_md5(response.url)
        article_item['create_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        article_item['update_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        now_day = datetime.datetime.now().strftime('%d')        
        spider_day =datetime.datetime.strptime(add_time.strip(), '%Y年%m月%d日 %H:%M').strftime('%d')
        # print(article_item['source_article'].replace(' ',''))
        if now_day == spider_day:
            yield article_item
        else:
            pass

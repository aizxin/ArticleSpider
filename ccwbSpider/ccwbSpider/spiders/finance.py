# -*- coding: utf-8 -*-
import scrapy
import datetime
from scrapy.http import Request
from urllib import parse
from scrapy.exceptions import CloseSpider

class FinanceSpider(scrapy.Spider):
    name = 'finance'
    allowed_domains = ['finance.ifeng.com']
    start_urls = ['http://finance.ifeng.com/listpage/1/marketlist.shtml']

    def parse(self, response):
        post_nodes = response.xpath('//*[@id="list01"]/li/div/div[2]/h2/a')
        for post_node in post_nodes:
            post_url = post_node.css("::attr(href)").extract_first("")
            if self.name in post_url:
                yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail)
        next_url = response.xpath('//*[@id="pagenext"]/@href').extract_first("")
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)
    def parse_detail(self, response):
        title = response.xpath('//*[@id="artical_topic"]/text()').extract_first("")
        add_time = response.xpath('//*[@id="artical_sth"]/p/span[1]/text()').extract_first("")
        content_from = response.xpath('//*[@id="artical_sth"]/p/span[3]/span/a/text()').extract_first("")
        content = response.xpath('//*[@id="main_content"]').extract()[0]
        url = response.url
        now_day = datetime.datetime.now().strftime('%d')
        spider_day = datetime.datetime.strptime(add_time, '%Y-%m-%d %H:%M:%S').strftime('%d')
        if now_day != spider_day:
            raise CloseSpider('enough')



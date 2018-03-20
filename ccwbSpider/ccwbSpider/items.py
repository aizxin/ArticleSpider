# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CcwbspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ArticleItem(scrapy.Item):
    title = scrapy.Field() # 文章标题
    add_time = scrapy.Field() # 文章发布时间
    url = scrapy.Field() # 文章的原地址
    url_object_id = scrapy.Field() # 文章的id
    content = scrapy.Field() # 文章的内容
    create_time = scrapy.Field() # 文章抓取时间
    source_article = scrapy.Field() # 文章来源
    type_article = scrapy.Field() # 文章分类1:经济，2:新闻，3：体育

    def get_insert_sql(self):
        insert_sql = """
            insert into ccwb_article(title, url, url_object_id,add_time,content,create_time,source_article,type_article)
            VALUES (%s, %s, %s,%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE create_time=VALUES(create_time),content=VALUES(content)
        """
        params = (
            self["title"],
            self["url"],
            self["url_object_id"],
            self["add_time"],
            self["content"],
            self["create_time"],
            self["source_article"],
            self["type_article"],
        )
        return insert_sql, params
# -*- coding: utf-8 -*-

from scrapy.cmdline import execute

import sys
import os 

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(['scrapy','crawl','financece']) #中国经济网（财经滚动新闻）
# execute(['scrapy','crawl','finance']) #凤凰网财经,财经
# execute(['scrapy','crawl','financechinanews']) #中国新闻网,财经
execute(['scrapy','crawl','news163']) #网易新闻（社会新闻）
# execute(['scrapy','crawlall'])

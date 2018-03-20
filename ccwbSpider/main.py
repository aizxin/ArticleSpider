# -*- coding: utf-8 -*-

import time
import os

while True:
    os.system("python3 -m scrapy crawlall")
    time.sleep(60)  #每隔一天运行一次 24*60*60=86400s
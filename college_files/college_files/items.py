# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FileToDown(scrapy.Item):
    # define the fields for your item here like:
    # files = scrapy.Field()
     files_urls = scrapy.Field()
    # local_dir = scrapy.Field()


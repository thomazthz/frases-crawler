# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FrasesItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    autor = scrapy.Field()
    frase = scrapy.Field()
    fb_share = scrapy.Field()
    fav_count = scrapy.Field()
    is_fav = scrapy.Field()


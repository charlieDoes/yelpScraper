# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class YelpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    businessName = scrapy.Field()
    yelpLink = scrapy.Field()
    rating = scrapy.Field()
    highlightReview1 = scrapy.Field()
    highlightReview2 = scrapy.Field()
    highlightReview3 = scrapy.Field()
    priceRange = scrapy.Field()
    website = scrapy.Field()
    address = scrapy.Field()
    phoneNumber = scrapy.Field()
    totalRatingCount = scrapy.Field()
    businessType = scrapy.Field()
    businessMenu = scrapy.Field()

    monday = scrapy.Field()
    tuesday = scrapy.Field()
    wednesday = scrapy.Field()
    thursday = scrapy.Field()
    friday = scrapy.Field()


class TestItem(scrapy.Item):
    openingHours = scrapy.Field()

    monday = scrapy.Field()
    tuesday = scrapy.Field()
    wednesday = scrapy.Field()
    thursday = scrapy.Field()
    friday = scrapy.Field()

    address = scrapy.Field()

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from yelpSpider.items import *

class YelpPipeline(object):
    def process_item(self, item, spider):

        #So item['element'] is actually a list, not a single variable like a string or int
        #Therefore if you have only one element in each item, you need to process the first
        #element, so item['element'][0]

        item['phoneNumber'][0] = item['phoneNumber'][0].strip()

        #strip removes the \n, or newlines.  Really nice.
        #scrapy will sometimes complain that item['element'][0] doesn't exist when it
        #obviously has.  That's because some yelp entries lack that element, so scrapy
        #pulls a null value

        item['highlightReview1'][0] = item['highlightReview1'][0].strip()
        item['highlightReview2'][0] = item['highlightReview2'][0].strip()
        item['highlightReview3'][0] = item['highlightReview3'][0].strip()

        item['businessName'][0] = item['businessName'][0].strip()


        return item

import scrapy
from scrapy.spiders import CrawlSpider, Rule

from urlparse import urljoin
from scrapy.http import Request

from yelpSpider.items import YelpItem
#scrapy.Spider

class Yelp1Spider(scrapy.Spider):
    name = "yelpSF"
    allowed_domains = ["yelp.com"]
    start_urls = [
    'http://www.yelp.com/search?find_desc=restaurants&find_loc=San+Francisco,+CA&start=0',

    ]

    #Generates all url directions to be sifted
    #for i in range(1,100):
    #    start_urls.append('http://www.yelp.com/search?find_desc=restaurants&find_loc=San+Francisco,+CA&start='+str(i * 10))


    def start_requests(self):
        #Ensures scrapy processess all files in order by assigning each link a priority number
        for priorityNumber, url in enumerate(self.start_urls):
            yield Request(url, priority = priorityNumber)


    def parse(self, response):
        #Processes all links found in yelp entries
        for href in response.xpath('//a[contains(@class, "biz-name") and contains(@class, "js-analytics-click")]/@href'):
            url = urljoin('http://www.yelp.com', href.extract())
            #Priority number is assigned to each extracted link so yelp processes each entry in order
            for x in range(1,11):
                yield scrapy.Request(url, callback=self.parse_dir_contents, priority=x)


    def parse_dir_contents(self, response):
        #Where all the main extraction occurs.  This code was formed by looking at how Yelp is constructed
        item = YelpItem()


        for businessHours in response.xpath("//table[contains(@class,'table') and contains(@class,'table-simple') and contains(@class,'hours-table')]/tbody"):
            item['monday'] = businessHours.xpath('(tr/td/span)[1]/text()').extract() + businessHours.xpath('(tr/td/span)[2]/text()').extract()
            item['tuesday'] = businessHours.xpath('(tr/td/span)[3]/text()').extract() + businessHours.xpath('(tr/td/span)[4]/text()').extract()
            item['wednesday'] = businessHours.xpath('(tr/td/span)[5]/text()').extract() + businessHours.xpath('(tr/td/span)[6]/text()').extract()
            item['thursday'] = businessHours.xpath('(tr/td/span)[7]/text()').extract() + businessHours.xpath('(tr/td/span)[8]/text()').extract()
            item['friday'] = businessHours.xpath('(tr/td/span)[9]/text()').extract() + businessHours.xpath('(tr/td/span)[10]/text()').extract()

        for address in response.xpath("//strong[@class='street-address']/address"):
            item['address'] = address.xpath("span/text()").extract()

        item['businessName'] = response.xpath('//h1[@itemprop="name"]/text()').extract()
        item['businessType'] = response.xpath("//span[@class='category-str-list']/a/text()").extract()

        item['totalRatingCount'] = response.xpath('//span[@itemprop="reviewCount"]/text()').extract()
        item['rating'] = response.xpath("(//div[@class='rating-very-large'])[1]/i/@title").extract()
        item['yelpLink'] = response.url

        item['highlightReview3'] = response.xpath("(//p[@class='quote'])[3]/text()").extract()
        item['highlightReview2'] = response.xpath("(//p[@class='quote'])[2]/text()").extract()
        item['highlightReview1'] = response.xpath("(//p[@class='quote'])[1]/text()").extract()

        item['businessMenu'] = response.xpath("//a[@class='external-menu']/@href").extract()
        item['priceRange'] = response.xpath("(//span[contains(@itemprop, 'priceRange')])/text()").extract()

        item['phoneNumber'] = response.xpath("//span[@class='biz-phone']/text()").extract()
        item['website'] = response.xpath("//div[@class='biz-website']/a/text()").extract()


        yield item

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TravelspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class LowpriceItem(scrapy.Item):
    cityName = scrapy.Field()
    airportName = scrapy.Field()
    arrCityCode = scrapy.Field()
    price = scrapy.Field()
    
class AllUsefulInfoItem(scrapy.Item):
    cityID = scrapy.Field()
    tid = scrapy.Field()
    answers = scrapy.Field()

class AllViewsetItem(scrapy.Item):
    cityID = scrapy.Field()
    viewsetName = scrapy.Field()

class AllHotelItem(scrapy.Item):
    cityID = scrapy.Field()
    hotelName = scrapy.Field()
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class RottenCrawlSpider(CrawlSpider):
    name = 'rotten_crawl'
    allowed_domains = ['rottentomatoes.com']
    start_urls = ['https://www.rottentomatoes.com/browse/in-theaters/']

    rules = (
        Rule(LinkExtractor(allow=r'/m/\w'),
             callback='parse_item',
             follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()

        item['ROT_movieName'] = response.xpath(
            '//*[@id="topSection"]/div[2]/div[1]/h1/text()'
        ).get()

        item['ROT_Cscore'] = response.xpath(
            '//*[@id="tomato_meter_link"]/span[2]/text()'
        ).get()

        item['ROT_Uscore'] = response.xpath(
            '//*[@id="topSection"]/div[2]/div[1]/section/section/div[2]/h2/a/span[2]/text()'
        ).get()
        return item
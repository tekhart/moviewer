# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MovieCrawlSpider(CrawlSpider):
    name = 'meta_crawl'
    allowed_domains = ['rottentomato.com']
    start_urls = ['https://www.metacritic.com/browse/movies/release-date/theaters/date?page=0']

    rules = (
        Rule(LinkExtractor(allow=r'/movie/\w'),
             callback='parse_item',
             follow=True),
    )

    def parse_item(self, response):
        iq= {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()

        iq['META_movieName'] = response.xpath(
            '//*[@id="main_content"]/div[1]/div[1]/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div/div/div[1]/div/h1/text()'
        ).extract()
        #
        # iq['META_Cscore'] = response.xpath(
        #     '//*[@id="nav_to_metascore"]/div[1]/div[2]/div[1]/a/div/text()'
        # ).extract()
        #
        # iq['META_Uscore'] = response.xpath(
        #     '//*[@id="nav_to_metascore"]/div[2]/div[2]/div[1]/a/div/text()'
        # ).extract()
        #
        # iq['META_poster'] = response.xpath(
        #     '//*[@id="main_content"]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/img/text()'
        # ).extract()
        #
        # iq['META_genre'] = response.xpath(
        #     '//*[@id="main_content"]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[5]/div[2]/span[2]/span/text()'
        # ).extract()
        #
        # iq['META_rate'] = response.xpath(
        #     '//*[@id="main_content"]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[5]/div[3]/span[2]/text()'
        # ).extract()
        #
        # iq['META_release'] = response.xpath(
        #     '//*[@id="main_content"]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[2]/table/tbody/tr/td/span[2]/span[2]/text()'
        # ).extract()
        #
        # iq['META_director'] = response.xpath(
        #     '//*[@id="main_content"]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[5]/div[1]/a/span/text()'
        # ).extract()
        #
        # iq['META_starring'] = response.xpath(
        #     '//*[@id="main_content"]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[3]/span[2]/text()'
        # ).extract()
        #
        # iq['META_synopsis'] = response.xpath(
        #     '//*[@id="summary_blurb_550205"]/span[2]/text()'
        # ).extract()
        return iq

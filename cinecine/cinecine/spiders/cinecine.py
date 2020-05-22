# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CinecineSpider(CrawlSpider):
    name = 'cinecine'
    allowed_domains = ['cine21.com']
    start_urls = ['http://cine21.com/']


    rules = (
        Rule(LinkExtractor(allow=r'cine21\.com/movie/info/\?movie\_id=\.*'),
             callback='parse_item', follow=True),
        #Rule(LinkExtractor(allow=r'cine21\.com/movie/point/recent'),
        #     callback='parse_item', follow=True),
    )



    def parse_item(self, response):
        q = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()

        # 포스터
        q['movie_poster'] = response.xpath(
            '//*[@id="container"]/div[2]/div/div/div[1]/img/@src').extract()

        # 제목
        q['movie_title'] = response.xpath(
            '//*[@id="container"]/div[2]/div/div/div[3]/p[1]/text()').extract()

        # 개봉일
        q['movie_date'] = response.xpath(
            '//*[@id="container"]/div[2]/div/div/div[3]/p[5]/span[1]/text()').extract()

        # 관객수
        q['movie_audience'] = response.xpath(
            '//*[@id="container"]/div[2]/div/div/div[3]/p[5]/span[2]/text()').extract()

        # 줄거리
        q['movie_story'] = response.xpath(
            '//*[@id="content"]/div[1]/div/text()').extract()

        # 리뷰
        q['movie_review'] = response.xpath(
            '//*[@id="content"]/div[5]/div[1]/div[3]/a/span[3]/text()').extract()

        # 감독
        q['movie_director'] = response.xpath(
            '//*[@id="container"]/div[2]/div/div/div[3]/p[6]/text()').extract()

        # 배우
        q['movie_actor'] = response.xpath(
            '//*[@id="actor_area"]/ul[2]/li[*]/p[1]/a/text()').extract()

        # 씨네별점
        q['movie_cine'] = response.xpath(
            '//*[@id="container"]/div[2]/div/div/ul/li[1]/span/text()').extract()

        # 네티즌별점
        q['movie_netizens'] = response.xpath(
            '//*[@id="container"]/div[2]/div/div/ul/li[2]/span/text()').extract()

        return q


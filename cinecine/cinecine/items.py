# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    class MovieItem(scrapy.Item):

        movie_poster=scrapy.Field()
        movie_title=scrapy.Field()
        movie_date=scrapy.Field()
        movie_audience=scrapy.Field()
        movie_story=scrapy.Field()
        movie_review=scrapy.Field()
        movie_director=scrapy.Field()
        movie_actor=scrapy.Field()
        movie_cine=scrapy.Field()
        movie_netizens=scrapy.Field()

        pass


class NaverItem(scrapy.Item):
    class NaverItem(scrapy.Item):

        naver_memo=scrapy.Field()
        naver_male=scrapy.Field()
        naver_female=scrapy.Field()

        pass

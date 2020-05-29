# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviewerItem(scrapy.Item):
    # define the fields for your item here like:

    #MetaMV_info

    #영화 제목
    ROT_movieName = scrapy.Field()

    #메타평론평점
    ROT_Cscore = scrapy.Field()

    #메타유저평점
    ROT_Uscore = scrapy.Field()

    # #포스터
    # META_poster = scrapy.Field()
    #
    # #장르
    # META_genre = scrapy.Field()
    #
    # #관람가
    # META_rate = scrapy.Field()
    #
    # #개봉일
    # META_release = scrapy.Field()
    #
    # #감독
    # META_director= scrapy.Field()
    #
    # #주연배우
    # META_starring= scrapy.Field()
    #
    # #줄거리
    # META_synopsis = scrapy.Field()

    pass

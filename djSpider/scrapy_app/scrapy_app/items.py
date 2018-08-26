# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyAppItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    unique_id = scrapy.Field()
    data = scrapy.Field()
    date = scrapy.Field()


class StoreItem(scrapy.Item):
    store_name = scrapy.Field()
    store_rating = scrapy.Field()
    store_review_total = scrapy.Field()


class StoreReviewItem(scrapy.Item):
    store_name = scrapy.Field()
    author_name = scrapy.Field()
    author_profile_url = scrapy.Field()
    review_content = scrapy.Field()
    comment_date = scrapy.Field()
    product_image_url = scrapy.Field()
    product_title = scrapy.Field()
    product_rating = scrapy.Field()


class StoreProductDetailItem(scrapy.Item):
    store_name = scrapy.Field()
    product_title = scrapy.Field()
    ask_a_question_url = scrapy.Field()
    over_view = scrapy.Field()
    review_count = scrapy.Field()
    favorited_count = scrapy.Field()
    favorite_url = scrapy.Field()
    description = scrapy.Field()

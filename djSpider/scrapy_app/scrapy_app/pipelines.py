# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyAppPipeline(object):
    def process_item(self, item, spider):
        return item


class StorePipeline(object):
    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def from_settings(cls, settings):
        pass

    def process_item(self, item, spider):
        return item

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass


class StoreReviewPipeline(object):
    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def from_settings(cls, settings):
        pass

    def process_item(self, item, spider):
        pass

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass


class StoreProductDetailPipeline(object):
    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def from_settings(cls, settings):
        pass

    def process_item(self, item, spider):
        pass

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass


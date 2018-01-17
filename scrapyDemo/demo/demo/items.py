# -*- coding: utf-8 -*-

# item 是保存爬取到的数据的容器；其使用方法和python字典类似。
# 虽然您也可以在Scrapy中直接使用dict，但是 Item 提供了额外保护机制来避免拼写错误导致的未定义字段错误。

import scrapy


class DemoItem(scrapy.Item):
    title=scrapy.Field()
    link=scrapy.Field()
    desc=scrapy.Field()

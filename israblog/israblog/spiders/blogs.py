import re

from scrapy import log
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.settings import Settings


class IsrablogSpider(CrawlSpider):
    name = 'israblog'
    allowed_domains = ['israblog.nana10.co.il']
    rules = (
        Rule(SgmlLinkExtractor(allow=[r'blogread\.asp']), callback='parse_blog', follow=True),
        Rule(SgmlLinkExtractor(allow=['/Category/\d+/.*',]), follow=True),
    )
    start_urls = [
        'http://israblog.nana10.co.il/',
        'http://israblog.nana10.co.il/lastblogs.aspx',
        'http://israblog.nana10.co.il/activeblogs.aspx',
        'http://israblog.nana10.co.il/Categories',
    ]

    def parse_blog(self, response):
        with open(response.url.split('/')[-1], 'wb') as f:
            f.write(response.body)


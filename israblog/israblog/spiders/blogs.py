import re

from datetime import datetime
from scrapy import log
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


class IsrablogSpider(CrawlSpider):
    name = 'israblog'
    allowed_domains = ['israblog.nana10.co.il']
    rules = (
        Rule(SgmlLinkExtractor(allow=['blogread.asp?blog=\d+(&year=\d+&month=\d+)?']), callback='parse_blog'),
        Rule(SgmlLinkExtractor(allow=['/Category/\d+/.*',]), follow=True),
    )
    start_urls = [
        'http://israblog.nana10.co.il/',
        'http://israblog.nana10.co.il/lastblogs.aspx',
        'http://israblog.nana10.co.il/activeblogs.aspx',
        'http://israblog.nana10.co.il/Categories',
    ]

    def parse_start_url(self, response):
        yield self.parse_blog(response)

    def parse_blog(self, response):
        self.log(response.url)
        match = re.match(r'/blogread.asp\?blog=(\d+)(?:&year=(\d+)&month=(\d+))?', response.url)
        if match:
            blog, year, month = match.groups()
            if not year and not month:
                now = datetime.now()
                year = now.year()
                month = now.month()
            self.log(blog, year, month)
        return None

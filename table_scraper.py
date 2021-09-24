#!/usr/bin/env python3
import scrapy
from table import Table

# requires table definition - see table.py

class TableSpider(scrapy.Spider):

    name = "table-scraper"

    start_urls = [
        'https://support.google.com/chrome/answer/157179?hl=en&co=GENIE.Platform%3DDesktop#zippy=%2Ctab-and-window-shortcuts%2Cgoogle-chrome-feature-shortcuts%2Caddress-bar-shortcuts%2Cwebpage-shortcuts%2Cmouse-shortcuts'
    ]

    def parse(self, response):
        table = Table(response.xpath('(//table)[1]'))
        # yield all rows
        yield from table.as_dicts()
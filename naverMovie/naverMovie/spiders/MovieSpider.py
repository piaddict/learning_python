import scrapy
from scrapy import Selector, item

from ..items import NavermovieItem

class MovieSpider(scrapy.Spider):
    name = "naverMovie"
    allowed_domains = ["http://movie.naver.com"]
    start_urls = [
        "http://movie.naver.com/movie/running/current.nhn"
    ]

    def parse(self, response):
        hxs = Selector(response)
        selects = hxs.xpath("// *[ @ id = 'content'] / div[1] / div[1] / div[3] / ul // li")
        items = list()
        for sel in selects:
            item = NavermovieItem()
            item["thumb"] = sel.xpath("div[@class='thumb']/a/img/@src").extract()
            item["title"] = sel.xpath("dl/dt/a/text()").extract()
            # item["genre"]
            # item["director"]
            # item["actors"]
            items.append(item)
        return items

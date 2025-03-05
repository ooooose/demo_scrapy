import scrapy


class BleagueMatchSpider(scrapy.Spider):
    name = "bleague-match"
    allowed_domains = ["www.bleague.jp"]
    start_urls = ["https://www.bleague.jp"]

    def parse(self, response):
        pass

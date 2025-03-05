import scrapy


class BleagueMatchSpider(scrapy.Spider):
    name = "bleague-match"
    allowed_domains = ["www.bleague.jp"]
    start_urls = ["https://www.bleague.jp"]

    def parse(self, response):
        links = response.xpath("//a")

        cnt = 0
        i = 0
        while cnt < 2:
            url = links[i].attrib["href"]
            if any(map(lambda d: d in url, self.allowed_domains)):
                cnt += 1
                yield response.follow(url, self.get_title)
            i += 1

    def get_title(self, response):
        title = response.xpath("//title/text()").get()
        yield dict(title=title)

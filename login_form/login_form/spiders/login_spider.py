import scrapy
from scrapy_playwright.page import PageMethod

class LoginSpider(scrapy.Spider):
    name = "login_spider"
    start_urls = ["xxx"]

    def start_requests(self):
        yield scrapy.Request(
            url=self.start_urls[0],
            meta={"playwright": True, "playwright_page_methods": [
                PageMethod("wait_for_selector", "input[type=email]"),
                PageMethod("fill", "input[type=email]", "xxx"),
                PageMethod("fill", "input[type=password]", "xxx"),
                PageMethod("click", "button[type=submit]"),
                PageMethod("wait_for_navigation")
            ]},
            callback=self.after_login
        )

    def after_login(self, response):
        yield {"title": response.xpath("//title/text()").get()}

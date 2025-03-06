import scrapy


class LoginSpider(scrapy.Spider):
  name = 'login_spider'
  start_urls = [""]

  def parse(self, response):
    return scrapy.FormRequest.from_response(
      response,
      formdata={'email': '', 'password': ''},
      callback=self.after_login
    )
  
  def after_login(self, response):
    if "ログインに失敗しました。" in response.text:
      self.logger.error("Login failed")
      return

    return response.follow("/dashboard")

  def parse_dashboard(self, response):
    title = response.xpath("//title/text()").get()
    yield {"title": title}
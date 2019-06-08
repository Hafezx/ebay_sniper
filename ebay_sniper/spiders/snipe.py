import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from scrapy.spiders import BaseSpider
from scrapy.http import FormRequest
from loginform import fill_login_form


class ElementSpider(scrapy.Spider):
    name = 'ebay11'
    start_urls = ['https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&ru=https%3A%2F%2Fwww.ebay.com%2F']

    def __init__(self, *args, **kwargs):
        super(ElementSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        return [FormRequest.from_response(response,
                                          formdata={'login': 'hafez.damanpak@gmail.com', 'password': '123qwe123'},
                                          callback=self.after_login)]

    def after_login(self, response):

        if "Incorrect username or password" in response.body:
            print
            "heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
            self.log("Login failed", level=Log.Error)
            return

        else:
            return Request(url="https://www.ebay.com",
                           callback=self.parse_data)

    def parse_data(self, response):
        haf = response.css('div.hl-cat-nav').get()
        print(haf)
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

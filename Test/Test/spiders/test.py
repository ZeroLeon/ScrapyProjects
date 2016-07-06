import scrapy

from Test.items import TestItem


class TestSpider(scrapy.Spider):

    name = "Test"
    allowed_domains = ["http://www.sda.gov.cn/"]
    start_urls = ["http://www.sda.gov.cn/WS01/CL1029/"]

    def parse(self,response):
        item = TestItem()
        item['link'] = response.xpath('//body/table[3]/tbody/tr/td[3]/table[@class="tabsHoverCon"][1]/tbody/tr/td/table/tbody/tr/td[@class="ListColumnClass2"]/a/@href').extract()
        item['desc'] = response.xpath('//body/table[3]/tbody/tr/td[3]/table[@class="tabsHoverCon"][1]/tbody/tr/td/table/tbody/tr/td[@class="ListColumnClass2"]/a//text()').extract()
        yield item
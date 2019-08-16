# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem


class TencentzpSpider(scrapy.Spider):
    name = 'tencentZP'
    allowed_domains = ['wz.sun0769.com']
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath('//td[@align="center"]//tr'):
            print(each)
            item = TencentItem()
            item["title"] = each.xpath('.//a[2]/text()').extract()[0]
            item["place"] = each.xpath('.//a[3]/text()').extract()[0]
            item["state"] = each.xpath('.//span/text()').extract()[0]
            item["name"] = each.xpath('.//td[@class="t12h"][2]/text()').extract()[0]
            item["time"] = each.xpath('.//td[@class="t12wh"]/text()').extract()[0]
            item["link"] = each.xpath('.//a[2]/@href').extract()[0]
            yield item
        if self.offset < 570:
            self.offset += 30
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)


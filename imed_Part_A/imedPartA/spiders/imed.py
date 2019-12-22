# -*- coding: utf-8 -*-
import scrapy


class ImedSpider(scrapy.Spider):
    name = 'imed'
    allowed_domains = ['report.imed.ir']
    allowed_domains = ['report.imed.ir']
    with open("urls.txt", "rt") as f:
        start_urls = [url.strip() for url in f.readlines()]

    def parse(self, response):
        yield {
            'Col_1_P':response.xpath('//form[@name="aspnetForm"]/div[1]/fieldset[1]/table/tr[1]/td[4]/span/text()').get(),
            'Col_1_G':response.xpath('//form[@name="aspnetForm"]/div[1]/fieldset[1]/table/tr[4]/td[2]/span/text()').get(),
            'Col_1_I':response.xpath('//form[@name="aspnetForm"]/div[1]/fieldset[2]/table/tr[1]/td[4]/span/text()').get(),
            'Col_1_H':response.xpath('//form[@name="aspnetForm"]/div[1]/fieldset[1]/table/tr[6]/td[2]/span/text()').get(),
            'Col_1_K':response.xpath('//form[@name="aspnetForm"]/div[1]/fieldset[2]/table/tr[1]/td[2]/span/text()').get(),
            'Col_1_J':response.xpath('//form[@name="aspnetForm"]/div[1]/fieldset[2]/table/tr[2]/td[2]/span/text()').get(),
            'Col_1_N':response.xpath('//form[@name="aspnetForm"]/div[1]/fieldset[2]/table/tr[3]/td[4]/span/text()').get(),
            'Col_1_L':response.xpath('//form[@name="aspnetForm"]/div[1]/fieldset[2]/table/tr[3]/td[2]/span/text()').get(),
            'Col_1_O':response.xpath('//form[@name="aspnetForm"]/div[1]/fieldset[2]/table/tr[4]/td[4]/span/text()').get(),
            'Col_1_M':response.xpath('//form[@name="aspnetForm"]/div[1]/fieldset[2]/table/tr[5]/td[2]/span/text()').get(),
            }
import scrapy 
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from imed.spiders.captcha import CaptchaSpider

process = CrawlerProcess(settings=get_project_settings())
process.crawl(CaptchaSpider)
process.start()
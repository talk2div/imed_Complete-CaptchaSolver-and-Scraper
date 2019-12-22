# -*- coding: utf-8 -*-
import io                                                                       
import urllib.request                                                         
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector
from PIL import Image                                                           
import pytesseract                                                              
import scrapy  
import time
from selenium import webdriver

from io import BytesIO
try:
    import Image
except ImportError:
    from PIL import Image
from subprocess import check_output
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
class CaptchaSpider(scrapy.Spider):
    name = 'captcha'
    allowed_domains = ['report.imed.ir']
    flag = True
    path = r'C:\Users\HP\Projects\imed\example.png'
    page = 1  
    file_save = True
    def start_requests(self):                           
        yield SeleniumRequest(
            url = 'http://report.imed.ir/Additionals/srchconfirmedimedcompany.aspx',
            wait_time= 3,
            screenshot=True,
            callback=self.parse
        )
    
    def parse(self, response):
        driver = response.meta['driver']
        if self.flag == True:
            search_input = driver.find_element_by_xpath('//input[@id="ctl00_MainContent_txtVerifyCode"]')
            element = driver.find_element_by_id("ctl00_MainContent_btn_Search")
            image = driver.find_element_by_id("CaptchaIMG").screenshot_as_png
            im = Image.open(BytesIO(image))  # uses PIL library to open image in memory
            im.save('example.png')
            print("Resolving")
            print("Resampling the Image")
            time.sleep(5)
            check_output([r"C:\Program Files\ImageMagick-7.0.9-Q16\magick.exe", self.path, '-resample', '600', self.path])
            captcha_text = pytesseract.image_to_string(Image.open(self.path),config='--psm 6 -c tessedit_char_whitelist=0123456789')
            print("Extracted Text", captcha_text)
            search_input.send_keys(captcha_text)
            driver.save_screenshot('after text.png')
            element.click()
            self.flag = False
            time.sleep(20)

        total_page = driver.find_element_by_xpath('//td[@class="rgPagerCell NumericPages"]/div[@class="rgWrap rgInfoPart"]/strong[2]').text
        while(self.page <= int(total_page)):
            html = driver.page_source
            response_obj = Selector(text=html)
            links = response_obj.xpath('//table[@class="rgMasterTable"]/tbody/tr')
            for each in links:
                urlPath = each.xpath('.//td[3]/a/@href').get()
                agencies_url = each.xpath('.//td[6]/a/@href').get()
                yield {
                    'Col 1-A':each.xpath('normalize-space(.//td[1]/text())').get(),
                    'Col 1-B':each.xpath('.//td[2]/text()').get(),
                    'Col 1-C':each.xpath('.//td[3]/a/@title').get(),
                    'Col 1-D':each.xpath('.//td[4]/text()').get(),
                    'Col 1-E':each.xpath('.//td[5]/text()').get(),
                    'Col 1-F':each.xpath('.//td[7]/a/@title').get(),
                    'AGENCIES':f'http://report.imed.ir/Additionals/{agencies_url}',
                    'URL':f'http://report.imed.ir/Additionals/{urlPath}'
                    }
            next_page = driver.find_element_by_xpath('//div[@class="rgWrap rgNumPart"]/a[@class="rgCurrentPage"]/following-sibling::a/span')
            if next_page:
                print("next page :", next_page.text)
                self.page = self.page + 1
                print("Click",self.page)
                next_page.click()
            else:
                print("THE LAST PAGE")
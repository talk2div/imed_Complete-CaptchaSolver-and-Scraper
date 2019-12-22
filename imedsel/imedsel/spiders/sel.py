# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which
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

class SelSpider(scrapy.Spider):
    name = 'sel'
    allowed_domains = ['report.imed.ir']
    start_urls = ['http://report.imed.ir/Additionals/srchconfirmedimedcompany.aspx']
    path = r'C:\Users\HP\Projects\imedsel\example.png'

    def __init__(self):
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # options=chrome_options

        chrome_path = which("chromedriver")

        driver = webdriver.Chrome(executable_path=chrome_path)
        driver.set_window_size(1920, 1080)
        driver.get("http://report.imed.ir/Additionals/srchconfirmedimedcompany.aspx")
        search_input = driver.find_element_by_xpath('//input[@id="ctl00_MainContent_txtVerifyCode"]')
        element = driver.find_element_by_id("ctl00_MainContent_btn_Search")
        image = driver.find_element_by_id("CaptchaIMG").screenshot_as_png
        im = Image.open(BytesIO(image))  # uses PIL library to open image in memory
        im.save('example.png')
        print("Resolving")
        print("Resampling the Image")
        time.sleep(10)
        check_output([r"C:\Program Files\ImageMagick-7.0.9-Q16\magick.exe", self.path, '-resample', '600', self.path])
        captcha_text = pytesseract.image_to_string(Image.open(self.path),config='--psm 7 -c tessedit_char_whitelist=0123456789')
        print("Extracted Text", captcha_text)
        search_input.send_keys(captcha_text)
        driver.save_screenshot('after text.png')
        element.click()
        driver.save_screenshot('after keys.png')
        time.sleep(20)
        self.html = driver.page_source
        driver.close()

    def parse(self, response):
        resp = Selector(text=self.html)
        for each in resp.xpath("//table[@class='rgMasterTable']/tbody/tr"):
            yield {
                'url':each.xpath('.//td[3]/a/@href').get(),
            }
        pass
            
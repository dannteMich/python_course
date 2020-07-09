# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.selector import Selector
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
import os

class LoginSpider(scrapy.Spider):
    name = "corona"
    start_urls = (
        'https://www.facebook.com/login',
    )

    def start_requests(self):       
    
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
        self.driver.get('https://www.facebook.com/login')
        time.sleep(3)
        username = self.driver.find_element_by_id("email")
        password = self.driver.find_element_by_id("pass")
        username.send_keys("")
        password.send_keys("")
        self.driver.find_element_by_name("login").click()
        time.sleep(3)
        self.driver.get('https://mobile.facebook.com/NaftaliBennett/?tsid=0.23867327949342498&source=result')
        time.sleep(2)
        x2 =0
        while True:
         self.driver.refresh()
         html = self.driver.find_element_by_tag_name('body')
         while x2<50:
          x2 = x2+1
          html.send_keys(Keys.DOWN) 
          html.send_keys(Keys.DOWN) 
          html.send_keys(Keys.DOWN) 
          html.send_keys(Keys.DOWN)
          html.send_keys(Keys.DOWN)
         x2 = 0 
         self.driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div[1]/div/div[4]/div/div[4]/div[6]/div[2]/div[1]/div/article/footer/div/div[2]/div[2]/a").click()
         time.sleep(2)
         sel = Selector(text=self.driver.page_source)
         bibi = sel.xpath("//*[@class='_5rgt _5nk5']//p/text()").extract()
         time.sleep(2)
         if bibi[1] != ' וזה לא מרוכז ב2-3 מוקדים כפי שהיה בעבר?':
           comment = self.driver.find_element_by_id("composerInput")
           comment.send_keys("נפתלי בנט אני מעריץ שלך אתה תרמת רבות למדינת ישראל. שירתת ביחדות לוחמה הכי מובחרות של צהל ועד היום משרת במילואים . אתה עשית סטארט אפ שהכניס מיליונים לקופת המדינה ובתור שר ביטחון דאגתה שתושבי הדרום יוכלו לישון בשקט ועוד הרבה המון דברים נסתרים מעין בגבול הצפון! בבחירות הבאות ללא ספק הצביע עבורך לרשות הממשלה! ושוב תודה רבה מעומק הלב!")
           time.sleep(2)
           self.driver.find_element_by_css_selector('._54k8._52jg._56bs._26vk._3lmf._3fyi._56bv._653w').click()
           break
         else:
            self.driver.back()
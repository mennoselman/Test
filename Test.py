from bs4 import BeautifulSoup 
import urllib2
import selenium
import signal
from contextlib import closing
#from selenium.webdriver import Firefox # pip install selenium
#from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import platform
import time


# In[3]:
def init_phantomjs_driver(*args, **kwargs):

    webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'

    driver =  webdriver.PhantomJS(*args, **kwargs)
    # driver.set_window_size(1400, 1000)

    return driver

class Crawler():
    def __init__(self):

        self.driver = init_phantomjs_driver(executable_path='driver/phantomjs')

        self.driver.implicitly_wait(10)  # seconds
        self.driver.set_page_load_timeout(30)

        self.starting()


    def starting(self):
        self.driver.get("https://www.ah.nl/producten")
        WebDriverWait(self.driver, timeout=30).until(
         lambda x: x.find_element_by_xpath("//div[@class='lane row product-category-navigation-lane  product-category-navigation-lane--ah']"))
        page_source = browser.page_source
        print(page_source)
        #self.driver.save_screenshot('check.png')

    def quit(self):
        try:
            self.driver.service.process.send_signal(signal.SIGTERM)
            self.driver.quit()
        except:
            self.driver.quit()

crawler = Crawler()
__author__ = 'zhukelin'
__date__ = '2019/4/7 0007 上午 12:58'

import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=option)
driver.get(url="https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F")
time.sleep(20)
print(driver.title)

search_content = WebDriverWait(driver,timeout=5).until(EC.presence_of_element_located((By.XPATH,'//input[@id="q"]')))
search_content.send_keys('衣服')
time.sleep(3)
#点击事件
search_button = WebDriverWait(driver,timeout=5).until(EC.presence_of_element_located((By.XPATH,'//button[contains(@class,"btn-search")]')))
search_button.click()
items = driver.find_element_by_xpath('')
image_url = WebDriverWait(driver, timeout=5).until(lambda d: d.find_element_by_xpath(
    '//div[@contains(@class,"grid")]/div[1]//img')).get_attribute('src')
with open('淘宝图片链接.json','w',encoding='utf-8') as f:
    f.write(image_url)





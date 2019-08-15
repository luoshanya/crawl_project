from selenium import webdriver
import time


driver = webdriver.Chrome()

get_data = driver.get('http://www.baidu.com')

time.sleep(4)
driver.close()
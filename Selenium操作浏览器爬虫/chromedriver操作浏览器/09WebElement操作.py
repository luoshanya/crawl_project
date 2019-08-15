from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
driver_path = r'E:\carlow\Chromedriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://www.baidu.com')


submitBtn = driver.find_element_by_id('su')
#查看类型
print(type(submitBtn))
#去属性里的值
print(submitBtn.get_attribute('value'))
#截图保存 jpg或者pgn格式都行
driver.save_screenshot('baidu.png')
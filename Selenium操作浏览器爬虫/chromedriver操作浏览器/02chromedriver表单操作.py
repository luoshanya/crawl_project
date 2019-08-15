from selenium import webdriver
import time
#操作select选择框需要导入以下命令
from selenium.webdriver.support.ui import Select



# 操作文本框
# driver_path = r'E:\carlow\Chromedriver\chromedriver.exe'
#
# driver = webdriver.Chrome(executable_path=driver_path)
#
# driver.get('https://www.baidu.com')

# driver_tag = driver.find_element_by_id('kw')
#输入文本框文字
# driver_tag.send_keys('python')
# time.sleep(3)

#清除文本框文字
# driver_tag.clear()
#退出quit()

#操作CheckBox框   暂时使用不了
# driver_path = r'E:\carlow\Chromedriver\chromedriver.exe'
#
# driver = webdriver.Chrome(executable_path=driver_path)
#
# driver.get('https://www.douban.com')
# driver.implicitly_wait(10)
# driver_remember = driver.find_element_by_name('remember')
# driver_remember.click()

#操作select选项框
# driver_path = r'E:\carlow\Chromedriver\chromedriver.exe'
# # 还需要用Select进行封装
# driver = webdriver.Chrome(executable_path=driver_path)
#
# driver.get('https://www..com')
# driver_select = Select(driver.find_element_by_name('remember'))
# #按照index索引查取第一个下标
# driver_select.select_by_index(1)

#操作按钮button

driver_path = r'E:\carlow\Chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://www.sogou.com')

driver_tag = driver.find_element_by_id('query')
# 输入文本框文字
driver_tag.send_keys('python')

#找到button的元素
Botton_tag = driver.find_element_by_id('stb')
#点击事件 点击按钮click()
Botton_tag.click()



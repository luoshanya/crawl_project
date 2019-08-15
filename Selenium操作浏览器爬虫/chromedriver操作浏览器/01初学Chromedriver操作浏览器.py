#调用selenium库中的模块webdriver
from selenium import webdriver
import time
#导入谷歌浏览器的Chromedriver.exe的路径
driver_path = r'E:\carlow\Chromedriver\chromedriver.exe'

#导入driver_path 链接浏览器的driver 方便以后操作浏览器
driver = webdriver.Chrome(executable_path=driver_path)

#操作浏览器对网页进行请求  但并不会返回一个参数
driver.get('https://www.baidu.com')
#需要查看的话要输入命令.page_source
print(driver.page_source)

# 根据id选择器查找元素
# inputTag = driver.find_element_by_id('kw')

# #给输入框填充内容
# inputTag.send_keys('python')

# 根据class_name查获取元素
# inputTag = driver.find_element_by_class_name('s_ipt')
# inputTag.send_keys('python')
# time.sleep(3)
# driver.quit()

# 根据name属性查找元素
# inputTag = driver.find_element_by_name('wd')
# inputTag.send_keys('python')

#根据标签名来查找元素
# inputTag = driver.find_elements_by_tag_name('input')
# inputTag.send_keys('python')

#根据xpath语法查找元素
# inputTag = driver.find_element_by_xpath('//input[@class="s_ipt"]')
# inputTag.send_keys('python')

#根据css选择器查找元素
# inputTag = driver.find_element_by_css_selector('.s_ipt')
# inputTag.send_keys('python')
# time.sleep(4)
# driver.quit()

# 如果只是想要解析网页中的数据，那么推荐将网页源代码扔给lxml来解析，因为lxml底层是c成语言写的,所以效率会更高
# 如果是想要对元素进行一些操作，比如一个文本框输入值，或者点击某个按钮，那么就必须使用selenium给我们提供的查找元素方法。
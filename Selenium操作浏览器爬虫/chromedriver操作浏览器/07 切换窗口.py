from selenium import webdriver
import time

driver_path = r'E:\carlow\Chromedriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://www.baidu.com')

#创建新的窗口
driver.execute_script("window.open('https://www.douban.com')")
print(driver.current_url)
#查看当前的所有新窗口 是一个列表形式
print(driver.window_handles)
#切换新窗口driver的url
driver.switch_to.window(driver.window_handles[1])
#查看当前的driver的url
print(driver.current_url)

#虽然在窗口中切换到了新的页面，但是driver中还没有切换。
#如果想要在代码中切换到新的页面中，并且要做一些爬虫。
#那么应该使driver.switch_to.window来切换到指定的窗口。
#从driver.window_handles中提取具体的第几个窗口
#driver.window_handles是一个列表，里面装的都是窗口句柄
#他会按照页面的顺序来存储窗口的句柄







time.sleep(4)
driver.quit()
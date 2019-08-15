from selenium import webdriver
#导入行为链
from selenium.webdriver.common.action_chains import ActionChains



driver_path = r'E:\carlow\Chromedriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://www.baidu.com')

input_tag = driver.find_element_by_id('kw')
#找到submit元素
submit_tag = driver.find_element_by_id('su')

#将driver传进ActinChains类里面
action = ActionChains(driver)
#将鼠标移动到input_tag上面
action.move_to_element(input_tag)
#给input标签填写内容 指明在input_tag中添加文字
action.send_keys_to_element(input_tag,'python')
#将鼠标移动到submit 上
action.move_to_element(submit_tag)
#给按钮一个点击事件
action.click()
#调用这个函数 开始运行
action.perform()
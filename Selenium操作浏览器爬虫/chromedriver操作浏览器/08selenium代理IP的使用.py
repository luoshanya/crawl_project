from selenium import webdriver

#创建proxy的容器
options = webdriver.ChromeOptions()
#将代理IP放进容器
# options.add_argument('--proxy-server=http://')

driver_path = r'E:\carlow\Chromedriver\chromedriver.exe'
#添加代理options   chrome_options = options
driver = webdriver.Chrome(executable_path=driver_path,options=options)
# #查看自己IP的地址
# driver.get('http://httpbin.org/ip')
driver.get('https://www.baidu.com')

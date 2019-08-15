from selenium import webdriver

driver_path = r'E:\carlow\Chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com')
#取到百度发送过来的全部cookies
for cookie in driver.get_cookies():
    print(cookie)

print('='*30)
#取某个cookie
print(driver.get_cookie('PSTM'))
#删除某个cookie
driver.delete_cookie('PSTM')
print('='*30)

print(driver.get_cookie('PSTM'))
#删除全部的cookies
driver.delete_all_cookies()
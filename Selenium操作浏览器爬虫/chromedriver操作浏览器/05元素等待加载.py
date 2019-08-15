from selenium import webdriver
#导入隐式等待的包
from selenium.webdriver.support.ui import WebDriverWait
#导入期望语句  通常简写EC
from selenium.webdriver.support import expected_conditions as EC
#导进选择器用到的繁写
from selenium.webdriver.common.by import By




driver_path = r'E:\carlow\Chromedriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://www.douban.com')
#隐式等待driver.implicitly_wait(20)
# driver.implicitly_wait(20)
# driver_remember = driver.find_element_by_name('remember')
# driver_remember.click()

#显示等待
remember_tag = WebDriverWait(driver,10).until(
    #ID要放进元组里面()
    EC.presence_of_element_located((By.NAME,'remember'))
)

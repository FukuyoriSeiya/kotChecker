from selenium import webdriver
import time
import const

# ログインページに遷移
driver = webdriver.Chrome('C:\Chrome\chromedriver.exe')
driver.get('https://github.com/login')

time.sleep(1)

# ログイン処理
mail = driver.find_element_by_name('login')
password = driver.find_element_by_name('password')

mail.clear()
password.clear()

mail.send_keys(const.EMAIL)
password.send_keys(const.PASSWORD)

mail.submit()

# マイページに遷移
driver.get('https://github.com/' + const.UNAME)

# テーブル内容取得
elem = driver.find_element_by_xpath("//*")
source_code = elem.get_attribute("outerHTML")

print(source_code)

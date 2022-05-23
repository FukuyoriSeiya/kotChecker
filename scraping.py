from selenium import webdriver
import time
import const
import re
import pandas as pd


def getGithub():
    # ログインページに遷移
    driver = webdriver.Chrome('C:/Chrome/chromedriver.exe')
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
    html = elem.get_attribute("outerHTML")

    # 特定の箇所を抽出
    patter_count = "data-count=" + r'"[0-9]"'  # 「data-count=」を抽出
    data_count = re.findall(patter_count, html)

    patter_date = 'data-date=' + r'"[0-9]{4}\-[0-9]{2}\-[0-9]{2}"'
    data_date = re.findall(patter_date, html)

    # dfの作成
    df = pd.DataFrame({"date": data_date, "count": data_count})
    df['count'] = df['count'].str.strip('data-count=')
    df['date'] = df['date'].str.strip('data-date=')
    
    # データ整形
    df['count'] = df['count'].str.replace('"',"").astype(int)
    df['date'] = pd.to_datetime(df['date'].str.replace('"',""))
    print(df)
    return df

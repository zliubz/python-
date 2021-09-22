from selenium import webdriver
#1.引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
from pandas import DataFrame as df
import pymysql
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

def getList(elements):
    global index,title
    for i in range(len(elements)):
        url.append(elements[i].find_element_by_tag_name('a').get_attribute('href'))
        title.append(elements[i].find_element_by_xpath('//*[@id="hotsearch-content-wrapper"]/li[{}]/a/span[2]'.format(str(i+1))).text)
        #single.append(elements[i].find_element_by_xpath('//*[@id="s_xmancard_news_new"]/div/div[1]/div/div/ul/li[{}]/div'.format(str(1))).text)


driver = webdriver.Chrome(chrome_options=chrome_options)
driver.maximize_window()
driver.get("https://www.baidu.com")
butt = driver.find_element_by_xpath('//*[@id="hotsearch-refresh-btn"]')
url=[]
title=[]
date=time.strftime("%Y-%m-%d", time.localtime()) 
for i in range(4):
    elements = driver.find_elements_by_xpath('//*[@id="hotsearch-content-wrapper"]/li')
    getList(elements)
    action=ActionChains(driver)
    action.click_and_hold(butt).release(butt).perform()


conn = pymysql.connect(
    host='localhost',
    user='root',password='990108',
    database='百度新闻',
    charset='utf8')
cursor = conn.cursor()
sql = 'CREATE TABLE IF NOT EXISTS 百度新闻合集 (标题 varchar(30), 链接 varchar(1000),日期 varchar(20));'
cursor.execute(sql)
sql = 'CREATE TABLE IF NOT EXISTS 每日百度新闻 (标题 varchar(30), 链接 varchar(1000));'
cursor.execute(sql)
sql='insert into 百度新闻合集 values(%s,%s,%s);'
for i in range(len(title)):
    cursor.execute(sql,(title[i],url[i],date))
sql='insert into 每日百度新闻 values(%s,%s);'
for i in range(len(title)):
    cursor.execute(sql,(title[i],url[i]))
conn.commit()
cursor.close()
conn.close()






from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
driver.find_element_by_id('kw').send_keys('虚竹')
driver.find_element_by_id('su').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()
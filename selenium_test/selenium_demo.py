from selenium import webdriver
from time import sleep

dv = webdriver.Chrome()
dv.maximize_window()
dv.get(url="http://192.168.205.128:8080/recruit.students/login/view")
dv.find_element_by_id("txtUserName").send_keys("admin")
sleep(1)
dv.find_element_by_id("txtPassword").send_keys("test123")
sleep(1)
dv.find_element_by_xpath("//*[@class='form-signin']/a").click()

sleep(5)
dv.quit()

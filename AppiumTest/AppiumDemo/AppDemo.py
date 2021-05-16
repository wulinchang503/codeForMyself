from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction

# from selenium.webdriver.support.wait import WebDriverWait

# 找到这个手机
desired = {
    "deviceName": "127.0.0.1:62001",
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "appPackage": "com.android.settings",
    # "appActivity": ".Settings",
    "appActivity": ".ChooseLockPattern"

}
# 链接远程设备并打开应用
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired)
# print(driver.current_package)
# print(driver.current_activity)
# time.sleep(1)
# driver.find_element_by_id("search").click()
# time.sleep(5)
# driver.find_element_by_class_name("android.widget.EditText").send_keys("通知")
# time.sleep(5)
# driver.find_element_by_xpath("//*[@content-desc='收起']").click()
# driver.find_element_by_id("com.android.settings:id/search").click()
# time.sleep(2)
# driver.find_element_by_class_name("android.widget.EditText").send_keys("Hello")
# time.sleep(3)
# driver.find_element_by_class_name("android.widget.EditText").clear()
# time.sleep(4)
# driver.find_element_by_class_name("android.widget.EditText").send_keys("wlan")
# mobile_net = driver.find_element_by_xpath("//*[@text='移动数据网络已关闭']")
# print(mobile_net.text)
# print(mobile_net.location)
# print(mobile_net.size)
# titles = driver.find_elements_by_id("android:id/title")
# for title in titles:
#     print(title.text, end=" ")
#     print(title.get_attribute("package"), end=" ")
#     print(title.get_attribute("bounds"), end="")
#     print("")
# driver.swipe(450, 1300, 450, 500, 1000)
# display_button = driver.find_element_by_xpath("//*[@text='建议']")
# print(display_button.text)
# wifi_button = driver.find_element_by_xpath("//*[@text='WLAN']")

# driver.scroll(wifi_button, display_button)
# driver.drag_and_drop(display_button, wifi_button)
# 找到更换壁纸元素

print(driver.get_window_size())

TouchAction(driver).press(x=180, y=770).move_to(x=450, y=770).move_to(x=710, y=1040).move_to(x=450, y=1300).move_to(
    x=180, y=1040).release().perform()
driver.get_screenshot_as_file('截图.png')
time.sleep(2)
TouchAction(driver).tap(x=760, y=1500).perform()
# wlan = driver.find_element_by_xpath("//*[@text='WLAN']")
# # touch_action = TouchAction(driver)  # 创建TouchAction对象
# # touch_action = touch_action.tap(change_paper)
# # touch_action.perform()
# TouchAction(driver).tap(x=400, y=400, count=2).perform()
# TouchAction(driver).press(x=300, y=400).perform()
# time.sleep(2)
# TouchAction(driver).tap(element=wlan).perform()
#
# time.sleep(2)
# TouchAction(driver).press(x=180, y=770).move_to(x=450, y=770).move_to(x=710, y=1040).move_to(x=450, y=1300).move_to(
#     x=180, y=1040).release().perform()
# wlan_info = driver.find_element_by_xpath("//*[@text='WiredSSID']")
# TouchAction(driver).press(el=wlan_info).release().perform()
# TouchAction(driver).press(wlan_info).wait(2000).release().perform()
# TouchAction(driver).long_press(el=wlan_info, duration=100).perform()
time.sleep(2)
TouchAction(driver).tap(x=760, y=1500).perform()

# setting = driver.find_element_by_class_name("android.widget.TextView")
# print(setting.get_attribute("bounds"))
# print("-----开始等待，10s内点击搜索按钮测试")
# wait = WebDriverWait(driver, 10)
# wait.until(lambda x: x.find_element_by_xpath("//*[@content-desc='收起']")).click()
# print("-----我找到了，并点完了")
# driver.background_app(10)  # 将应用放置到后台 多少秒
# time.sleep(5)
#  切换应用
# # driver.start_activity("com.android.browser", ".BrowserActivity")
# # print(driver.current_package)
# # print(driver.current_activity)
# # time.sleep(10)
driver.close_app()
# print(driver.current_package)
# driver.quit()
# # print(driver.current_package)
# time.sleep(2)
# # 判断是否安装安智市场
# if driver.is_app_installed("cn.goapk.market"):
#     # 如果已安装，就卸载
#     driver.remove_app("cn.goapk.market")
# else:
#     # 如果未安装，就安装这个app (传参数安装包的本地路径)
#     driver.install_app(r"D:\androidTest\anzhimarket.apk")
#
# time.sleep(5)
driver.quit()

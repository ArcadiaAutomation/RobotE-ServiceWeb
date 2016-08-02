import os
import time
from appium import webdriver

def getsms(sender,ip,index,udid):
    index = int(index)
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.2'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['appPackage'] = 'com.calea.echo'
    desired_caps['appActivity'] = 'com.calea.echo.MainActivity'
    desired_caps['udid'] = udid
    os.chdir("C:\Program Files (x86)\Appium\\node_modules")
    os.system("start cmd /k node appium -p 4723 -a "+ip+" --session-override")
    time.sleep(10)
    driver = webdriver.Remote('http://'+ip+':4723/wd/hub', desired_caps)
    name = driver.find_element_by_name(sender)
    name.click()
    time.sleep(5)
    sms = driver.find_elements_by_xpath("//*[@resource-id='com.calea.echo:id/imm_text']")
    return sms[len(sms)-index].get_attribute("text")

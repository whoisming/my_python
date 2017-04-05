#coding:utf-8

from appium import webdriver
from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'a4234bf6'
desired_caps['app'] = '/Users/zhiming/Desktop/app-release.apk'
desired_caps['appPackage'] = 'com.prance.app'
desired_caps['appActivity'] = '.ui.splash.WelcomeActivity'

dr = webdriver.Remote('http://10.88.88.182:4723/wd/hub', desired_caps)
sleep(5)
dr.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.Button[1]').click()
sleep(2)
dr.find_element_by_id('com.prance.app:id/login_btn').click()
sleep(2)
dr.find_element_by_id('com.prance.app:id/phone').send_keys('13426089565')
sleep(2)
dr.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]').send_keys('y123456')
sleep(2)
dr.find_element_by_id('com.prance.app:id/login').click()
sleep(10)

dr.find_element_by_id('com.prance.app:id/media_play_btn').click()
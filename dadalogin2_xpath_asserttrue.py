# -*- coding: UTF-8 -*-
from appium import webdriver
from time import sleep
import os
import unittest
import HTMLTestRunner
#from nose.tools import assert_true,assert_false

from selenium.common.exceptions import NoSuchElementException

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class loginbutton(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['device'] = 'android'
        desired_caps['platformName'] = 'Android'
        desired_caps['version'] = '4.4.4'  # 手机的android版本号
        desired_caps['deviceName'] = '295d9976'  # adb devices探测到的手机ID  #92bda50
        desired_caps['appPackage'] = 'com.newdadabus'  # app的包名
        desired_caps['appActivity'] = 'com.newdadabus.ui.activity.MainActivity'  # app的activity名
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()
        print '执行结束'

    def test_buttonA(self):
        for i in range(1,3):
            if i ==1:   #获取验证码按钮生效
                print '\ncase1'
                self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.TextView[4]").click()   #Xpath定位大法1
                self.driver.find_element_by_xpath("//*[@text='我的']").click()  #xpath绝对路径大法2
                #self.driver.find_element_by_id('com.newdadabus:id/ivUser').click()
                sleep(3)
                self.driver.find_element_by_id('com.newdadabus:id/llUserLayout').click()
                sleep(3)
                self.driver.find_element_by_id('com.newdadabus:id/tvMobileLogin').click()
                sleep(3)
                self.driver.find_element_by_id('com.newdadabus:id/etLoginMobile').send_keys('12345678911')
                self.assertTrue(self.driver.find_element_by_name(u'获取验证码').is_enabled(),u'手机号未输入或输入错误')
            if i ==2:  #获取验证码按钮失效_1,无手机号
                print 'case2'
                self.driver.find_element_by_id('com.newdadabus:id/etLoginMobile').clear()
                self.assertFalse(self.driver.find_element_by_name(u'获取验证码').is_enabled(),u'手机号未输入按钮应无法点击')

if __name__ == '__main__':
    testunit = unittest.TestSuite()  # 定义一个单元测试容器
    testunit.addTest(loginbutton("buttonA"))  # 将测试用例加入到测试容器中
    # testunit.addTest(elementA("dadaloginerror"))
    # testunit.addTest(elementA("dadaloginerror2")
    filename = "./myAppiumLog.html"  # 定义个报告存放路径，支持相对路径。
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Report_title',description='Report_description')  # 使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
    runner.run(testunit)
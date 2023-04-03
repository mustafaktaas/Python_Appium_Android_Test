import pytest
import time
import json
from selenium.webdriver.common.action_chains import ActionChains
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction


class TestLogin():

    def setup_method(self):
        desired_cap = {
            "platformName": "android",
            "deviceName": "emulator-5554",
            "app": "C:\\Appium\\app-release.apk"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
        self.driver.implicitly_wait(30)
        self.driver.find_element(AppiumBy.XPATH,
                            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(AppiumBy.XPATH,
                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ImageView").click()
        self.driver.implicitly_wait(30)

    def teardown_method(self):
        self.driver.quit()

    def test_loginwait(self):
        el1 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.TextView")
        el1.click()
        el2 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText")
        el2.send_keys("Dosya")
        el3 = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.TextView")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout")
        el4.click()
        el4.click()
        el5 = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView")
        el5.click()
        el5.click()
        el6 = self.driver.find_element(by=AppiumBy.XPATH,value="//android.widget.ImageView[@content-desc='Sorguyu temizle']")
        el6.click()

        x = 84
        y  = 218

        action = TouchAction(self.driver)
        action.tap(x=x, y=y).perform()

        el1 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/android.view.View")
        el1.click()
        el2 = self.driver.find_element(by=AppiumBy.ID, value="com.netdatasoft.android.divvydrive:id/create_tv")
        el2.click()
        el3 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/android.view.View")
        el3.click()
        el5 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.TextView")
        el5.click()
        el6 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ImageView")
        el6.click()
        el7 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.Button[2]")
        el7.click()

        self.driver.find_element(AppiumBy.ID, "com.netdatasoft.android.divvydrive:id/KullaniciAdi").send_keys("dsadas")
        self.driver.implicitly_wait(30)
        self.driver.find_element(AppiumBy.ID, "com.netdatasoft.android.divvydrive:id/KullaniciSifre").send_keys("dsadasda")
        self.driver.implicitly_wait(30)
        self.driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(AppiumBy.ID, "com.netdatasoft.android.divvydrive:id/KullaniciAdi").send_keys("demo10")
        self.driver.implicitly_wait(30)
        self.driver.find_element(AppiumBy.ID, "com.netdatasoft.android.divvydrive:id/KullaniciSifre").send_keys(
            "1234567Abc.")
        self.driver.implicitly_wait(30)
        self.driver.find_element(AppiumBy.XPATH,
                                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(AppiumBy.XPATH,
                                 "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button").click()

        '''
    def test_validloginwait(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(AppiumBy.ID, "com.netdatasoft.android.divvydrive:id/KullaniciAdi").send_keys("demo10")
        self.driver.implicitly_wait(30)
        self.driver.find_element(AppiumBy.ID, "com.netdatasoft.android.divvydrive:id/KullaniciSifre").send_keys("1234567Abc.")
        self.driver.implicitly_wait(30)
        self.driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button").click()
        '''

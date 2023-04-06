import pytest
import time
import os
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction


class TestApp():

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
        self.driver.find_element(AppiumBy.ID, "com.netdatasoft.android.divvydrive:id/KullaniciAdi").send_keys("test10")
        self.driver.implicitly_wait(30)
        self.driver.find_element(AppiumBy.ID, "com.netdatasoft.android.divvydrive:id/KullaniciSifre").send_keys(
            "1234567Abc.")
        self.driver.implicitly_wait(30)
        self.driver.find_element(AppiumBy.XPATH,
                                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(AppiumBy.XPATH,
                                 "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button").click()

    def teardown_method(self):
        self.driver.quit()

    def test_app(self):
        # profile_photo
        '''xxx
        el1 = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="	//android.widget.ImageButton[@content-desc='Gezinme Çekmecesini Aç']")
        el1.click()
        el2 = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.RelativeLayout/android.widget.ImageButton")
        el2.click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Gezinme Çekmecesini Aç")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ExpandableListView/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView")
        el4.click()

        el5 = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button")
        el5.click()
        el6 = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="/ hierarchy / android.widget.FrameLayout / android.widget.FrameLayout / android.widget.FrameLayout / android.widget.LinearLayout / android.widget.LinearLayout / \
          android.widget.LinearLayout[1] / android.widget.TextView")
        el6.click()
        el9 = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="//android.widget.LinearLayout[@content-desc='scan_20230404120202.jpeg, 19.25 kB, Apr 4']/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ImageView[1]")
        el9.click()

        el10 = self.driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button")
        el10.click()
        el11 = self.driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView")
        el11.click()
        self.driver.back()
        time.sleep(0.500)
        xxx'''

        # search_function
        '''xxx
        el1 = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView[1]")
        el1.click()
        el2c = self.driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout")
        el2c.click()
        el2 = self.driver.find_element(by=AppiumBy.ID, value="com.netdatasoft.android.divvydrive:id/search_src_text")
        el2.send_keys(".pdf")

        time.sleep(0.200)
        self.driver.press_keycode(84)

        el4 = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView")
        el4.click()
        el6 = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView")
        el6.click()
        el7 = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.Switch[1]")
        el7.click()
        el8 = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[3]/android.widget.Button[2]")
        el8.click()
        el9 = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView")
        el9.click()
        el10 = self.driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.Switch[1]")
        el10.click()
        el11 = self.driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.Switch[2]")
        el11.click()
        time.sleep(0.300)
        el11.click()
        el12 = self.driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.Switch[1]")
        el12.click()
        time.sleep(0.300)
        el12.click()
        el13 = self.driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.Switch[2]")
        el13.click()
        time.sleep(0.300)
        el13.click()
        el14 = self.driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.Switch[3]")
        el14.click()
        time.sleep(0.300)
        el14.click()
        el15 = self.driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[3]/android.widget.Switch[1]")
        el15.click()
        time.sleep(0.300)
        el15.click()
        el16 = self.driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[3]/android.widget.Switch[2]")
        el16.click()
        time.sleep(0.300)
        el16.click()
        el17 = self.driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[4]/android.widget.Button[2]")
        el17.click()
        el18 = self.driver.find_element(by=AppiumBy.ID,
                                        value="com.netdatasoft.android.divvydrive:id/search_close_btn")
        el18.click()
        time.sleep(0.500)
        xxx'''

        #shortcut_function
        '''xxx
        el2 = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.ImageButton")
        el2.click()
        el3 = self.driver.find_element(by=AppiumBy.ID, value="com.netdatasoft.android.divvydrive:id/kisayol_olustur_tv")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="com.netdatasoft.android.divvydrive:id/create_tv")
        el4.click()
        el5 = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="//android.widget.FrameLayout[@content-desc=\"Kısayollar\"]/android.widget.FrameLayout")
        el5.click()
        el6 = self.driver.find_element(by=AppiumBy.ID, value="com.netdatasoft.android.divvydrive:id/user_deck_line_tv")
        el6.click()
        el7 = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="//android.widget.FrameLayout[@content-desc=\"Kısayollar\"]/android.widget.FrameLayout/android.widget.ImageView")
        el7.click()
        el8 = self.driver.find_element(by=AppiumBy.ID, value="com.netdatasoft.android.divvydrive:id/shortcut_detail_action")
        el8.click()
        time.sleep(0.300)
        el9 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout")
        el9.click()
        el10 = self.driver.find_element(by=AppiumBy.XPATH,
                                   value="//android.widget.FrameLayout[@content-desc=\"Duvarım\"]/android.widget.FrameLayout/android.widget.ImageView")
        el10.click()
        time.sleep(0.500)
        xxx'''

        #notifications_function

        el1 = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView[2]")
        el1.click()
        el2 = self.driver.find_element(by=AppiumBy.XPATH, value="com.netdatasoft.android.divvydrive:id/bildirim_sil")
        el2.click()
        el3 = self.driver.find_element(by=AppiumBy.XPATH, value="com.netdatasoft.android.divvydrive:id/clear_all")
        el3.click()
        self.driver.back()
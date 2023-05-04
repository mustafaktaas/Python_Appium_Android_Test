import pytest
import time
import os
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestApp():

        desired_cap = {
            "platformName": "android",
            "deviceName": "emulator-5554",
            "app": "C:\\Appium\\app-release.apk"
        }

        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
        driver.implicitly_wait(30)
        driver.find_element(AppiumBy.XPATH,
                                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ImageView").click()
        driver.implicitly_wait(30)
        driver.find_element(AppiumBy.ID, "com.netdatasoft.android.divvydrive:id/KullaniciAdi").send_keys("test10")
        driver.implicitly_wait(30)
        driver.find_element(AppiumBy.ID, "com.netdatasoft.android.divvydrive:id/KullaniciSifre").send_keys(
            "1234567Abc.")
        driver.implicitly_wait(30)
        driver.find_element(AppiumBy.XPATH,
                                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button").click()
        driver.implicitly_wait(30)

        # profile_photo
        el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Gezinme Çekmecesini Aç")
        el3.click()
        el4 = driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ExpandableListView/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView")
        el4.click()

        el5 = driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button")
        el5.click()
        el6 = driver.find_element(by=AppiumBy.XPATH,
                                       value="/ hierarchy / android.widget.FrameLayout / android.widget.FrameLayout / android.widget.FrameLayout / android.widget.LinearLayout / android.widget.LinearLayout / \
          android.widget.LinearLayout[1] / android.widget.TextView")
        el6.click()

        time.sleep(0.500)
        TouchAction(driver).tap(None, 180, 1053, 1).perform()

        el9 = driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.TextView")
        el9.click()
        time.sleep(0.300)
        el10 = driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button")
        el10.click()
        el11 = driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView")
        el11.click()
        time.sleep(0.500)
        driver.back()
        time.sleep(1)
        driver.find_element(by=AppiumBy.XPATH,
                            value="//android.widget.FrameLayout[@content-desc='Duvarım']/android.widget.FrameLayout/android.widget.ImageView").click()
        time.sleep(0.300)

        print("\nProfil Fotografı Başarılı!!!\n")

        # search_function

        time.sleep(0.500)
        el1 = driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView[1]")
        el1.click()
        el2c = driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout")
        el2c.click()
        el2 = driver.find_element(by=AppiumBy.ID, value="com.netdatasoft.android.divvydrive:id/search_src_text")
        el2.send_keys(".pdf")

        time.sleep(0.200)
        driver.press_keycode(84)

        el4 = driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView")
        el4.click()
        el6 = driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView")
        el6.click()
        el7 = driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.Switch[1]")
        el7.click()
        el8 = driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[3]/android.widget.Button[2]")
        el8.click()
        el9 = driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView")
        el9.click()
        el10 = driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.Switch[1]")
        el10.click()
        el11 = driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.Switch[2]")
        el11.click()
        time.sleep(0.300)
        el11.click()
        el12 = driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.Switch[1]")
        el12.click()
        time.sleep(0.300)
        el12.click()
        el13 = driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.Switch[2]")
        el13.click()
        time.sleep(0.300)
        el13.click()
        el14 = driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.Switch[3]")
        el14.click()
        time.sleep(0.300)
        el14.click()
        el15 = driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[3]/android.widget.Switch[1]")
        el15.click()
        time.sleep(0.300)
        el15.click()
        el16 = driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[3]/android.widget.Switch[2]")
        el16.click()
        time.sleep(0.300)
        el16.click()
        el17 = driver.find_element(by=AppiumBy.XPATH,
                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[4]/android.widget.Button[2]")
        el17.click()
        el18 = driver.find_element(by=AppiumBy.ID,
                                        value="com.netdatasoft.android.divvydrive:id/search_close_btn")
        el18.click()
        time.sleep(0.500)

        print("\nArama İşlevi Başarılı!!!\n")

        # shortcut_function

        el2 = driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.ImageButton")
        el2.click()
        el3 = driver.find_element(by=AppiumBy.ID, value="com.netdatasoft.android.divvydrive:id/kisayol_olustur_tv")
        el3.click()
        el4 = driver.find_element(by=AppiumBy.ID, value="com.netdatasoft.android.divvydrive:id/create_tv")
        el4.click()
        el5 = driver.find_element(by=AppiumBy.XPATH,
                                       value="//android.widget.FrameLayout[@content-desc=\"Kısayollar\"]/android.widget.FrameLayout")
        el5.click()
        el6 = driver.find_element(by=AppiumBy.ID, value="com.netdatasoft.android.divvydrive:id/user_deck_line_tv")
        el6.click()
        el7 = driver.find_element(by=AppiumBy.XPATH,
                                       value="//android.widget.FrameLayout[@content-desc=\"Kısayollar\"]/android.widget.FrameLayout/android.widget.ImageView")
        el7.click()
        el8 = driver.find_element(by=AppiumBy.ID,
                                       value="com.netdatasoft.android.divvydrive:id/shortcut_detail_action")
        el8.click()
        time.sleep(0.300)
        el9 = driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout")
        el9.click()
        el10 = driver.find_element(by=AppiumBy.XPATH,
                                        value="//android.widget.FrameLayout[@content-desc=\"Duvarım\"]/android.widget.FrameLayout/android.widget.ImageView")
        el10.click()
        time.sleep(0.500)

        print("\nKısayol İşlevleri Başarılı!!!\n")
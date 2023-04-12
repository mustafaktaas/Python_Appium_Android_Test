import pytest
import time
import os
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction


class TestAppLocal():

    def setup_method(self):
        desired_cap = {
            "platformName": "android",
            "deviceName": "emulator-5554",
            "app": "C:\\Appium\\app-release.apk"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
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

    def teardown_method(self):
        self.driver.quit()

    def test_app_local(self):
        """
        # Duvarım Klasör Seçenekleri

        ## Yeniden adlandır-Taşı-Linkle Paylaş- Klasör Paylaş
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]")
        self.find_sendKeys_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.EditText",
            "AAaa")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.Button[2]")
        time.sleep(0.500)
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[4]")
        self.find_sendKeys_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.EditText",
            "AAaa1")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.Button[2]")

        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[4]")
        self.find_sendKeys_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.EditText",
            "AAaa")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.Button[2]")
        print("\nYeniden Adlandırma İşlevi Başarılı!!!")

        ###Taşı
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]")

        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]")
        self.find_click_action(
            "//android.widget.FrameLayout[@content-desc='Duvarım']/android.widget.FrameLayout/android.widget.ImageView")
        print("\nTaşıma İşlevi Başarılı!!!")

        ###Linkle Paylaş
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.View")
        time.sleep(0.500)
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.View")
        time.sleep(0.500)
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.Button")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/com.android.internal.widget.ViewPager/android.widget.RelativeLayout/com.android.internal.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.Button[1]")

        print("\nLinkle Paylaş İşlevi Başarılı!!!")

        ###Klasör Paylaş

        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[6]")

        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.view.View")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]/android.view.View")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]/android.view.View")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]/android.view.View")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.AutoCompleteTextView")
        self.find_sendKeys_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.AutoCompleteTextView",
            "test1")
        self.driver.press_keycode(66)
        time.sleep(1)
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[1]")
        self.driver.back()
        self.find_sendKeys_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText",
            "DenemePaylas")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[2]")
        print("\nKlasör Paylaş İşlevi Başarılı!!!")

        ## Kısayol Oluştur-Erişebilen Kullanıcılar-Klasör Geçmişi- Sil- Kalıcı Sil- Özellikler- Vazgeç

        ### Kısayol oluştur
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[5]")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.Button[2]")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.ImageView")
        self.find_click_action(
            "//android.widget.FrameLayout[@content-desc='Kısayollar']/android.widget.FrameLayout/android.widget.ImageView")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout")
        self.find_click_action(
            "//android.widget.FrameLayout[@content-desc='Duvarım']/android.widget.FrameLayout/android.widget.ImageView")
        print("\nKısayol Oluşturma İşlevi Başarılı!!!")

        ### Erişebilen Kullanıcılar
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[10]")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.Button")
        print("\nErişebilen Kullanıcıların Gözükme İşlevi Başarılı!!!")

        ###Klasör Geçmişi
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.ImageButton")
        bottom_sheet = self.driver.find_element(by=AppiumBy.XPATH,
                                                value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout')

        action = TouchAction(self.driver)
        action.long_press(bottom_sheet).move_to(x=500, y=850).release().perform()
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[11]")
        self.driver.back()
        print("\nKlasör Geçmişi Gözükme İşlevi Başarılı!!!")

        ### Klasör Özellikler
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.ImageButton")
        bottom_sheet = self.driver.find_element(by=AppiumBy.XPATH,
                                                value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout')

        action = TouchAction(self.driver)
        action.long_press(bottom_sheet).move_to(x=500, y=850).release().perform()
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[15]")
        self.find_click_action("//android.widget.LinearLayout[@content-desc='Kurallar']")
        self.driver.back()
        print("\nKlasör Özellikler İşlevi Başarılı!!!")

        ### Klasör Vazgeç
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.ImageButton")
        bottom_sheet = self.driver.find_element(by=AppiumBy.XPATH,
                                                value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout')

        action = TouchAction(self.driver)
        action.long_press(bottom_sheet).move_to(x=500, y=700).release().perform()
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[16]")
        print("\nKlasör Vazgeç İşlevi Başarılı!!!")

        ### Klasör Silme - Kalıcı Sil
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.ImageButton")
        bottom_sheet = self.driver.find_element(by=AppiumBy.XPATH,
                                                value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout')

        action = TouchAction(self.driver)
        action.long_press(bottom_sheet).move_to(x=500, y=850).release().perform()
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[13]")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.Button[2]")
        time.sleep(1)
        print("\nKlasör Silme İşlevi Başarılı!!!")
        """
        """
        # Duvarım Dosya Seçenekleri

        ## Dosya Aç Kapa Görüntüle

        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[5]/android.widget.RelativeLayout/android.widget.TextView")
        time.sleep(1)
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageButton")

        print("\nDosya Aç Kapa Başarılı!!!\n")

        ## Linkle Paylaş

        ###Linkle Paylaş
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[5]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.View")
        time.sleep(0.500)
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.View")
        time.sleep(0.500)
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.Button")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/com.android.internal.widget.ViewPager/android.widget.RelativeLayout/com.android.internal.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.Button[1]")

        print("\nLinkle Paylaş İşlevi Başarılı!!!")

        ###Taşı
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[5]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]")

        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]")
        self.find_click_action(
            "//android.widget.FrameLayout[@content-desc='Duvarım']/android.widget.FrameLayout/android.widget.ImageView")
        print("\nTaşıma İşlevi Başarılı!!!")

        ## Kopyala-Yenidfen adlandır-Dosya Geçmişi-Dosya Versiyonları
              ###Kopyala
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[5]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[4]")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]")

        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.ImageButton")
        bottom_sheet = self.driver.find_element(by=AppiumBy.XPATH,
                                                value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout')

        action = TouchAction(self.driver)
        action.long_press(bottom_sheet).move_to(x=500, y=850).release().perform()
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[13]")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.Button[2]")
        time.sleep(0.500)
        self.find_click_action(
            "//android.widget.FrameLayout[@content-desc='Duvarım']/android.widget.FrameLayout/android.widget.ImageView")
        print("\nKopyala İşlevi Başarılı!!!")
          ### Yeniden Adlandır
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[5]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[5]")
        self.find_sendKeys_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.EditText",
            "Abcc1")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.Button[2]")

        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[5]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[5]")
        self.find_sendKeys_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.EditText",
            "Abcc")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.Button[2]")
        print("\nYeniden Adlandır İşlevi Başarılı!!!")
        ### Dosya Geçmişi
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[5]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[7]")
        self.driver.back()
        print("\nDosya Geçmişi Gözükme İşlevi Başarılı!!!")
        ### Dosya Versiyonları
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[5]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[9]")
        self.find_click_action(
            "//android.widget.FrameLayout[@content-desc='Duvarım']/android.widget.FrameLayout/android.widget.ImageView")
        print("\nDosya Versiyonları Gözükme İşlevi Başarılı!!!")

        ## Dosya Paylaş- İndir-Sil - Kalıcı Olarak Sil- Özellikler- Vazgeç

        ###Dosya Paylaş

        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[5]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[10]")
        '''
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.view.View")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]/android.view.View")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]/android.view.View")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]/android.view.View")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.AutoCompleteTextView")
        self.find_sendKeys_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.AutoCompleteTextView",
            "test1")
        self.driver.press_keycode(66)
        time.sleep(1)
        '''
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.Button[1]")

        print("\nDosya Paylaş İşlevi Başarılı!!!")
        ### Dosya İndir
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[5]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]")
        time.sleep(2)
        print("\nDosya İndir İşlevi Başarılı!!!")

        ### Dosya Kilitle
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[5]/android.widget.RelativeLayout/android.widget.ImageButton")
        bottom_sheet = self.driver.find_element(by=AppiumBy.XPATH,
                                                value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout')

        action = TouchAction(self.driver)
        action.long_press(bottom_sheet).move_to(x=500, y=850).release().perform()

        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[11]")
        self.find_sendKeys_action("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.EditText","Deneme")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[3]/android.widget.Button[2]")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[5]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[9]")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.Button[2]")

        print("\nDosya Kilitle İşlevi Başarılı!!!")
        print("\nSilme İşlevi Atlandı!!!")

        ### Dosya Özellikler
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[5]/android.widget.RelativeLayout/android.widget.ImageButton")
        bottom_sheet = self.driver.find_element(by=AppiumBy.XPATH,
                                                value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout')

        action = TouchAction(self.driver)
        action.long_press(bottom_sheet).move_to(x=500, y=850).release().perform()
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[14]")
        self.find_click_action("//android.widget.LinearLayout[@content-desc='Dosya Güvenlik Raporu']")
        self.driver.back()
        print("\nDosya Özellikler İşlevi Başarılı!!!")

        ### Dosya Vazgeç
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[5]/android.widget.RelativeLayout/android.widget.ImageButton")
        bottom_sheet = self.driver.find_element(by=AppiumBy.XPATH,
                                                value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout')

        action = TouchAction(self.driver)
        action.long_press(bottom_sheet).move_to(x=500, y=700).release().perform()
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[15]")
        print("\nDosya Vazgeç İşlevi Başarılı!!!")
        """

        # Medya Seçenekleri

        ## Medya Aç Kapa Görüntüle

        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.ImageButton")
        time.sleep(1)
        self.driver.back()

        print("\nDosya Aç Kapa Başarılı!!!\n")

        ### Medya Linkle Paylaş
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.View")
        time.sleep(0.500)
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.View")
        time.sleep(0.500)
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.Button")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/com.android.internal.widget.ViewPager/android.widget.RelativeLayout/com.android.internal.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.Button[1]")

        print("\nLinkle Paylaş İşlevi Başarılı!!!")

        ### Medya Taşı
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]")

        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]")
        self.find_click_action(
            "//android.widget.FrameLayout[@content-desc='Duvarım']/android.widget.FrameLayout/android.widget.ImageView")
        print("\nTaşıma İşlevi Başarılı!!!")

        ##  Medya Kopyala-Yenidfen adlandır-Dosya Geçmişi-Dosya Versiyonları
        ### Medya Kopyala
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[4]")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]")

        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.ImageButton")
        bottom_sheet = self.driver.find_element(by=AppiumBy.XPATH,
                                                value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout')

        action = TouchAction(self.driver)
        action.long_press(bottom_sheet).move_to(x=500, y=850).release().perform()
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[13]")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.Button[2]")
        time.sleep(0.500)
        self.find_click_action(
            "//android.widget.FrameLayout[@content-desc='Duvarım']/android.widget.FrameLayout/android.widget.ImageView")
        print("\nKopyala İşlevi Başarılı!!!")
        ### Medya Yeniden Adlandır
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[5]")
        self.find_sendKeys_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.EditText",
            "971")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.Button[2]")

        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[5]")
        self.find_sendKeys_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.EditText",
            "97")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.Button[2]")
        print("\nYeniden Adlandır İşlevi Başarılı!!!")
        ### Medya Dosya Geçmişi
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[7]")
        self.driver.back()
        print("\nDosya Geçmişi Gözükme İşlevi Başarılı!!!")
        ### Medya Dosya Versiyonları
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[9]")
        time.sleep(0.500)
        self.find_click_action(
            "//android.widget.FrameLayout[@content-desc='Duvarım']/android.widget.FrameLayout/android.widget.ImageView")
        print("\nDosya Versiyonları Gözükme İşlevi Başarılı!!!")

        ## Medya Dosya Paylaş- İndir-Sil - Kalıcı Olarak Sil- Özellikler- Vazgeç

        ### Medya Dosya Paylaş

        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[10]")
        '''
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.view.View")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]/android.view.View")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]/android.view.View")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]/android.view.View")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.AutoCompleteTextView")
        self.find_sendKeys_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.AutoCompleteTextView",
            "test1")
        self.driver.press_keycode(66)
        time.sleep(1)
        '''
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.Button[1]")

        print("\nDosya Paylaş İşlevi Başarılı!!!")
        ### Medya Dosya İndir
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]")
        time.sleep(2)
        print("\nDosya İndir İşlevi Başarılı!!!")

        ###  Medya Dosya Kilitle
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.ImageButton")
        bottom_sheet = self.driver.find_element(by=AppiumBy.XPATH,
                                                value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout')

        action = TouchAction(self.driver)
        action.long_press(bottom_sheet).move_to(x=500, y=850).release().perform()

        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[11]")
        self.find_sendKeys_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.EditText",
            "Deneme")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[3]/android.widget.Button[2]")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.ImageButton")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[9]")
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.Button[2]")

        print("\nDosya Kilitle İşlevi Başarılı!!!")
        print("\nSilme İşlevi Atlandı!!!")

        ### Medya Dosya Özellikler
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.ImageButton")
        bottom_sheet = self.driver.find_element(by=AppiumBy.XPATH,
                                                value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout')

        action = TouchAction(self.driver)
        action.long_press(bottom_sheet).move_to(x=500, y=850).release().perform()
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[14]")
        self.find_click_action("//android.widget.LinearLayout[@content-desc='Dosya Güvenlik Raporu']")
        self.driver.back()
        print("\nDosya Özellikler İşlevi Başarılı!!!")

        ### Medya Dosya Vazgeç
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.ImageButton")
        bottom_sheet = self.driver.find_element(by=AppiumBy.XPATH,
                                                value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout')

        action = TouchAction(self.driver)
        action.long_press(bottom_sheet).move_to(x=500, y=700).release().perform()
        self.find_click_action(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[15]")
        print("\nDosya Vazgeç İşlevi Başarılı!!!")


    def find_click_action(self, xpath):
        click = self.driver.find_element(by=AppiumBy.XPATH, value=xpath)
        click.click()

    def find_sendKeys_action(self,xpath,value):
        self.driver.find_element(by=AppiumBy.XPATH, value=xpath).send_keys(value)


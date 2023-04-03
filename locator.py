from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

desired_cap = {
  "platformName": "android",
  "deviceName": "emulator-5554",
  "app": "C:\\Appium\\app-release.apk"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

driver.implicitly_wait(120)
driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button").click()
driver.implicitly_wait(120)
driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ImageView").click()
driver.implicitly_wait(120)

driver.find_element(AppiumBy.ID,"com.netdatasoft.android.divvydrive:id/KullaniciAdi").send_keys("demo10")
driver.find_element(AppiumBy.ID,"com.netdatasoft.android.divvydrive:id/KullaniciSifre").send_keys("1234567Abc.")

driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button").click()
driver.implicitly_wait(120)

driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button").click()
driver.implicitly_wait(120)

driver.quit()
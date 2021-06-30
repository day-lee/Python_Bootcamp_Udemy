from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

chrome_driver_path = "C:\dayeon2020\chromedriver.exe" #for mac: no .exe
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()

driver.get("https://tinder.com/")
time.sleep(4)

#login popup
login_btn = driver.find_element_by_xpath(
    "//*[@id='content']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]")
login_btn.click()
time.sleep(4)

facebook = driver.find_element_by_xpath("//*[@id='modal-manager']/div/div/div[1]/div/div[3]/span/div[2]/button")
facebook.click()
time.sleep(5)

#switch the window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

#fill in the login infomation
username = driver.find_element_by_xpath("//*[@id='email']")
username.send_keys("-")

password = driver.find_element_by_xpath("//*[@id='pass']")
password.send_keys("-")

login_btn = driver.find_element_by_xpath("//*[@id='loginbutton']")
login_btn.click()
time.sleep(3)

driver.switch_to.window(base_window)
print(driver.title)
time.sleep(4)

#Click ALLOW for location.
allow_location = driver.find_element_by_xpath("//*[@id='modal-manager']/div/div/div/div/div[3]/button[1]")
allow_location.click()
time.sleep(2)

#Click NOT INTERESTED for notifications.
no_notifications = driver.find_element_by_xpath("//*[@id='modal-manager']/div/div/div/div/div[3]/button[1]")
no_notifications.click()
time.sleep(2)

#Click I ACCEPT for cookies
accept_cookie = driver.find_element_by_xpath("//*[@id='content']/div/div[2]/div/div/div[1]/button")
accept_cookie.click()
time.sleep(2)

#dislike bot
# for i in range(5):
#     hit_dislike_btn = driver.find_element_by_xpath(
#     "//*[@id='content']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button")
#     hit_dislike_btn.click()
#     time.sleep(3)
#     print("I disliked this girl.")

#like bot
for i in range(5):
    try:
        hit_like_btn = driver.find_element_by_xpath(
            "//*[@id='content']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button")
        hit_like_btn.click()
        print("I like this girl.")
        time.sleep(2)

    except NoSuchElementException:
        time.sleep(2)
        hit_x = driver.find_element_by_xpath("// *[ @ id = 'modal-manager'] / div / div / button[2]")
        hit_x.click()

    except ElementClickInterceptedException:
        time.sleep(2)
        hit_x = driver.find_element_by_xpath("// *[ @ id = 'modal-manager'] / div / div / button[2]")
        hit_x.click()

# driver.quit()

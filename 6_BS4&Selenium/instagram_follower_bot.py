import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

CHROME_DRIVER_PATH = "C:\-\chromedriver.exe"
SIMILAR_ACCOUNT = "c"
IG_USER = "d-"
IG_PASSWORD = "-"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        user_id = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        user_id.send_keys(IG_USER)
        password.send_keys(IG_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        popup_x = self.driver.find_element_by_css_selector(
            "body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm")
        popup_x.click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        # self.driver.get("https://www.instagram.com/twizted_up/")

        click_followers = self.driver.find_element_by_xpath(
            "//*[@id='react-root']/section/main/div/header/section/ul/li[2]")
        click_followers.click()
        time.sleep(3)
        follow_btn = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[1]")
        follow_btn.click()
        time.sleep(3)

        #find all li elements in list
        try:
            while True:
                follower_popup = self.driver.find_element_by_xpath("//div[@class='isgrP']")
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_popup)

        except ElementClickInterceptedException:
            cancel_btn = self.driver.find_element_by_xpath("//button[contains(.,'팔로우 취소')]")
            self.driver.execute_script("arguments[0].click();", cancel_btn)


#__________________________________________________________________________
        # follower_popup_list = self.driver.find_elements_by_xpath("//div[@class='isgrP']//li")
        # print("follower_popup_list len is {}".format(len(follower_popup_list)))
        # print("ended")


    def follow(self):
        buttons = self.driver.find_elements_by_xpath("//button[contains(.,'팔로우')]")
        for btn in buttons:
            # Use the Java script to click on follow because after the scroll down
            # the buttons will be unclickeable unless you go to it's location
            self.driver.execute_script("arguments[0].click();", btn)
            time.sleep(3.5)


bot = InstaFollower()
bot.login()
bot.find_followers()
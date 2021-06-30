from selenium import webdriver
import time

PROMISED_DOWN = 1000
PROMISED_UP = 500
CHROME_DRIVER_PATH = "\chromedriver.exe"
TWITTER_EMAIL = "-@gmail.com"
TWITTER_PASSWORD = "-"
id = "L"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_driver_path = CHROME_DRIVER_PATH
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP
        self.speed = self.get_internet_speed()

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        # hit GO
        go = self.driver.find_element_by_css_selector("div.start-button")
        go.click()
        time.sleep(70)

        # get speed checked
        down = self.driver.find_element_by_class_name("download-speed")
        up = self.driver.find_element_by_class_name("upload-speed")
        print(f"down: {down.text}")
        print(f"up: {up.text}")
        return {"down": f"{down.text}", "up": f"{up.text}"}

    def tweet_at_provider(self, down, up):
        self.driver.get("https://twitter.com/")
        time.sleep(10)

        # hit GO
        go = self.driver.find_element_by_link_text("로그인")
        go.click()
        time.sleep(3)

        # login
        email = self.driver.find_element_by_name("session[username_or_email]")
        email.send_keys(TWITTER_EMAIL)
        password = self.driver.find_element_by_name("session[password]")
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(3)

        login = self.driver.find_element_by_xpath(
            "//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[3]")
        login.click()
        time.sleep(5)

        # 2 2nd login for verification
        email_2 = self.driver.find_element_by_name("session[username_or_email]")
        email_2.send_keys(id)
        password_2 = self.driver.find_element_by_name("session[password]")
        password_2.send_keys(TWITTER_PASSWORD)
        time.sleep(3)

        login_2 = self.driver.find_element_by_xpath(
            "//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[3]")
        login_2.click()
        time.sleep(5)

        # write
        write = self.driver.find_element_by_xpath(
            "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]"
            "/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div")
        write.send_keys(
            f"Hey Internet Provider, why is my internet speed {down} down/ {up} up, When I pay for {self.down}/ {self.up}?")
        time.sleep(10)
        tweet = self.driver.find_element_by_xpath(
            "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]"
            "/div[4]/div/div/div[2]/div[3]/div/span/span")
        tweet.click()


bot = InternetSpeedTwitterBot()
bot.tweet_at_provider(down=bot.speed["down"], up=bot.speed["up"])
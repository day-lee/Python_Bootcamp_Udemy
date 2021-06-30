from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path = "C:\dayeon2020\chromedriver.exe" #for mac: no .exe
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=105149562&"
           "keywords=Python%20developer&location=%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD")
time.sleep(4)

login_btn = driver.find_element_by_xpath("/html/body/div[3]/a[1]")
login_btn.click()

username = driver.find_element_by_id("username")
username.send_keys("testpythondy@gmail.com")
password = driver.find_element_by_id("password")
password.send_keys("this is for password")

login_click_btn = driver.find_element_by_xpath("//*[@id='app__container']/main/div[2]/form/div[3]")
login_click_btn.click()
time.sleep(2)

#-------------------------------------job apply--------------------------------

next_co = driver.find_elements_by_css_selector("section.jobs-search__left-rail ul li a.job-card-list__title")
for company in next_co:
    # co = driver.find_elements_by_css_selector("li .a job-card-list__title")
    company.click()
    time.sleep(5)

    driver.find_element_by_css_selector(".jobs-apply-button--top-card button").click()  # easy_apply
    time.sleep(2)

    #driver.find_element_by_css_selector(".display-flex button")
    try:
        send_btn = driver.find_element_by_css_selector(".display-flex button.artdeco-button--primary")
        # send_btn.click()
        # time.sleep(3)

        x_btn = driver.find_element_by_class_name("mercado-match")
        x_btn.click()
        time.sleep(3)

        xx_btn = driver.find_element_by_css_selector(".artdeco-modal__actionbar button.artdeco-button--primary")
        xx_btn.click()
        time.sleep(3)
        print(f"{company.text} applied")
        print("-------------------------")

    except NoSuchElementException:
        pass

driver.quit()
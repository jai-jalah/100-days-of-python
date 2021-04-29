from selenium import webdriver
from decouple import config
import time
from selenium.webdriver.common.keys import Keys

URL = "https://www.linkedin.com/jobs/search/?f_E=2%2C3&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&sortBy=R"
EMAIL = config("LINKEDIN_EMAIL")
PASS = config("LINKEDIN_PASS")

chrome_driver_path = "/Users/JaiJk/Projects/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)

sign_in_link = driver.find_element_by_link_text("Sign in")
sign_in_link.click()

time.sleep(5)

cookie_pop_up = driver.find_element_by_xpath(
    '//*[@id="artdeco-global-alert-container"]/div[1]/section/div/div[2]/button[2]'
)
cookie_pop_up.click()

email_field = driver.find_element_by_id("username")
email_field.send_keys(EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(PASS)
password_field.send_keys(Keys.ENTER)

save_button = driver.find_element_by_class_name(
    "jobs-save-button artdeco-button artdeco-button--3 artdeco-button--secondary"
)
job_list = driver.find_elements_by_css_selector(".job-card-container--clickable")
for job in job_list:
    job.click()
    time.sleep(2)
    save_button.click()
    time.sleep(2)

from selenium import webdriver

URL = "https://www.linkedin.com/jobs/search/?f_E=2%2C3&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&sortBy=R"

chrome_driver_path = "/Users/JaiJk/Projects/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)

sign_in_link = driver.find_element_by_link_text("Sign in")
sign_in_link.click()
from selenium import webdriver

chrome_driver_path = "/Users/JaiJk/Projects/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")

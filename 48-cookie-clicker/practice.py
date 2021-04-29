from selenium import webdriver

chrome_driver_path = "/Users/JaiJk/Projects/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get(
#     "https://www.amazon.co.uk/Basketball-Elastic-Cushioning-Lightweight-Trainers/dp/B07KW1GBLR/ref=sr_1_6?dchild=1&keywords=basketball+shoes&qid=1619626899&sr=8-6"
# )
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

driver.get("https://www.python.org/")
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# doc_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(doc_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# menu_contents = driver.find_element_by_xpath(
#     '//*[@id="content"]/div/section/div[2]/div[2]/div/ul'
# )
# menu_contents = menu_contents.text
# print(menu_contents)

# event_times = driver.find_elements_by_css_selector(".event-widget time")
# event_names = driver.find_elements_by_css_selector(".event-widget li a")
# events = {}

# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text,
#     }

# print(events)

driver.quit()
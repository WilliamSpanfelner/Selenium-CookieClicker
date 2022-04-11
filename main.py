from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/william/Developer/Python/chromedriver"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

# Test that a connection can be made to a known web address
# url = "https://www.amazon.com"

# url = "https://www.amazon.com/BZLSFHZ-Ergonomic-Adjustable-Headrest-Breathable/dp/B09MB1QT4G/ref=sr_1_206?crid" \
#             "=1BTMETGBD2VVO&keywords=chairs+for+desk&qid=1649319961&sprefix=chairs%2Caps%2C394&sr=8-206 "
# driver.get(url)
#
# content = driver.find_element(By.CLASS_NAME, "a-offscreen")
# formatted_price = content.get_attribute("innerHTML")
# price = formatted_price.split("$")[1].replace(",", "")
# print(price)
#
# title = driver.find_element(By.ID, "productTitle").get_attribute("innerHTML").strip()
# print(title)

url = "https://www.python.org/"
driver.get(url)
# Deprecation warning
# search_bar = driver.find_element_by_name("q")
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
#
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)
# print(logo.get_attribute("alt"))
#
# documents_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documents_link.text)
#
# report_bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(report_bug_link.text)

events_dict = {}

events_list = driver.find_elements(By.XPATH, '/html/body/div/div[3]/div/section/div[3]/div[2]/div/ul/li')
for i in range(len(events_list)):
    event_date = events_list[i].find_element(By.TAG_NAME, "time").text
    event_title = events_list[i].find_element(By.TAG_NAME, "a").text
    print(event_date, event_title)
    events_dict[i] = {'date': event_date, 'name': event_title}

print(events_dict)

angelas_events_dict = {}
angela_events = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
angela_events_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
for time in angela_events:
    print(time.text)

for name in angela_events_names:
    print(name.text)

for i in range(len(angela_events)):
    angelas_events_dict[i] = {
        'date': angela_events[i].text,
        'name': angela_events_names[i].text
    }

print(angelas_events_dict)

driver.quit()

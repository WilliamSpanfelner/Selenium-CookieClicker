from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/william/Developer/Python/chromedriver"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

url = "https://en.wikipedia.org/wiki/Main_Page"

driver.get(url)
# article_count = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div/div[3]/a[1]')
# article_count = driver.find_element(By.ID, "articlecount")
# count = article_count.get_attribute("Special:Statistics")
# print(article_count.text)
# article_count.click() - produces error

# Click the article_count link
angelas_article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(angelas_article_count.text)
# angelas_article_count.click() # - no error noted

# Click the All portals link
# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# all_portals.click()

# Enter a search term in the Search Wikipedia search bar.
# To send the ENTER key requires the Keys import above.
search = driver.find_element(By.ID, "searchInput")
search.send_keys("Python")
search.send_keys(Keys.ENTER)


# driver.quit()

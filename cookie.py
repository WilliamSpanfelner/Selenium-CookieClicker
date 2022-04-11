from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from timer import Timer


def cookie_rating(cookies_made):
    """Returns the rate of cookie production"""
    cookie_rate = cookies_made.text.split("\n").pop()
    return cookie_rate


def check_for_upgrades():
    """Returns a list of upgrade ids available for purchase"""

    # Upgrades are automatically enabled by the number of cookies made.
    # This means that the clickable elements can be located by a partial
    # id and the .product.unlocked.enabled classes - additionally, upgrades
    # cannot be purchased without the cookies. All upgrades can be located
    # as follows.
    upgrades = driver.find_elements(By.CSS_SELECTOR, "div[id^=product].product.unlocked.enabled")

    # Get the ids of the upgrades items using list comprehension
    upgrade_ids = [upgrade.get_attribute('id') for upgrade in upgrades]
    print(f"upgrade_ids: {upgrade_ids}")
    return upgrade_ids


def buy_best_upgrade_from(upgrade_ids):
    # Ensure the upgrade_ids list is not empty, otherwise return
    if len(upgrade_ids) > 0:
        # Get the last item in the list which will also
        # have the greatest value
        best_upgrade_id = upgrade_ids.pop()

        # Using the best_upgrade_id purchase it by clicking the element
        purchase_upgrade = driver.find_element(By.ID, best_upgrade_id)
        purchase_upgrade.click()
        print(f"Purchased upgrade: {best_upgrade_id}")
    else:
        return


t = Timer()

chrome_driver_path = "/Users/william/Developer/Python/chromedriver"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

url = "https://orteil.dashnet.org/cookieclicker/"

driver.get(url)

cookie = driver.find_element(By.ID, "bigCookie")
cookies_made = driver.find_element(By.ID, "cookies")

total_etime = 5 * 60
t.start()

while total_etime > 0:
    cookie.click()
    e_time = t.elapsed_time()
    if e_time > 5:
        total_etime -= e_time
        t.stop()
        upgrade_list = check_for_upgrades()
        buy_best_upgrade_from(upgrade_list)
        t.start()

print(f"cookies/second: {cookie_rating(cookies_made)}")
driver.quit()

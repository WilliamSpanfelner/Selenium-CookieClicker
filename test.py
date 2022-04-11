from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from timer import Timer

t = Timer()

chrome_driver_path = "/Users/william/Developer/Python/chromedriver"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

url = "https://orteil.dashnet.org/cookieclicker/"

driver.get(url)
cookie = driver.find_element(By.ID, "bigCookie")
cookies_made = driver.find_element(By.ID, "cookies")
cookie_rate = cookies_made.text.split("\n").pop()

total_etime = 5 * 60
t.start()

while total_etime > 0:
    cookie.click()
    e_time = t.elapsed_time()

    if e_time > 5:
        total_etime -= e_time
        t.stop()

        # upgrades = driver.find_elements(By.CSS_SELECTOR, "#store")
        upgrades = driver.find_elements(By.CSS_SELECTOR, "div[id^=product].product.unlocked.enabled")
        upgrade_ids = [upgrade.get_attribute('id') for upgrade in upgrades]
        print(f"upgrade_ids: {upgrade_ids}")

        if len(upgrade_ids) > 0:
            best_upgrade_id = upgrade_ids.pop()
            print(f"best_upgrade_id: {best_upgrade_id}")

            purchase_best_upgrade = driver.find_element(By.ID, best_upgrade_id)
            purchase_best_upgrade.click()

            print(f"Purchased upgrade: {best_upgrade_id}")

        t.start()

print(f"cookies/second: {cookie_rate}")
driver.quit()

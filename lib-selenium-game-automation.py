from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")


def get_highest_reward_element(elements):
    for i in range(len(elements)):
        if len(elements[i].get_attribute("class")) == 0 and i != 0:
            return elements[i-1]
    return None

# compute the time 5 seconds from the current time
cookie = driver.find_element(By.ID, "cookie")
reward_ids = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment", "buyAlchemy lab", "buyPortal", "buyTime machine", "buyElder Pledge"]
# print(cursor.get_attribute("class"))
for _ in range(60):
    time_later = time.time() + 5
    while time.time() <= time_later:
        cookie.click()
        money_element = driver.find_element(By.ID, "money").text
        # print(money)
    reward_elements = [driver.find_element(By.ID, reward_id) for reward_id in reward_ids]
    highest_element = get_highest_reward_element(reward_elements)
    if highest_element is not None:
        highest_element.click()
cps_element = driver.find_element(By.ID, "cps").text
cps = float(cps_element.split(":")[1].strip())
print(cps)
# print(cursor.get_attribute("class"))

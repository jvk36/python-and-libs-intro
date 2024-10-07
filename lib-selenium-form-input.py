from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

# click on a link after finding the element based on link text
# all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()
# driver.maximize_window()

first_name_element = driver.find_element(By.NAME, "fName")
first_name_element.send_keys("John", Keys.ENTER)
last_name_element = driver.find_element(By.NAME, "lName")
last_name_element.send_keys("Vincent", Keys.ENTER)
email_element = driver.find_element(By.NAME, "email")
email_element.send_keys("JohnKonnayilVincent@gmail.com", Keys.ENTER)

# signup_button = driver.find_element(By.TAG_NAME, "button")
signup_button = driver.find_element(By.CSS_SELECTOR, "form button")
signup_button.click()

from selenium import webdriver
from selenium.webdriver.common.by import By

#******* SCRAPES THE UPCOMING EVENTS FROM python.org WEBSITE ************

# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# NOTE: The XPATH supplied may have to be updated from the website by going through Chrome Inspect. 
menu_list_ul = driver.find_element(By.XPATH,"//*[@id='content']/div/section/div[2]/div[2]/div/ul")
time_texts = [time.text for time in menu_list_ul.find_elements(By.TAG_NAME, "time")]
# print(time_texts)
name_texts = [name.text for name in menu_list_ul.find_elements(By.TAG_NAME, "a")]
# print(name_texts)
# event_data = {}
# for i in range(len(time_texts)):
#     event_data[i] = {"time": time_texts[i], "name": name_texts[i]}

event_data = {i: {"time": time_texts[i], "name": name_texts[i]} for i in range(len(time_texts))}
print(event_data)

# input()

# driver.close()
driver.quit()

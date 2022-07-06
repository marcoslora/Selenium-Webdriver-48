from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/ml/Documents/Development/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")
# count_wiki = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# count_wiki.click()
# print(count_wiki.text)
# all_portals = driver.find_element(By.LINK_TEXT, "Contributions")
# all_portals.click()

f_name = driver.find_element(By.NAME, "fName")
f_name.send_keys("Marcos")
l_name = driver.find_element(By.NAME, "lName")
l_name.send_keys("Lora")
email = driver.find_element(By.NAME, "email")
email.send_keys("marcoslsfasf@asdasd.com")
submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()
# email.send_keys(Keys.ENTER)

# driver.quit()
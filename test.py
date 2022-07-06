import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "/Users/ml/Documents/Development/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.banreservas.com.do/TuBancoPersonas/Login.aspx?ReturnUrl=%2fTuBancoPersonas%2f")
# all_portals = driver.find_element(By.CLASS_NAME, "nav-link.nav-link-blue.tasacambio-ventaUS")
# print(all_portals.text)
search = driver.find_element(By.NAME, "ctl00$MainHolder$TextBoxUserName")
time.sleep(2)
search.send_keys("Python")
time.sleep(1)
search.send_keys(Keys.ENTER)
search1 = driver.find_element(By.NAME,"ctl00$MainHolder$Password")
time.sleep(1)
search1.send_keys("sdsdsdsds")
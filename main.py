from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path = "/Users/ml/Documents/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get("https://camelcamelcamel.com/product/B09HDYYXGX")
# driver.get("https://www.python.org/")
driver.get("https://www.banreservas.com/")
# price = driver.find_element(By.CLASS_NAME, "green")
test = driver.find_element(By.CLASS_NAME, "nav-link nav-link-blue tasacambio-compraUS".replace(" ", "."))
test = test.text
test = test.split()
print(test[1])

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# documentation = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation.text)

# xpath_test = driver.find_element(By.XPATH, "//*[@id='container']/li[3]/ul/li[7]/a")
# print(xpath_test.text)
# events_dict = {}
# events_name = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# events_time = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# for n in range(len(events_time)):
#     events_dict[n] = {
#         "time": events_time[n].text,
#         "name": events_name[n].text
#     }
# print(events_dict)
# driver.close()
driver.quit()
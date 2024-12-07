import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()

url="http://github.com"

driver.get(url)


searchInput=driver.find_element(By.NAME,"q")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(1)
result=driver.find_elements_by_css_selector(".repo-list-item h3 a")

for element in result:
    print(element.text)

driver.close()
import time


from selenium import webdriver

driver=webdriver.Chrome()

url="http://github.com"
driver.get(url)

time.sleep(2)
driver.maximize_window()
driver.save_screenshot("github.com+homepage.png")

url="http://github.com/sadikturan"
driver.get(url)

print(driver.title)

if "sadikturan" in driver.title:
    driver.save_screenshot("github-sadikturan.png")

time.sleep(2)
driver.back()
time.sleep(2)
driver.close()
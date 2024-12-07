import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from twitterUserInfo import password, username

    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_argument('--lang=en,en_US')
        self.browser = webdriver.Chrome('chromedriver.exe', options=self.browserProfile)
        self.username = username
        self.password = password
        
    def signIn(self):
        self.browser.get("https://twitter.com/i/flow/login")
        time.sleep(2)  
        
        usernameInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label")
        
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        
        btnSubmit = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div")
        btnSubmit.click()
        
        time.sleep(2)
        
twitter = Twitter(username, password)    
# Giriş yap
twitter.signIn()

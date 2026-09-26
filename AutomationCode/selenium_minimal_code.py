import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# service = Service("/path/to/chromedriver")  # user this if you are using downloaded Chrome Driver
# for modern selenium have Selenium Manager and which automatically download appropriate driver and launch browser
options = Options()
# options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
options.add_argument("--incognito")
options.add_argument("--start-maximized")
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")
search = driver.find_element(By.NAME, "q")
search.send_keys("Selenium Python")
search.submit()
driver.quit()

'''
Service
   ↓
Which WebDriver should Selenium use?
        ↓
    ChromeDriver

Options
   ↓
How should Chrome be launched?
        ↓
    Chrome  
'''

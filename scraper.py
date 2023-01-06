from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
    #Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options = options)
    url = "http://automated.pythonanywhere.com/login/"
    driver.get(url)
    return driver
def clean_text(text):
    """"Extract only the temperature from text"""
    output =float( text.split(": ")[-1])
    return output

def main():
    driver = get_driver()

    # Find and fill in username and password
    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(2)
    print(driver.current_url)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)

    # Click on Home link and wait 2 sec
    print(driver.current_url)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    time.sleep(2)
    print(driver.current_url)
    # Scrape the temperature value
    text = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]").text
    return clean_text(text)
print(main())

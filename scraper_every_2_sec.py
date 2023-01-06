from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt

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
    url = "http://automated.pythonanywhere.com/"
    driver.get(url)
    return driver

def clean_text(text):
    """"Extract only the temperature from text"""
    output =float( text.split(": ")[-1])
    return output

def write_temperature(temperature):
    # Get the current date
    now = dt.now()
    # Format the date as a string in the desired format
    date_string = now.strftime("%Y-%m-%d_%H-%M-%S")
    # Create the file name by concatenating the date string with '.txt'
    filename = date_string + '.txt'
    # Open the file in write mode
    file = open(filename, 'w')
    # Write some text to the file
    file.write(str(temperature))
    # Close the file
    file.close()

def main():
    driver = get_driver()

    # Scrape the temperature value
    while True:
        time.sleep(2)
        text = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]").text
        write_temperature(clean_text(text))

main()

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from playsound import playsound
import random

brave_path = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
# option.add_argument("--incognito") OPTIONAL
# option.add_argument("--headless") OPTIONAL

def move(x):
    driver.find_element_by_xpath(f"//div[@id=\"{x}\"]").click()
    sleep(0)
    check=driver.find_elements_by_xpath("//i[@class=\"fas fa-snowflake spicon spia\"]")
    if(len(check)==0):
        playsound('beep.mp3')
    else:
        print('Gotcha!')
        playsound('beep.mp3')
        playsound('beep.mp3')
        playsound('beep.mp3')
        playsound('beep.mp3')
        exit(0)
        #playsound('beep.mp3')


# Create new Instance of Chrome
driver = webdriver.Chrome(chrome_options=option)

driver.get("https://www.delugerpg.com/login")
sleep(1)
driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys("username")
sleep(1)
driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys("password")
sleep(1)
driver.find_element_by_xpath("//input[@name=\"Login\"]").click()
sleep(1)
driver.get("https://www.delugerpg.com/map/overworld20")
dirs=['dr-nw','dr-n','dr-ne','dr-e','dr-se','dr-s','dr-sw','dr-w']

while(1):
    val=random.randint(0,len(dirs)-1)
    direction=dirs[val]
    move(direction)

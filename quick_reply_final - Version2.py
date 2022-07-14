from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:8080")
#Change chrome driver path accordingly
chrome_driver = "C:\\Users\\anush\\Downloads\\Harsha\\Class\\Py\\Bot\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
print(driver.title)

def ping(msg,sal):
    check = driver.find_elements_by_xpath("//textarea[@name=\"chatTextInput\"]")
    #click = driver.find_elements_by_xpath("//div[@data-tooltip=\"Chat with everyone\"]")
    if(len(check)==0):
        driver.find_element_by_xpath("//div[@data-tooltip=\"Chat with everyone\"]").click()
        #check[0].click()
        chat = driver.find_element_by_xpath("//textarea[@name=\"chatTextInput\"]")
        chat.send_keys("{} {} {}".format(msg,sal,Keys.ENTER))
    else:
        chat = driver.find_element_by_xpath("//textarea[@name=\"chatTextInput\"]")
        chat.send_keys("{} {} {}".format(msg,sal,Keys.ENTER))

sal=input("Enter Sir/Madam:") #enter sir or madam
list = ["Okay","Clear","Yes","No","Continue"]
while(1):
    choice = int(input("Enter Choice:"))
    msg=list[choice-1]
    ping(msg,sal)

#chrome.exe -remote-debugging-port=8080 --user-data-dir="C:\Users\anush\Download\Harsha\Class\Py\Bot\v2"

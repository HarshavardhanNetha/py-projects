from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


options = Options()
options.add_argument('--user-data-dir=C:\\Users\\Harsha\\Desktop\\wassapBot\\data')
#options.add_argument('--headless')
#Change chrome driver path accordingly
driver = webdriver.Chrome(options=options)

driver.get("https://web.whatsapp.com")

print(driver.title)
try:
    # wait 10 seconds before looking for element
    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "_1XaX-")))
finally:
    try:
        
        driver.execute_script("document.body.style.zoom='100%'")
        #msg_area[0] -> search bar
        #msg_area[1] -> msg typing bar

        chat = driver.find_elements_by_xpath("//div[@class=\"TbtXF\"]")


        for i in chat:
            #cnt+=2
            #print(i.text,"\n",end = "\n")
            temp = i.text.split()
            #print(temp)
            
            if(len(temp)!=0 and temp[-1].isnumeric()):
                if('bday' in temp or 'Happy' in temp or 'Birthday' in temp or 'birthday' in temp or 'happy' in temp or 'hpy' in temp or 'bornday' in temp):
                    print(temp)
                    #sleep(1)
                    #chat_click[cnt].click()
                    i.click()
                    #driver.execute_script("arguments[0].click();",i)
                    #sleep(1)
                    msg_area = driver.find_elements_by_xpath("//div[@class=\"_2_1wd copyable-text selectable-text\"]")
                    
                    #msg_area[1].click()
                    msg_area[1].send_keys("Thank you very much. :)",Keys.ENTER)
        driver.quit()
    except Exception as e:
        print(e)
        driver.quit()
        
        
    '''for i in chat():
        if("bday" in i.text):
            i.click()
            msg_area[1].click()
            msg_area[1].send_keys("ANY TEXT HERE",Keys.ENTER)
            
#to get messages after clcking any chat
msgs = driver.find_elements_by_xpath("//div[@class=\"_1bR5a\"]")

['Happy','happy','hpy',]
            
    '''
    


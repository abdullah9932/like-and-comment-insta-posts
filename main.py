from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests as req
import os
import sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui



grinning_face="\U0001F600"	
smiley_with_teeth="\U0001F601"	
smile="\U0001F642"	
smiling_with_heart_eyes="\U0001F60D"
heart="\U0001F497"
thumbsup="\U0001F44D"
File = 'urls.txt'
nooflinks=60
Username = ''
Password = ''
browser='firefox'
commenttxt=emoji.emojize("nice"+heart)
commenting='ON'
i=0

def likepost(driver):
    global commenttxt,commenting,i
    sleep(5)
    driver.find_element_by_xpath('/html/body/div/section/main/div/div/article/div[2]/section[1]/span[1]/button').click()
    print("liked")
    SCROLL_PAUSE_TIME = 1
    last_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(SCROLL_PAUSE_TIME)
    if commenting=='ON':
        try:
            driver.find_element_by_css_selector(".Ypffh").click()
            comment_box = ui.WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".Ypffh")))
            comment_box.send_keys(commenttxt)
            sleep(2)
            comment_box.send_keys(Keys.RETURN)
            i+=1
            print('commented'+str(i))
            sleep(2)
        except:
            print("Commenting is disabled"+str(i))
    else:
        sleep(2)

def Linkfile(i,driver):
    with open(File) as Links:
       Link = Links.readlines()[i]
       print (Link)
       driver.get(Link)
       likepost(driver); 
       sleep(4)
    

def main():
    global nooflinks
    global browser,commenttxt
    if browser=='firefox':
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.cache.disk.enable", False)
        profile.set_preference("browser.cache.memory.enable", False)
        profile.set_preference("browser.cache.offline.enable", False)
        profile.set_preference("network.http.use-cache", False) 
        driver =webdriver.Firefox(profile)
       
    if browser=='chrome':
        driver=webdriver.Chrome()
    try:
        sleep(2)
        driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        sleep(3)
        driver.find_element_by_name('username').send_keys(Username)
        driver.find_element_by_name('password').send_keys(Password)
        driver.find_element_by_name('password').send_keys(Keys.RETURN)
        sleep(8)
    except:
        pass
    for i in range(0,nooflinks):
        Linkfile(i,driver);
                 
if __name__ == "__main__":
    main()


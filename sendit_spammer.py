# imports and installs

import os
os.system("pip install selenium")
os.system("pip install keyboard")
os.system("pip install urllib3")
from selenium import webdriver
import time
import keyboard
index = 0
os.system("cls")
# sendit url
url = input("sendit url : ")

# ask for message here
message = input("your message : ")



# main code

while True:
        index +=1
        try:
                # open chromedrive / get url
                driver = webdriver.Chrome("chromedriver.exe")
                driver.get(url)
                time.sleep(2)
                # find the buttons and type the message
                driver.find_element_by_xpath("""/html/body/div/div[3]/div/div[1]/div[2]/form""").click()
                keyboard.write(message)
                driver.find_element_by_xpath("""/html/body/div/div[3]/div/div[2]/div/div[2]""").click()
                time.sleep(1)
                driver.quit()
        except:
                #error exception
                print("error")
                driver.quit()
                pass
        # tell you how many time you have spammed
        print("\r" + f"sendit spammed {index} times", end="")
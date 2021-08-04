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
# open chromedrive / get url
driver = webdriver.Chrome("chromedriver.exe")
driver.get(url)
# main code
time.sleep(1)
while True:
        index +=1
        try:

                time.sleep(1)
                # find the buttons and type the message
                driver.find_element_by_xpath("""/html/body/div/div[3]/div/div[1]/div[2]/form""").click()
                keyboard.write(message)
                driver.find_element_by_xpath("""/html/body/div/div[3]/div/div[2]/div/div[2]""").click()
                time.sleep(1)
                driver.refresh()
                # tell you how many time you have spammed
                print("\r" + f"sendit spammed {index} times", end="")
        except Exception as e:
                #error exception
                print(e)
                print("error")
                driver.quit()
                driver = webdriver.Chrome("chromedriver.exe")
                time.sleep(1)
                pass


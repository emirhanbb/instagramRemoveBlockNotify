from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime


yourInstagramUsername = "username"
yourInstagramPassword = "pass"

checkInstagramUsername = "The instagram account to check out username"

f = open("data.txt", "a")

driver = webdriver.Chrome()
driver.get("https://www.instagram.com")
sleep(3)

driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(yourInstagramUsername)
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(yourInstagramPassword)
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]").click()

sleep(6)
#driver.find_element_by_xpath("/html/body/div[1]/div/div/section/main/div/div/div/div/button").click()
driver.find_element_by_class_name("sqdOP").click()
sleep(4)
driver.find_element_by_class_name("aOOlW.HoLwm").click()
sleep(3)

counter = 0


while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    driver.find_element_by_class_name("XTCLo.x3qfX").clear()
    sleep(3)
    driver.find_element_by_class_name("XTCLo.x3qfX").send_keys(checkInstagramUsername)
    users = driver.find_elements_by_class_name("_7UhW9.xLCgt.MMzan.KV-D4.fDxYl")
    for i in users:
        if i.text == checkInstagramUsername:
            counter = 1
    if counter == 0:
        f.write("BLOCK " + current_time + "\n")
    else:
        f.write("UNBLOCK " + current_time + "\n")
        print("UNBLOCK " + current_time)
        counter = 0

    sleep(25)





driver.close()

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
# Replace below path with the absolute path of the \
#chromedriver in your computer
driver = webdriver.Chrome(r'D:\chromedrive\chromedriver')

driver.get("https://web.whatsapp.com/")
# time.sleep()
wait = WebDriverWait(driver, 600)
# Replace 'My Bsnl' with the name of your friend or group name
target = '"Icecream Premis"'

# Replace the below string with your own message
string = sys.argv[1]

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
By.XPATH, x_arg)))
print (group_title)
print ("Wait for few seconds")
group_title.click()
message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
for i in range(0,15000):
    message.send_keys(string)
    sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
    sendbutton.click()
driver.close()
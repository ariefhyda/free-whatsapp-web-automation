from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException  
import time 
import pandas as pd
import os

# Replace below path with the absolute path
# to chromedriver in your computer
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# for login session
options.add_argument("user-data-dir=C:\\Users\\hyda\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
driver = webdriver.Chrome(executable_path='C:/Python/wa/whatsappmessagepython/chromedriver.exe',chrome_options=options)
# to rediect to WA web
driver.get("https://web.whatsapp.com")
wait = WebDriverWait(driver, 600)

if os.path.exists("failed_log.txt"):
    os.remove("failed_log.txt")


# Replace excel file path
df = pd.read_excel('bulk.xlsx')
filepath="C:/Python/wa-send/"

# function to check  
def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

input('Enter anything after scaning QRCODE or after web is READY')


for index, row in df.iterrows():
    
    # without extension wa web plus    
    # redirect to wa me 
    # driver.get("https://web.whatsapp.com/send?phone="+str(row['phone_number']))
    # wait = WebDriverWait(driver, 600)
    # time.sleep(10)

    # with extension wa web plus (https://wawplus.com/en/)
    new_chat= driver.find_element_by_xpath('//div[@id="startNonContactChat"]')
    new_chat.click()
    time.sleep(1)

    input_contact= driver.find_element_by_xpath('//input[@placeholder="Phone number"]')
    input_contact.send_keys(str(row['phone_number']))
    time.sleep(1)

    start_new_chat = driver.find_element_by_xpath('//a[@class="btn-ok"]')
    start_new_chat.click()
    time.sleep(5)

    if(check_exists_by_xpath('//div[@data-animate-modal-body="true"]')==False):
        attachment_box= driver.find_element_by_xpath('//div[@title="Attach"]')
        attachment_box.click()

        file_box= driver.find_element_by_xpath('//input[@accept="*"]')
        file_box.send_keys(filepath+str(row['file']))
        # if your file is large, add the time below
        time.sleep(4)
        send_button_file = driver.find_element_by_xpath('//span[@data-icon="send"]')
        send_button_file.click()

        message_box = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
        message_box.send_keys("Thanks from hyda. Cheers!")

        message_button = driver.find_element_by_xpath('//button[@class="_1E0Oz"]')
        message_button.click()
        print("Success : " +str(row['phone_number'])+"=>"+str(row['file']))
        # if your file is large, add the time below
        time.sleep(3)
    else:
        print("invalid number : " +str(row['phone_number'])+"=>"+str(row['file']))
        file1 = open("failed_log.txt","a")
        file1.writelines(str(row['phone_number']))
        file1.writelines("\n")

        btn_close= driver.find_element_by_xpath('//div[@class="VtaVl -TvKO"]')
        btn_close.click()
        time.sleep(2)



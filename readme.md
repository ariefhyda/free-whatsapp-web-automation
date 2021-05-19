# FREE Whatsapp auto send text and file

This program is used to make it easier to perform automatic submissions without using an API

You can choose by using the Whatsapp link (https://web.whatsapp.com/send?phone=) or using the chrome extension (https://wawplus.com/en/). I recommend using the extension.

## Requirment
- Python 
  - install selenium
  - install pandas
- WA web plus (https://wawplus.com/en/)
- Chrome driver (https://chromedriver.chromium.org/downloads). Download your driver according to your chrome version.

## With Whatsapp Link
You can uncomment line 43-45 and comment line 48-58
<pre>
#redirect to wa me 
driver.get("https://web.whatsapp.com/send?phone="+str(row['phone_number']))
wait = WebDriverWait(driver, 600)
time.sleep(10)
</pre>

## With Extension
You can uncomment line 48-58 and comment line 43-45
<pre>
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
</pre>

don't forget to check 'Enable start conversation with non contancts' in WA Web Plus



## Conclusion
If you are still confused, you can contact me on email : arifhidayah22@gmail.com


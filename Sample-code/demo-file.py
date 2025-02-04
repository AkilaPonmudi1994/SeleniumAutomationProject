from selenium import webdriver
from selenium.webdriver.common.by import By
import time

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
driver.implicitly_wait(3)

#Login to the application
user_name=driver.find_element(By.NAME,'username')
user_name.send_keys("Admin")
password=driver.find_element(By.NAME,'password')
password.send_keys("admin123")
login_button=driver.find_element(By.XPATH,"//button[@type='submit']")
login_button.click()
time.sleep(1)
#Adding new admin - TC-001
admin_tab=driver.find_element(By.LINK_TEXT,'Admin')
admin_tab.click()
username_textbox=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input")
username_textbox.send_keys("Admin")
#driver.quit()

#locating svg element
#driver.find_element(By.XPATH,'//button[@title='My Timesheet']')
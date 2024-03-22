from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import undetected_chromedriver as uc

from datetime import datetime
import time
import re

from passwords import *


class gmail_work():
    
    def __init__(self, username, password, browser_off=True):
        self.username = username
        self.password = password
        options = Options()
        
        if browser_off:
            options.add_argument("--headless")
            
        # driver = uc.Chrome(options=options)
        driver = webdriver.Chrome(options=options)

        driver.get('https://www.gmail.com')

        username_find = driver.find_element(By.ID, 'identifierId')
        
        username_find.send_keys(username)
        
        username_find.send_keys(Keys.RETURN)
        time.sleep(3)

        password_find = driver.find_element(By.NAME, "Passwd")
        password_find.send_keys(PASSWORD)

        password_find.send_keys(Keys.RETURN)
        time.sleep(3)
        
        self.driver = driver

    def change_password(self, new_password):
        driver = self.driver
        driver.get('https://myaccount.google.com/signinoptions/password')
        time.sleep(3)
        new_password_find = driver.find_element(By.NAME, "password")
        new_password_find.send_keys(new_password)
        confirm_password_find = driver.find_element(By.NAME,"confirmation_password")
        confirm_password_find.send_keys(new_password)
        confirm_password_find.send_keys(Keys.RETURN)
        self.driver = driver
        return new_password

    def get_accounts_data(self):
        driver = self.driver
        driver.get('https://myaccount.google.com/personal-info')
        driver.refresh()
        full_name = re.search("\\n(\w+)\s(\w+)", driver.find_element(By.ID, "i11").text).groups()
        date_str = re.search("\\n(.*)", driver.find_element(By.ID, "i12").text).groups()[0]
        emails = re.search("\\n(.*)\\n(.*)", driver.find_element(By.ID, "i14").text).groups()
        dict_data = {
            'email': emails[0],
            'password': self.password,
            'first_name': full_name[0],
            'last_name': full_name[1],
            'birth_date': datetime.strptime(date_str, "%B %d, %Y").date(),
            'backup_email': emails[1],
            }
        self.driver = driver
        return dict_data

    def change_names(self, new_first_name, new_last_name):
        driver = self.driver
        driver.get('https://myaccount.google.com/profile/name/edit')
        time.sleep(3)
        first_name = driver.find_element(By.ID, "i6")
        first_name.clear()
        last_name = driver.find_element(By.ID, "i11")
        last_name.clear()
        first_name.send_keys(new_first_name)
        last_name.send_keys(new_last_name)
        button_save = driver.find_elements(By.TAG_NAME, "Button")[6]
        button_save.click()
        time.sleep(3)
        self.driver = driver
        return new_first_name, new_last_name
    
    def __del__(self):
        self.driver.quit()
    
class twitter_work():
    def __init__(self, username, password, browser_off=True):
        self.username = username
        self.password = password

        options = Options()
        
        if browser_off:
            options.add_argument("--headless")
            
        driver = webdriver.Chrome(options=options)

        driver.get('https://twitter.com/login')
        time.sleep(3)

        username_find = driver.find_element(By.TAG_NAME, 'input')
        
        username_find.send_keys(username)
        
        username_find.send_keys(Keys.RETURN)
        time.sleep(3)

        password_find = driver.find_elements(By.TAG_NAME, "input")[1]
        password_find.send_keys(PASSWORD)

        password_find.send_keys(Keys.RETURN)
        time.sleep(3)
        
        self.driver = driver

    def send_message(self, message):
        driver = self.driver
        driver.get("https://twitter.com/compose/post")
        time.sleep(3)
        focused_input = driver.switch_to.active_element
        focused_input.send_keys(message)
        
        action = ActionChains(driver)
        action.key_down(Keys.CONTROL)
        action.send_keys(Keys.RETURN)
        action.key_up(Keys.CONTROL)
        action.perform()
        
        time.sleep(2)
        self.driver = driver

    def __del__(self):
        self.driver.quit()
        
    



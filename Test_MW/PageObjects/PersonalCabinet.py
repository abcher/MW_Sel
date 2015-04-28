import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Base_Test_Case import TestBase

class PersonalCabinet():
    """Page object of Personal cabinet"""
    texts={}
    texts["Your login test"]="/html/body/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/a[1]"
    
      

      
    def open(self,driver,url):
         driver.get(url+"Extra/QuotedDynamic.aspx")
    def login(self,driver,login,password):
         print ("Begin login in Personal cabinet")
       
         driver.find_element_by_id("ctl00_Login_ctl01").send_keys(login)
         driver.find_element_by_id("ctl00_Login_ctl02").send_keys(password)
         driver.find_element_by_name("ctl00$Login$ctl03").click()
         wait = ui.WebDriverWait(driver, 50)
         element = wait.until(EC.presence_of_element_located((By.TAG_NAME,'a')))

         print ("Finish login in Personal cabinet") 

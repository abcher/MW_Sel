from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from QuotedDinamic import QuotedDinamic
import unittest, time, re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException






class TestBase(unittest.TestCase):
     """Base class for all test cases"""
     def setUp(self):
        self.driver = webdriver.Chrome()
      
        self.driver.implicitly_wait(50)
        testName = self.shortDescription()
        print (testName)

     
        
        #self.selbase_url = "http://wmwin8/MW/"
        self.selbase_url = "http://localhost/test1/"
        self.verificationErrors = []
        self.accept_next_alert = True 
        self.WormUp(self,self.driver,self.selbase_url)         
     def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

     def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
     def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
     def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
  #special methods to wait ajax calls using JQuery
  #usage: call AjaxWait(WebDriverInstance,TimeOut(default=10))
  #TBD not working -need to be tested
       
     def AjaxWait(self,driver,time=30):        
          WebDriverWait(driver, time).until(driver.execute_script("return jQuery.active"),  "Timeout waiting for page to load")

    
     @staticmethod
     def WormUp(self,driver,selbase_url,page=QuotedDinamic):
          page.open(self,driver,selbase_url)
          wait = ui.WebDriverWait(driver, 50)
          element = wait.until(EC.presence_of_element_located((By.ID,'ctl00_generalContent_QuotedDynamicControl_DynamicOffersFilter_btnSearch')))
        

 

       

           
    #def TearDown(self):
    #    self.driver.quit()
    #    print("end")



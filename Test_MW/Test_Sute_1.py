from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import sys
sys.path.append(os.getcwd()+"\PageObjects")
from PersonalCabinet import PersonalCabinet
from QuotedDinamic import QuotedDinamic
from Busket import Busket

import unittest, time, re
import Tools

from Test_Oracule import Oracule
from Base_Test_Case import TestBase
from Tools import DataGenerator


 

class TestMW_General(TestBase):
            
    """Main class to run tests on MW"""
    busket=Busket()
    quoted_dinamic=QuotedDinamic()
    personal_cabinet=PersonalCabinet()

    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    def __init__(self, methodName='runTest', Param=None,secondParam=None):
        super(TestMW_General, self).__init__(methodName)
        self.param = Param
        self.second_param=secondParam

    @staticmethod
    def parametrize(testcase_klass, param=None):
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(TestMW_General)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(TestMW_General(name, Param=param,secondParam=second_param))
        return suite


    
        #test methods
    def test_login_user(self):
        self.personal_cabinet.open(self.driver,self.selbase_url)
        self.personal_cabinet.login(self.driver,"test","1")
        time.sleep(2)
        #self.AjaxWait(self,self.driver)
        self.assertEqual("Ваш логин test", self.driver.find_element_by_xpath(PersonalCabinet.texts["Your login test"]).text)


    
        

    def test_find_price_in_QD(self):
       #page.price(self)
        
        self.quoted_dinamic.open(self.driver,self.selbase_url)
        self.quoted_dinamic.search(self.driver,"30.03.2020")
  
        
        time.sleep(2)

        self.assertEqual("800", self.driver.find_element_by_id(QuotedDinamic.price_values["price_1"]).text)
        #end total check at last
        Oracule.compare_table_objects(self,self.driver,'tbody','td','test_booking_ethalon.txt','test_booking_current.txt') 
        
        #time.sleep(20)
    def test_book_price(self):
          self.personal_cabinet.open(self.driver,self.selbase_url)
          self.personal_cabinet.login(self.driver,"test","1")
          time.sleep(2)
          self.quoted_dinamic.open(self.driver,self.selbase_url)
          self.quoted_dinamic.search(self.driver,self.param)  #"30.03.2020"
          #method that opens new tab
          self.quoted_dinamic.get_the_price(self.driver,QuotedDinamic.price_values["price_1"])          
          #get next tab
          self.driver.current_window_handle 
          currentHandle = set(self.driver.window_handles)
          currentHandle.remove(self.driver.current_window_handle)  
          self.driver.switch_to_window(currentHandle.pop())          
          self.busket.book_single_turist(self.driver,DataGenerator.generate_tourist_data(),self.second_param,"01","01","1980","123","456")

          time.sleep(5)
          #handle alert about no mail 
          alert = self.driver.switch_to_alert()
          alert.accept()
          time.sleep(2)
         
    #service methods    
if __name__ == "__main__":
    suite = unittest.TestSuite()

    suite.addTest(TestMW_General("test_find_price_in_QD"))
    suite.addTest(TestMW_General("test_login_user"))

    params=["30.03.2020","31.03.2020"]
    params2=["Ivan","Stepan"]

    #for paramtr in params:
    #    for paramtr2 in params2:
    #       suite.addTest(TestMW_General("test_book_price",Param=paramtr,secondParam=paramtr2))
    
    unittest.TextTestRunner(verbosity=2).run(suite)
    #unittest.main()


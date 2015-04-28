from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import Tools


class Oracule():

    def create_ethalon_table_object(self,driver,tagNameOuter,tagNameInner,ethalon_file_name):
        list_from_current = []
        Table=driver.find_elements(By.TAG_NAME, tagNameOuter)
        for x in Table:     
           try:list_from_current.append(x.find_elements(By.TAG_NAME, tagNameInner)[0].text)
           except:pass
        path_to_ethalon=os.getcwd() +'\\TableObjects\\Ethalon\\'+ ethalon_file_name
        Tools.TableObjectMaker.conserve(list_from_current,path_to_ethalon)

    def compare_table_objects(self,driver,tagNameOuter,tagNameInner,ethalon_file_name,current_file_name):
        list_from_current = []
        path_to_ethalon=os.getcwd() +'\\TableObjects\\Ethalon\\'+ ethalon_file_name
        path_to_current= os.getcwd() +'\\TableObjects\\Current\\'+ current_file_name
        Table=driver.find_elements(By.TAG_NAME, tagNameOuter)
        for x in Table:     
           try:list_from_current.append(x.find_elements(By.TAG_NAME, tagNameInner)[0].text)
           except:pass
        Tools.TableObjectMaker.conserve(list_from_current,path_to_current)
      
        list_ethalon=Tools.TableObjectMaker.open_conserve(path_to_ethalon)
        list_current=Tools.TableObjectMaker.open_conserve(path_to_current)
    
        self.assertEqual(list_ethalon, list_current , "Lists dont match")
  
        #for e in   listNewNew:
        # if not e in  listOld:
        #    self.fail(e+"  is not found")


       
          
    
        
       
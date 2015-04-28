from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import urllib




class QuotedDinamic(object):
    """Page object of QD"""
    price_values={}
    price_values["price_1"]="ctl00_generalContent_QuotedDynamicControl_DynamicOffersTable_DgPrices_ctl02_hlPrice"

    datapickers={}
    datapickers["DataZaezdaFrom"]="ctl00_generalContent_QuotedDynamicControl_DynamicOffersFilter_ctrlCalendar_TxtMultiDatepickerFrom"


    checkboxex={}
    checkboxex["CurrencyUE"]="ctl00_generalContent_QuotedDynamicControl_DynamicOffersFilter_currencySelector_curList_0"

    buttons={}
    buttons["BtnSearch"]="ctl00_generalContent_QuotedDynamicControl_DynamicOffersFilter_btnSearch"

   
        #for sorce_line in pizza_page:
            # print (sorce_line)
    
    def open(self,driver,url):
        driver.get(url+"Extra/QuotedDynamic.aspx")

    def search(self,driver,begin_date):
        print ("Begin search in QD")
        wait = ui.WebDriverWait(driver, 50)
        element1 = wait.until(EC.element_to_be_clickable((By.ID,self.datapickers["DataZaezdaFrom"])))
        driver.find_element_by_id(self.datapickers["DataZaezdaFrom"]).clear()
 
        driver.find_element_by_id(self.datapickers["DataZaezdaFrom"]).send_keys(begin_date)
        driver.find_element_by_id(self.checkboxex["CurrencyUE"]).click()
        wait = ui.WebDriverWait(driver, 50)
        element2 = wait.until(EC.element_to_be_clickable((By.ID,self.buttons["BtnSearch"])))
     
        driver.find_element_by_id(self.buttons["BtnSearch"]).click()
        print ("Finish search in QD")
    def get_the_price(self,driver,price_id):
       #ctl00_generalContent_QuotedDynamicControl_DynamicOffersTable_DgPrices_ctl02_hlPrice
        print("Click the price in QD to get in busket")
        driver.find_elements_by_id(price_id)[0].click()

    
#????????? ?????????? ???? ????? ????????? ????????
    #def price(self):
    #    url="http://wmwin8/MW/TourDates.aspx?priceKey=6482&date=2014-10-28&sid=durh2u5x3o1eh42wral1y5y5&src=local&rate=%d1%80%d0%b1"
    #    _page = urllib.request.urlopen(url)
    #    print(_page.read())
   
      
  


   

      

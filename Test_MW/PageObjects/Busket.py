import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Base_Test_Case import TestBase

class Busket():
    """Page object of Busket page"""

    inputs={}
    inputs["turist_family_id"]="ctl00_generalContent_BasketTourists_touristData_dgTourists_ctl02_txtLastName"
    inputs["turist_name_id"]="ctl00_generalContent_BasketTourists_touristData_dgTourists_ctl02_txtFirstName"
    inputs["birth_day_id"]="ctl00_generalContent_BasketTourists_touristData_dgTourists_ctl02_sdtBirthDate_txtDay"
    inputs["birth_month_id"]="ctl00_generalContent_BasketTourists_touristData_dgTourists_ctl02_sdtBirthDate_txtMonth"
    inputs["birth_year_id"]="ctl00_generalContent_BasketTourists_touristData_dgTourists_ctl02_sdtBirthDate_txtYear"
    inputs["passport_ser_id"]="ctl00_generalContent_BasketTourists_touristData_dgTourists_ctl02_pPassport_txtPassportSeries"
    inputs["passport_number_id"]="ctl00_generalContent_BasketTourists_touristData_dgTourists_ctl02_pPassport_txtPassportNumber"

    buttons={}
    buttons["Recalculate"]="ctl00_generalContent_BasketPrice_BtnCalculate"
    buttons["Book"]="ctl00_generalContent_BtnOrder"
   



    #def __init__(self):
    #    self.driver=driver
       
    #to get to busket we must switch windows
    def get_busket():
        pass

    def book_single_turist(self,driver,turist_family,turist_name,birth_day,birth_month,birth_year,passport_ser,passport_number):
        
         print("Begin book single tourist in Busket")
         driver.find_element_by_id(self.inputs["turist_family_id"]).send_keys(turist_family)
         driver.find_element_by_id(self.inputs["turist_name_id"]).send_keys(turist_name)
         driver.find_element_by_id(self.inputs["birth_day_id"]).send_keys(birth_day)
         driver.find_element_by_id(self.inputs["birth_month_id"]).send_keys(birth_month)
         driver.find_element_by_id(self.inputs["birth_year_id"]).send_keys(birth_year)
         driver.find_element_by_id(self.inputs["passport_ser_id"]).send_keys(passport_ser)
         driver.find_element_by_id(self.inputs["passport_number_id"]).send_keys(passport_number)

         driver.find_element_by_id(self.buttons["Book"]).click()
         print("Finish book single tourist in Busket")



           

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Home(object):
    name = (By.XPATH, "//div[@class='form-group']/input[@name='name']")
    email = (By.NAME, "email")
    checkbox_item = (By.CSS_SELECTOR, "input#exampleCheck1")
    select_box = (By.XPATH, "//select[@id='exampleFormControlSelect1']")
    radio_box = (By.XPATH, "//div[contains(@class,'form-check-inline')]")
    # date_field = (By.NAME, "bday")
    btn_click = (By.CSS_SELECTOR, "input[class*='btn-success']")
    final_text = (By.XPATH, "//strong[text()='Success!']")

    def __init__(self, driver):
        self.driver = driver

    def getLoginName(self):
        return self.driver.find_element(*self.name)

    def getLoginEmail(self):
        return self.driver.find_element(*self.email)

    def getCheckBoxItem(self):
        return self.driver.find_element(*self.checkbox_item)

    def selectDroopDown(self):
        select_box = Select(self.driver.find_element(*self.select_box))
        return select_box

    def radioSelect(self):
        all_option = self.driver.find_elements(*self.radio_box)
        return all_option

    def date_select(self):
        return self.driver.execute_script("document.getElementsByName('bday')[0].value='1993-08-16'")

    def register(self):
        return self.driver.find_element(*self.btn_click).click()

    def validate_success(self):
        return self.driver.find_element(*self.final_text).text



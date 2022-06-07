from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Confirm(object):
    text_field = (By.XPATH, "//input[@id='country']")
    india_option = (By.XPATH, "//div[@class='suggestions']/ul/li/a[text()='India']")
    checkbox_option = (By.XPATH, "//label[@for='checkbox2']")
    purchase_btn = (By.XPATH, "//input[contains(@class,'btn-success')]")
    success_info = (By.XPATH, "//strong[text()='Success!']")

    def __init__(self, driver):
        self.driver = driver

    def send_text(self):
        return self.driver.find_element(*self.text_field)

    def auto_suggest_dropdown(self):
        ww = WebDriverWait(self.driver, 10)
        ww.until(EC.presence_of_element_located(self.india_option))
        return self.driver.find_element(*self.india_option)

    def checkbox_select(self):
        return self.driver.find_element(*self.checkbox_option)

    def final_purchase(self):
        return self.driver.find_element(*self.purchase_btn)

    def success_msg(self):
        return self.driver.find_element(*self.success_info)

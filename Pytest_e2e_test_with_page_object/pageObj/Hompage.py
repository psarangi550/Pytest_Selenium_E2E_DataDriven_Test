from selenium.webdriver.common.by import By

from Pytest_e2e_test_with_page_object.pageObj.CheckOutPage import CheckOut


class Home(object):
    shop = (By.XPATH, "//ul[@class='navbar-nav']/li[2]/a[@class='nav-link']")

    def __init__(self, driver):
        self.driver = driver
        # self.test = test_case_selenium.TestPageSel()

    # defining as class variable
    def shopItem(self):
        self.driver.find_element(*self.shop).click()
        return CheckOut(self.driver)

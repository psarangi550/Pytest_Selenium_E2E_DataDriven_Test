from selenium.webdriver.common.by import By
from Python_selenium_login_e2e_DD_Test.PageObjects.HomePage import Home
from utilities.BaseModule import TestBaseClass


class TestLogin(TestBaseClass):

    def test_register_login(self):
        homepage = Home(self.driver)
        homepage.getLoginName().send_keys('abi')
        homepage.getLoginEmail().send_keys('rika1997@gmail.com')
        homepage.getCheckBoxItem().click()
        homepage.selectDroopDown().select_by_visible_text("Female")
        all_radio_option = homepage.radioSelect()
        self.select_radio_option(all_radio_option,"Employed")
        homepage.date_select()
        homepage.register()
        assert homepage.validate_success() == "Success!"

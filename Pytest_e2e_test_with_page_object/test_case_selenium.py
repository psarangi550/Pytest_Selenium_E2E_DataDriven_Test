# from Pytest_e2e_test_with_page_object.pageObj.CheckOutPage import CheckOut
# from Pytest_e2e_test_with_page_object.pageObj.ConfirmPage import Confirm
from Pytest_e2e_test_with_page_object.pageObj.Hompage import *
from utilities.BaseModule import TestBaseClass


class TestPageSel(TestBaseClass):
    def test_page_selenium(self):
        homepage = Home(driver=self.driver)
        checkout = homepage.shopItem()
        checkout.checkout_blackberry().click()
        confirm = checkout.checkout_item_btn()
        confirm.send_text().send_keys('ind')
        confirm.auto_suggest_dropdown().click()
        confirm.checkbox_select().click()
        confirm.final_purchase().click()
        final_output = confirm.success_msg().text
        assert final_output == "Success!", "Test_failed"

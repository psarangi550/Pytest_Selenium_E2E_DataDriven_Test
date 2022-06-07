from selenium.webdriver.common.by import By
from Pytest_e2e_test_with_page_object.pageObj.ConfirmPage import Confirm


class CheckOut(object):
    checkout_items = (By.CSS_SELECTOR, "div[class*='card h-100']")
    text_item = (By.XPATH, "div[@class='card-body']/h4/a")
    selected_items = (By.XPATH, "div[@class='card-footer']/button")
    click_btn = (By.CSS_SELECTOR, "a.btn-primary")
    check_btn = (By.CSS_SELECTOR,"button.btn-success")

    def __init__(self, driver):
        self.driver = driver

    def checkout_blackberry(self):
        all_items = self.driver.find_elements(*self.checkout_items)
        for item in all_items:
            if item.find_element(*self.text_item).text == "Blackberry":
                item.find_element(*self.selected_items).click()
                break
        return self.driver.find_element(*self.click_btn)

    def checkout_item_btn(self):
        self.driver.find_element(*self.check_btn).click()
        return Confirm(self.driver)

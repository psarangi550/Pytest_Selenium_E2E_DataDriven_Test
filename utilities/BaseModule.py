import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setUp")
class TestBaseClass:
    radio_text = (By.XPATH, "label[@class='form-check-label']")

    def select_radio_option(self, all_list, text_val):
        for item in all_list:
            if item.find_element(*self.radio_text).text == text_val:
                item.find_element(*self.radio_text).click()

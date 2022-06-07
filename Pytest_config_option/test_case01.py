import pytest


@pytest.mark.usefixtures("setUp02")
class TestSelenium:
    def test_sel(self):
        self.driver.get("https://www.google.com/")
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service


@pytest.fixture(scope="class")
def setUp02(request):
    service = Service()
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    request.cls.driver = driver
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="edge",help="provide browser option")


@pytest.fixture(scope="class")
def setUp(request,pytestconfig):
    if pytestconfig.getoption("browser")=="chrome":
        service = Service("C:\\Users\\611903295\\Downloads\\python_BDD_Testing\\chromedriver.exe")
        chrome_options=webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.binary_location="C:\\Users\\611903295\\AppData\\Local\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        driver=webdriver.Chrome(service=service,options=chrome_options)
    else:
        service = Service()
        driver=webdriver.Edge(service=service)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
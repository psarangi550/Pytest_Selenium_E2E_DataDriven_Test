import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="edge", help="provides browser name")


@pytest.fixture(scope="class")
def setUp(request):
    if request.config.getoption("browser") == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.binary_location = "C:\\Users\\611903295\\AppData\\Local\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        service = Service("C:\\Users\\611903295\\Downloads\\python_BDD_Testing\\chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=chrome_options)
    else:
        service = Service()
        driver = webdriver.Edge(service=service)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield driver
    driver.close()
    driver.quit()

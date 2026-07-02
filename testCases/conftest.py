import  pytest
from  selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on: chrome, firefox, edge, headless")

@pytest.fixture(scope="class")
def driver_setup(request):
    browser=request.config.getoption("--browser")
    if browser=="chrome":
        print("Launching Chrome Browser")
        chrome_options=webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        })
        driver=webdriver.Chrome(options=chrome_options)
    elif browser=="firefox":
        print("Launching Firefox Browser")
        driver=webdriver.Firefox()
    elif browser=="edge":
        print("Launching Edge Browser")
        driver=webdriver.Edge()
    elif browser=="headless":
        print("Launching Headless Browser")
        chrome_options=webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver=webdriver.Chrome(options=chrome_options)
    else:
        print("Invalid Browser")
        driver=None
    driver.maximize_window()
    request.cls.driver=driver
    yield driver
    driver.quit()

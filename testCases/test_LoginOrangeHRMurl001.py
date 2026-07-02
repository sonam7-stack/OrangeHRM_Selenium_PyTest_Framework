import pytest
import allure

from Utilities.readConfig import ReadConfig
from pageObjects.Login import Login_page_class
from Utilities.logger import Logger_class

@pytest.mark.usefixtures("driver_setup")
class Test_orangehrm_login_001:
    driver = None
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    login_url = ReadConfig.get_login_url()
    log=Logger_class.get_logger()
    @allure.title("Verify OrangeHRM Login Page URL")
    @allure.description("This test verifies the URL of the OrangeHRM login page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("Navigate to OrangeHRM Login Page")
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", name="OrangeHRM Login Page")
    @allure.issue("https://github.com/allure-framework/allure-python/issues/123", name="Issue 123")
    @allure.story("Verify Login Page URL")
    def test_verify_url_001(self):
        self.log.info("Starting Test: Verify OrangeHRM Login Page URL")
        self.log.info("Navigating to OrangeHRM Login Page")
        self.driver.get(self.login_url)
        self.log.info("OrangeHRM Login Page Loaded")
        if self.driver.title=='OrangeHRM':
            self.log.info("OrangeHRM Login Page URL Verified")
            self.driver.save_screenshot("screenshots\\test_verify_url_pass.png")
            self.log.info("Screenshot of Passed Test Saved")
            allure.attach.file("screenshots\\test_verify_url_pass.png", name="test_verify_url_pass", attachment_type=allure.attachment_type.PNG)
            assert True
        else:
            self.log.error("OrangeHRM Login Page URL Not Verified")
            self.driver.save_screenshot("screenshots\\test_verify_url_fail.png")
            allure.attach.file("screenshots\\test_verify_url_fail.png", name="test_verify_url_fail", attachment_type=allure.attachment_type.PNG)
            assert False
        self.log.info("test_verify_url_001 test Completed")
        self.log.info("=============================================================")

    def test_orangehrm_login_002(self):
        self.log.info("Starting Test: Verify OrangeHRM Login Functionality")
        self.log.info("Navigating to OrangeHRM Login Page")
        self.driver.get(self.login_url)
        self.log.info("OrangeHRM Login Page Loaded")
        lp = Login_page_class(self.driver)
        self.log.info("Entering Username and Password")
        lp.enter_username(self.username)
        lp.enter_password(self.password)
        self.log.info("Clicking Login Button")
        lp.click_login()
        if lp.verify_login() == "Login Successful":
            self.log.info("Login Successful")
            self.driver.save_screenshot("screenshots\\test_OrangeHRM_Login_002_pass.png")
            self.log.info("Screenshot of Passed Test Saved")
            allure.attach.file("screenshots\\test_OrangeHRM_Login_002_pass.png", name="test_OrangeHRM_Login_002_pass", attachment_type=allure.attachment_type.PNG)
            assert True
        else:
            self.log.error("Login Failed")
            self.driver.save_screenshot("screenshots\\test_OrangeHRM_Login_002_fail.png")
            self.log.info("Screenshot of Failed Test Saved")
            allure.attach.file("screenshots\\test_OrangeHRM_Login_002_fail.png", name="test_OrangeHRM_Login_002_fail", attachment_type=allure.attachment_type.PNG)
            assert False
        self.log.info("test_orangehrm_login_002 test Completed")
        self.log.info("=============================================================")

#pytest -v -n=auto --html=Html_Reports\OrangeHRM_Login.html --alluredir=Allure_Reports --browser chrome
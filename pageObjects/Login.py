from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions


class Login_page_class:
    txt_username_xpath = "//input[@placeholder='Username']"
    txt_password_xpath = "//input[@placeholder='Password']"
    btn_login_xpath = "//button[@type='submit']"
    validate_login_xpath = "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']"

    def __init__(self, driver):
        self.driver = driver
        self.wait=WebDriverWait(self.driver, 10)
    def enter_username(self,username):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.txt_username_xpath)))
        self.driver.find_element(By.XPATH, self.txt_username_xpath).send_keys(username)
    def enter_password(self,password):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.txt_password_xpath)))
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def click_login(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.btn_login_xpath)))
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def verify_login(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,self.validate_login_xpath)))
            login_suc=self.driver.find_element(By.XPATH,self.validate_login_xpath).text
            if login_suc=="Dashboard":
                return "Login Successful"
        except:
            return "Login Failed"

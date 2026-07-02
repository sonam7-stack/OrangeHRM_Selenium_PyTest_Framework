@echo off
pytest -v -n=auto --html=Html_Reports\OrangeHRM_Login.html --alluredir=Allure_Reports --browser chrome
pytest -v -n=auto --html=Html_Reports\OrangeHRM_Login.html --alluredir=Allure_Reports --browser firefox
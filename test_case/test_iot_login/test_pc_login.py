import os
import sys
import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest
from test_case.test_iot_openBrowse.base_driver_bowers import driver_basePC_class
from config.path_config import SccreShort
import threading
@allure.description('登录用例')
class Test_login(driver_basePC_class):
    @pytest.mark.parametrize('account,pwd',[("CDAdmin3",'CDAdmin.123'),("CDAdmin1",'CDAdmin.1232'),("CDAdmin1",'CDAdmin.12'),("CDAdmin1",'CDAdmin.124')])
    def test_login_corrent_userandPwd(self,account,pwd):
        self.driver.implicitly_wait(3)
        username_ele = '//*[@id="form_item_account"]'
        self.driver.find_element(by=By.XPATH,value=username_ele).clear()
        self.driver.find_element(by=By.XPATH,value=username_ele).send_keys(account)
        pwd_ele = '//*[@id="form_item_password"]'
        self.driver.find_element(by=By.XPATH,value=pwd_ele).clear()
        self.driver.find_element(by=By.XPATH,value=pwd_ele).send_keys(pwd)
        time.sleep(2)
        log_btn = '//*[@id="app"]/div/div/div[1]/div/form/div[4]/div/div/div/div/button'
        self.driver.find_element(by=By.XPATH,value=log_btn).click()
        time.sleep(2)
        self.driver.save_screenshot(SccreShort+"/b.jpg")
        allure.attach.file(SccreShort+"/b.JPG",attachment_type=allure.attachment_type.JPG)
        time.sleep(10)
        el2='//*[@id="app"]/section/section/section/div[2]/header/div[2]/span/span/span'
        self.driver.find_element(by=By.XPATH,value=el2).click()
        el3='//*[@id="htmlRoot"]/body/div[3]/div/div/ul/li[2]'
        self.driver.find_element(by=By.XPATH,value=el3).click()
        time.sleep(3)
        el4='//*[@id="htmlRoot"]/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/button[2]/span'
        self.driver.find_element(by=By.XPATH,value=el4).click()


if __name__=="__main__":
    op=Test_login
    # op.test_login_corrent_userandPwd()
    op.testposition()
    # t1=threading.Thread(target=Test_login.test_login_corrent_userandPwd)
    # t2=threading.Thread(target=Test_login.test_logout_current_user)
    # t1.start()
    # t1.join()
    # t2.start()

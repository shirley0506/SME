from selenium import webdriver
import time

from selenium.webdriver.common.action_chains import ActionChains

class login_out():
    def __init__(self, ip, driver):
        self.driver = driver
        self.driver.get("http://" + ip + ":3500/login")

    def login(self, name, pwd):
        self.username = self.driver.find_element_by_id("name")
        self.password = self.driver.find_element_by_id("password")
        # 双击选中内容
        ActionChains(self.driver).double_click(self.username).perform()
        self.username.send_keys(name)
        ActionChains(self.driver).double_click(self.password).perform()
        self.password.send_keys(pwd)
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/ul/li[4]/button").click()

    def logout(self):
        self.active_user = self.driver.find_element_by_xpath("//*[@id='root']/section/header/div[3]/span")
        ActionChains(self.driver).move_to_element(self.active_user).perform()
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/ul/li[3]").click()
        self.driver.close()



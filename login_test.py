import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.addCleanup(self.driver.quit)

    def test_successful_login(self):
        driver = self.driver
        driver.get("https://letsusedata.com/")
        driver.find_element(By.ID, "txtUser").click()
        driver.find_element(By.ID, "txtUser").clear()
        driver.find_element(By.ID, "txtUser").send_keys("test1")
        driver.find_element(By.ID, "txtPassword").click()
        driver.find_element(By.ID, "txtPassword").clear()
        driver.find_element(By.ID, "txtPassword").send_keys("Test12456")
        driver.find_element(By.ID, "javascriptLogin").click()
        self.assertFalse(driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Remember username'])[1]/following::span[1]").text.__contains__("Valid Password"))

    def test_unsuccessful_login(self):
        driver = self.driver
        driver.get("https://letsusedata.com/")
        driver.find_element(By.ID, "txtUser").click()
        driver.find_element(By.ID, "txtUser").clear()
        driver.find_element(By.ID, "txtUser").send_keys("test1")
        driver.find_element(By.ID, "txtPassword").click()
        driver.find_element(By.ID, "txtPassword").clear()
        driver.find_element(By.ID, "txtPassword").send_keys("test1234")
        driver.find_element(By.ID, "javascriptLogin").click()
        self.assertFalse(driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Remember username'])[1]/following::span[1]").text.__contains__("Invalid Password"))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

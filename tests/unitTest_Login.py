import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        user = "admin"
        pwd = "123456"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element(By.ID, "id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID, "id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)
        # assert "Logged in"
        try:
            # attempt to find the 'Logout' button - if found, logout
            driver.find_element(By.XPATH, "/html/body/nav/div[1]/div[2]/ul[2]/li/a").click()
            driver.find_element(By.XPATH, "/html/body/nav/div[1]/div[2]/ul[2]/li/ul/li/a").click()
            assert True

        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False

        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == '__main__':
    unittest.main()

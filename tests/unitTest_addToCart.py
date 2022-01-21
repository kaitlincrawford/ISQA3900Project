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
        driver.get("http://127.0.0.1:8000")
        driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/div/div/p/a").click()
        elem = driver.find_element(By.ID, "id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID, "id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000/product_list")
        time.sleep(3)
        # assert "Logged in"
        try:
            driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/a[2]").click()
            time.sleep(3)
            driver.find_element(By.XPATH, "/html/body/div/div/form/input[3]").click()
            time.sleep(3)
            driver.find_element(By.XPATH, "/html/body/nav/div[2]/div/a")
            assert True

        except NoSuchElementException:
            self.fail("Looks like item did not get added to cart")
            assert False

        time.sleep(3)


if __name__ == '__main__':
    unittest.main()

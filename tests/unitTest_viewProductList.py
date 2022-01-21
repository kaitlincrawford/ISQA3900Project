import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_method(self):
        user = "admin"
        pwd = "123456"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)
        try:
            # find 'Shop Now' and click it – note this is all one Python statement
            driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/div/div/p/a").click()
            elem = driver.find_element(By.ID, "id_username")
            elem.send_keys(user)
            elem = driver.find_element(By.ID, "id_password")
            elem.send_keys(pwd)
            time.sleep(3)
            elem.send_keys(Keys.RETURN)
            driver.get("http://127.0.0.1:8000/product_list")
            driver.find_element(By.XPATH, "/html/body/div/div[2]/h1")
            assert True

        except NoSuchElementException:
            self.fail("Product List does not appear when clicked on Shop Now button on home page ")
            assert False

        time.sleep(5)


def tearDown(self):
    self.driver.close()


if __name__ == '__main__':
    unittest.main()

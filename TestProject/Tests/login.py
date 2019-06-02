from selenium import webdriver
import time
import unittest
from TestProject.Pages.loginpage import LoginPage
from TestProject.Pages.homePage import HomePage


class Logintest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create chrome Driver
        cls.driver = webdriver.Chrome("/Users/orengelbendorf 1 2/PycharmProjects/Selenium/Drivers/chromedriver3")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        # Open test page
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main()



import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def fill_form(self, link):
        browser = self.browser
        browser.get(link)
        input1 = self.browser.find_element(By.CSS_SELECTOR, 'div.first_block .form-control.first')
        input1.send_keys("Ivan")
        input2 = self.browser.find_element(By.CSS_SELECTOR, "div.first_block .form-control.second")
        input2.send_keys("Ivanov")
        input3 = self.browser.find_element(By.CSS_SELECTOR, "div.first_block .form-control.third")
        input3.send_keys("ttt@gmail.com")

        browser.find_element(By.CSS_SELECTOR, 'button').click()

        return browser.find_element(By.TAG_NAME, 'h1').text

    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        registration_result = self.fill_form(link)
        self.assertEqual('Congratulations! You have successfully registered!', registration_result)

    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        registration_result = self.fill_form(link)
        self.assertEqual('Congratulations! You have successfully registered!', registration_result)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
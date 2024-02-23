import unittest
from appium.webdriver.common.appiumby import AppiumBy
from infra.mobile_wrapper import MobileWrapper
from logic.calculator_page import CalculatorPage


class CalculatorTests(unittest.TestCase):
    def setUp(self):
        mobile_wrapper = MobileWrapper()
        self.driver = mobile_wrapper.get_driver()

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_sum_calc(self):
        calculator_page = CalculatorPage(self.driver)
        calculator_page.add_flow()
        result = self.driver.find_element(by=AppiumBy.XPATH,
                                          value='//android.widget.TextView[@resource-id="com.google.android.calculator:id/result_final"]')
        actualResult = result.text
        expectedResult = '3'
        self.assertEqual(actualResult, expectedResult, "Sum calculation is incorrect")

    def test_subtraction_calc(self):
        calculator_page = CalculatorPage(self.driver)
        calculator_page.subtraction_flow()
        result = self.driver.find_element(by=AppiumBy.XPATH,
                                          value='//android.widget.TextView[@resource-id="com.google.android.calculator:id/result_final"]')
        actualResult = result.text
        expectedResult = '4'
        self.assertEqual(actualResult, expectedResult, "Subtraction calculation is incorrect")

    def test_Multiplication_calc(self):
        calculator_page = CalculatorPage(self.driver)
        calculator_page.multiple_flow()
        result = self.driver.find_element(by=AppiumBy.XPATH,
                                          value='//android.widget.TextView[@resource-id="com.google.android.calculator:id/result_final"]')
        actualResult = result.text
        expectedResult = '10'
        self.assertEqual(actualResult, expectedResult, "multiplicaiton calculation is incorrect")

    def test_division_calc(self):
        calculator_page = CalculatorPage(self.driver)
        calculator_page.divide_flow()
        result = self.driver.find_element(by=AppiumBy.XPATH,
                                          value='//android.widget.TextView[@resource-id="com.google.android.calculator:id/result_final"]')
        actualResult = result.text
        expectedResult = '5'
        self.assertEqual(actualResult, expectedResult, "multiplicaiton calculation is incorrect")


if __name__ == "__main__":
    unittest.main()


from appium.webdriver.common.appiumby import AppiumBy
from infra.base import BasePage


class CalculatorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_number(self, number):
        number_id = f'com.google.android.calculator:id/digit_{number}'
        print(number_id)
        number_element = self.driver.find_element(by=AppiumBy.ID, value=number_id)
        number_element.click()

    def click_on_operation(self, operation):
        operation_id = f'com.google.android.calculator:id/op_{operation}'
        operation_element = self.driver.find_element(by=AppiumBy.ID, value=operation_id)
        operation_element.click()

    def click_on_equal(self):
        operation_id = 'com.google.android.calculator:id/eq'
        operation_element = self.driver.find_element(by=AppiumBy.ID, value=operation_id)
        operation_element.click()

    def add_flow(self):
        self.click_on_number(1)
        self.click_on_operation("add")
        self.click_on_number(2)
        self.click_on_equal()

    def subtraction_flow(self):
        self.click_on_number(5)
        self.click_on_operation("sub")
        self.click_on_number(1)
        self.click_on_equal()

    def divide_flow(self):
        self.click_on_number(15)
        self.click_on_operation("div")
        self.click_on_number(3)
        self.click_on_equal()

    def multiple_flow(self):
        self.click_on_number(5)
        self.click_on_operation("mul")
        self.click_on_number(2)
        self.click_on_equal()


from appium.webdriver.common.appiumby import AppiumBy
from infra.base import BasePage


class HomePage(BasePage):
    ADD_NEW_EVENT_BTN = "com.claudivan.taskagenda:id/btNovoEvento"
    SELECT_THE_EVENT_TIME_XPATH = "//android.widget.TextView[@resource-id='android:id/text1' and @text='Today']"

    def __init__(self, driver):
        super().__init__(driver)
        self.add_new_event = None
        self.driver = driver
        self.init_page()

    def init_page(self):
        self.add_new_event = self.driver.find_element(by=AppiumBy.ID, value=self.ADD_NEW_EVENT_BTN)

    def click_on_add_new_event_button(self):
        self.add_new_event.click()

    def start_new_event_for_today(self):
        self.click_on_add_new_event_button()
        select_time_for_the_new_event = self.driver.find_element(by=AppiumBy.XPATH,
                                                                 value=self.SELECT_THE_EVENT_TIME_XPATH)
        select_time_for_the_new_event.click()

from appium.webdriver.common.appiumby import AppiumBy
from infra.base import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CreateNewEventPage(BasePage):
    INPUT_EVENT_NAME = "com.claudivan.taskagenda:id/etTitulo"
    SAVE_EVENT_BTN = "com.claudivan.taskagenda:id/item_salvar"

    def __init__(self, driver):
        super().__init__(driver)
        self.input_event_name = None
        self.save_event_button = None
        self.driver = driver
        self.init_page()

    def init_page(self):
        self.input_event_name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.ID, self.INPUT_EVENT_NAME))
        )
        self.save_event_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.ID, self.SAVE_EVENT_BTN))
        )

    def insert_event_name(self):
        self.input_event_name.click()
        self.input_event_name.send_keys("test")

    def add_new_event(self):
        self.insert_event_name()
        self.save_event_button.click()

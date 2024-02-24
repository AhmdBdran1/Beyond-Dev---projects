from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains

from infra.base import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EventsPage(BasePage):
    EVENT_TO_DO = "com.claudivan.taskagenda:id/btEventosSemana"
    EVENT_NAME = "com.claudivan.taskagenda:id/tvTitulo"
    ALLOW_NOTIFICATIONS_BTN = "com.android.permissioncontroller:id/permission_allow_button"
    DELETE_BUTTON_XPATH = "//android.widget.TextView[@resource-id='android:id/text1' and @text='Delete']"
    CONFIRM_DELETE_BTN = "android:id/button1"
    EVENT_CART_XPATH = "//android.widget.ListView[@resource-id='com.claudivan.taskagenda:id/lvListaEventos']/android.widget.FrameLayout/android.widget.RelativeLayout"
    EDIT_BUTTON = "com.claudivan.taskagenda:id/item_editar"
    INPUT_EVENT_NAME = "com.claudivan.taskagenda:id/etTitulo"
    SAVE_CHANGES_BUTTON = "com.claudivan.taskagenda:id/item_salvar"
    EVENT_NAME_AFTER_CHANGE = "com.claudivan.taskagenda:id/tvTitulo"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_exist_of_added_task(self):
        event_to_do = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ID, self.EVENT_TO_DO))
        )
        event_to_do.click()

        try:
            allow_notifications_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, self.ALLOW_NOTIFICATIONS_BTN))
            )
            allow_notifications_btn.click()
        except TimeoutException:
            print("Element not found within the timeout period. Skipping this step.")
            # Optionally, you can raise the exception again to propagate it to the caller
            raise
        event_name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ID, self.EVENT_NAME))
        )
        return event_name.text

    def delete_an_task(self):
        try:
            event_to_do = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, self.EVENT_TO_DO))
            )
            event_to_do.click()

            try:
                allow_notifications_btn = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((AppiumBy.ID, self.ALLOW_NOTIFICATIONS_BTN))
                )
                allow_notifications_btn.click()
            except TimeoutException:
                print("Element not found within the timeout period. Skipping this step.")
                # Optionally, you can raise the exception again to propagate it to the caller
                raise

            event_cart = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.EVENT_CART_XPATH))
            )
            action_chains = ActionChains(self.driver)
            action_chains.click_and_hold(event_cart).perform()
            delete_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, self.DELETE_BUTTON_XPATH))
            )
            delete_button.click()
            confirm_delete_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, self.CONFIRM_DELETE_BTN))
            )
            confirm_delete_button.click()
            return True
        except Exception:
            return False

    def edit_name_of_an_event(self):
        event_to_do = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ID, self.EVENT_TO_DO))
        )
        event_to_do.click()

        try:
            allow_notifications_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, self.ALLOW_NOTIFICATIONS_BTN))
            )
            allow_notifications_btn.click()
        except TimeoutException:
            print("Element not found within the timeout period. Skipping this step.")
            # Optionally, you can raise the exception again to propagate it to the caller
            raise

        event_cart = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, self.EVENT_CART_XPATH))
        )
        event_cart.click()

        edit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ID, self.EDIT_BUTTON))
        )
        edit_button.click()
        input_event_name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ID, self.INPUT_EVENT_NAME))
        )
        input_event_name.click()
        input_event_name.send_keys(" changed")

        save_changes_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ID, self.SAVE_CHANGES_BUTTON))
        )
        save_changes_button.click()

        event_name_after_change = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.ID, self.EVENT_NAME_AFTER_CHANGE))
        )

        return event_name_after_change.text

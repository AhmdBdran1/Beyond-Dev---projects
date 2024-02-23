from time import sleep, time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from infra.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    SEARCH_INPUT_XPATH = "/html/body/div[3]/div/header/div/div/div[1]/div/div[2]/div/div[1]/input"
    SUGGESTIONS_MENU_XPATH = "/html/body/div[3]/div/header/div/div/div[1]/div/div[2]/div/div[3]/div[1]"
    ACCEPT_COOKIES_BTN_XPATH = "//*[@id='didomi-notice-agree-button']/span"
    SELECT_DATE_BTN = "/html/body/div[3]/div/main/div[3]/div[1]/div/div[1]/div[2]/div[2]/div[2]/div"
    SELECTED_DATE_BTN = "//*[@id='tippy-4']/div/div[1]/div/div/div/div/div/div/table/tbody/tr[5]/td[4]/button"
    FIRST_MATCH_BTN_SELECTOR = "#collapsible-content-1708532843147 > div > div > div:nth-child(2) > div > a"
    DATE_OF_MATCH = "/html/body/div[3]/div/main/div[3]/div[2]/div[1]/div/div[2]/div/div/div/div/div[1]"
    CLOSE_NOTIFICATION_BTN_SELECTOR = "#modal-root > div.modal_modal_container__yWQXK > div.wizard-widget-large-view.popup_window__Lmd9Q > button > div > svg"
    setting_icon_xpath = "//button[@class='main-header-module-settings-button']"
    Change_theme_switch_xpath = "//div[@class='settings-module-row-container '][contains(text(),'הגדר רקע כהה')]/div/div"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.accept_cookies_btn = WebDriverWait(self.driver, 10).until(
            (EC.element_to_be_clickable((By.XPATH, self.ACCEPT_COOKIES_BTN_XPATH)))
        )
        self.accept_cookies_btn.click()

    def click_change_theme_switch(self):
        change_theme_switch_element = self.driver.find_element(By.XPATH, self.Change_theme_switch_xpath)
        change_theme_switch_element.click()

    def click_setting_button(self):
        setting_button_element = self.driver.get_element(By.XPATH, self.setting_icon_xpath)
        setting_button_element.click()

    def get_theme_status(self):
        change_theme_switch_element = self.driver.find_element(By.XPATH, self.Change_theme_switch_xpath)
        return change_theme_switch_element.get_attribute("class")

    def display_suggestions_flow(self):
        try:
            search_input = WebDriverWait(self.driver, 10).until(
                (EC.element_to_be_clickable((By.XPATH, self.SEARCH_INPUT_XPATH)))
            )
            search_input.click()
            WebDriverWait(self.driver, 10).until(
                (EC.visibility_of_element_located((By.XPATH, self.SUGGESTIONS_MENU_XPATH)))
            )
            return True
        except Exception as e:
            # Return False if any exception occurs
            print(f"Error occurred: {e}")
            return False

    def display_match_for_specific_match(self):
        try:
            select_date_btn = WebDriverWait(self.driver, 10).until(
                (EC.element_to_be_clickable((By.XPATH, self.SELECT_DATE_BTN)))
            )
            select_date_btn.click()

            selected_date_btn = WebDriverWait(self.driver, 5).until(
                (EC.element_to_be_clickable((By.XPATH, self.SELECTED_DATE_BTN)))
            )
            selected_date_btn.click()

            close_btn = WebDriverWait(self.driver, 15).until(
                (EC.element_to_be_clickable((By.CSS_SELECTOR, self.CLOSE_NOTIFICATION_BTN_SELECTOR)))
            )
            close_btn.click()

            return True

        except Exception as e:
            # Return False if any exception occurs
            print(f"Error occurred: {e}")
            return False

    def get_website_title(self):
        try:
            return self.get_page_title()

        except Exception as e:
            # Return False if any exception occurs
            print(f"Error occurred: {e}")
            return 'error'

    def change_theme_flow(self):
        sleep(1)
        self.click_setting_button()
        self.click_change_theme_switch()
        sleep(1)
        current_settings = self.get_theme_status()
        self.click_change_theme_switch()
        sleep(1)
        return current_settings, self.get_theme_status()

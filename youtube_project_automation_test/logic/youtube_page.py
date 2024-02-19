from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from infra.base_page import BasePage
class YouTubePage(BasePage):
    SEARCH_INPUT="//input[@id='search']"
    SEARCH_SUGGESTIONS="//div[@class='gstl_50 sbdd_a']"


    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.search_input=driver.find_element(By.XPATH,self.SEARCH_INPUT)




    def fill_search_input(self,text):
        self.search_input.send_keys(text)

    def press_enter_on_search_input(self):
        self.search_input.send_keys(Keys.RETURN)



    def search_flow(self,text):
        self.fill_search_input(text)
        self.press_enter_on_search_input()


    def display_suggestions_flow(self):
        self.search_input.send_keys("h")
        self.search_input.send_keys("e")
        self.search_input.send_keys("l")
        self.search_input.send_keys("l")
        sleep(4)
        self.search_suggestions = self.driver.find_element(By.XPATH,self.SEARCH_SUGGESTIONS)
        return self.search_suggestions.is_displayed()




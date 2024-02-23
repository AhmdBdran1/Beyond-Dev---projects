import unittest
from infra.browser_wraper import BrowserWrapper
from logic.home_page import HomePage
from selenium import webdriver


class YouTubePageTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()

    def test_search_suggestion_flow(self, driver):
        home_page = HomePage(driver)
        self.assertTrue(home_page.display_suggestions_flow())
        driver.quit()

    def test_display_specific_date(self, driver):
        home_page = HomePage(driver)
        result = home_page.display_match_for_specific_match()
        self.assertTrue(result)
        driver.quit()

    def test_the_title_of_the_page(self, driver):
        home_page = HomePage(driver)
        title = home_page.get_page_title()
        self.assertIn("365Scores", title, "The title does not match")
        driver.quit()

    def test_change_theme(self, driver):
        old_theme_class, new_theme_class = driver.change_theme_flow()
        self.assertNotEqual(old_theme_class, new_theme_class)
        driver.quit()

    def test_specific_test(self):
        self.browser.run_test(self.test_search_suggestion_flow)  # select the specific function you want to run

    def test_all_tests(self):
        tests_list = [self.test_the_title_of_the_page, self.test_display_specific_date,
                      self.test_search_suggestion_flow]
        for test in tests_list:
            self.browser.run_test(test)


if __name__ == "__main__":
    unittest.main()


from infra.browser_wrapper import BrowserWrapper
from logic.youtube_page import YouTubePage
import unittest

class YouTubePageTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver("http://www.youtube.com")
        self.youtube_page = YouTubePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_check_title_for_search(self):
        self.youtube_page.search_flow("Python programming")
        self.assertIn("Python programming", self.youtube_page.get_page_title(), "The title does not match")

    def test_autocomplete_suggestions(self):
        self.assertTrue(self.youtube_page.display_suggestions_flow())


if __name__ == "__main__":
    unittest.main()


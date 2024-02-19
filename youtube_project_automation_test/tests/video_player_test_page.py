
from infra.browser_wrapper import BrowserWrapper
from logic.video_player_page import VideoPlayerPage
from logic.youtube_page import YouTubePage
import unittest


class YouTubePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver("http://www.youtube.com")
        self.youtube_page = YouTubePage(self.driver)
        self.youtube_page.search_flow("Python programming")
        self.video_player_page = VideoPlayerPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_visibility_of_play_button_after_click_on_video(self):
        self.assertTrue(self.video_player_page.check_visibility_of_play_button_after_click_on_video())

    # def test_add_to_history(self):
    #     self.assertTrue(self.video_player_page.add_to_history())

    def test_skip_advertising(self):
        self.assertTrue(self.video_player_page.skip_video_flow())

    def test_open_channel_page_from_video_page(self):
        self.assertTrue(self.video_player_page.open_channel_page_from_video_page())

    def test_change_video_quality(self):
        self.assertTrue(self.video_player_page.change_video_quality())

if __name__ == "__main__":
    unittest.main()


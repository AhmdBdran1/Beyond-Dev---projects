from time import sleep

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from infra.base_page import BasePage
class VideoPlayerPage(BasePage):
    VIDEO_ITEM_SELECTOR = "#contents > ytd-video-renderer:nth-child(5)"
    VIDEO_PLAYER_XPATH = "//*[@id='movie_player']/div[1]/video"
    PLAY_BTN_SELECTOR = "#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button"
    SKIP_BTN_NAME = "ytp-ad-skip-button-text"
    VIDEO_SETTING_BTN_SELECTOR = ".ytp-settings-button"
    QUALITY_SETTING_OPTION = "#ytp-id-18 > div > div > div:nth-child(4)"
    VIDEO_QUALITY_MENU = ".ytp-popup.ytp-settings-menu"
    VIDEO_QUALITY_OPTIONS = "#ytp-id-18"
    VIDEO_TITLE_SELECTOR = "h1.title yt-formatted-string"
    VIDEO_QUALITY_XPATH="//*[@id='ytp-id-18']/div/div[2]/div[2]"
    CHANNEL_NAME_XPATH\
        = "//*[@id='owner']/ytd-video-owner-renderer/a"



    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

        first_video = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#contents > ytd-video-renderer:nth-child(5)"))
        )
        first_video.click()

        self.video = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH,self.VIDEO_PLAYER_XPATH))
        )
        self.video_title = self.driver.find_element(By.CSS_SELECTOR, self.VIDEO_TITLE_SELECTOR).text



    def check_visibility_of_play_button_after_click_on_video(self):

        try:
            # Wait for the play button to become invisible
            self.play_btn = WebDriverWait(self.driver, 30).until(
                EC.invisibility_of_element((By.CSS_SELECTOR, self.PLAY_BTN_SELECTOR))
            )

            # Click on the video
            self.video.click()
            sleep(3)

            # Wait for the play button to become visible again
            self.play_btn = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, self.PLAY_BTN_SELECTOR))
            )

            # If everything goes well, return True
            return True

        except TimeoutException:
            # If timeout exception occurs, return False or handle the exception as needed
            return False


    def add_to_history(self):
        sleep(3)
        # Click on the YouTube logo to go back to the homepage
        self.driver.find_element(By.ID, "logo-icon").click()
        # Go to the History page
        self.driver.get("https://www.youtube.com/feed/history")
        # Wait for the history page to load
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "ytd-video-renderer #video-title"))
        )
        # Check if the video is in the history
        history_videos = self.driver.find_elements(By.CSS_SELECTOR, "ytd-video-renderer #video-title")
        history_video_titles = [video.text for video in history_videos]

        if self.video_title in history_video_titles:
            return True
        else:
            return False



    def open_channel_page_from_video_page(self):
        # Click on the first video
        channel_name_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CHANNEL_NAME_XPATH))
        )

        channel_url = channel_name_element.get_attribute("href")
        channel_name_element.click()
        sleep(5)

        # Get the URL of the opened channel page
        opened_channel_url = self.driver.current_url
        return channel_url == opened_channel_url

    def skip_video_flow(self):
        try:
            # Wait for the advertisement skip button to appear
            skip_ad_button = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.CLASS_NAME, self.SKIP_BTN_NAME))
            )
            # Click the skip ad button
            skip_ad_button.click()
            return True

        except Exception as e:
            # Return False if any exception occurs
            print(f"Error occurred: {e}")
            return False


    def change_video_quality(self):
        try:

            self.skip_video_flow()

            video_settings_button = (WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.VIDEO_SETTING_BTN_SELECTOR))
            ))
            # Click on the video quality settings option (gear icon)
            video_settings_button.click()

            quality_settings_button = (WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.QUALITY_SETTING_OPTION))
            ))
            quality_settings_button.click()


            # Once the menu is present, find the video quality options
            video_quality_option = WebDriverWait(self.driver,10).until(
                EC.element_to_be_clickable((By.XPATH, self.VIDEO_QUALITY_XPATH))
            )

            video_quality_option.click()

            sleep(2)
            return True

        except Exception as e:
            # Return False if any exception occurs
            print(f"Error occurred: {e}")
            return False








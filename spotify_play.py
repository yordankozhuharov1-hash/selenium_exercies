from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SpotifyPlayer:
    def __init__(self):
        self.driver = webdriver.Edge()

    def play_when_is_sad(self):
        self.driver.get(
            "https://www.youtube.com/watch?v=R-KTvjTWKhk&autoplay=1"
        )

        wait = WebDriverWait(self.driver, 15)

        try:
            play_btn = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button.ytp-play-button")
                )
            )

            if play_btn.get_attribute("title") == "Play (k)":
                play_btn.click()

            print("Video started!")

        except Exception as e:
            print("Error:", e)

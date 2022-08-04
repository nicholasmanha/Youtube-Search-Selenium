import youtube.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Youtube(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers",
                 teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--mute-audio")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Youtube, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()


    def search_vid(self, vid_title):
        self.get(const.BASE_URL.format(str(vid_title)))


    def play_vid(self):
        wait = WebDriverWait(self, 3)
        presence = EC.presence_of_element_located
        visible = EC.visibility_of_element_located
        wait.until(visible((By.ID, "video-title")))
        self.find_element(By.ID, "video-title").click()

    def getstats(self):
        views = self.find_element(By.CLASS_NAME, "view-count").get_attribute('innerHTML')
        views_num = views[0:len(views)-6]
        return views_num
        self.quit()
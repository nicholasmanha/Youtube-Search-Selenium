import youtube.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from prettytable import PrettyTable


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


    def search_vid(self, vid_title, list_length):

        self.get(const.BASE_URL.format(str(vid_title)))
        wait = WebDriverWait(self, 3)
        presence = EC.presence_of_element_located
        visible = EC.visibility_of_element_located
        wait.until(visible((By.ID, "video-title")))
        results_cont = self.find_element(By.ID, "contents")
        results_elements = results_cont.find_elements(By.CSS_SELECTOR, "*")
        num = 0 #limiting search results
        myTable = PrettyTable(['Title', 'Author', 'Date', 'Views'])
        while True:
            for video in results_elements:
                #checking if current element is a video
                if str(video.get_attribute('id')).strip() == 'video-title':
                    title = str(video.get_attribute('title'))
                    label = str(video.get_attribute('aria-label'))
                    #label with everything but the title
                    no_title = label.replace(title, '')
                    author = no_title[4:re.search(r"\d", no_title).start()-1]
                    date = no_title[re.search(r"\d", label.replace(title, '')).start():no_title.index("ago")-1]
                    words = no_title.split()
                    views = words[-2]
                    myTable.add_row([title, author, date + " ago", views])
                    num += 1
                if num >= list_length:
                    break
            break
        print(myTable)
        self.quit()



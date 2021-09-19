from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

ADD_BUTTON = (By.XPATH, "//a[@data-original-title]")
DELETE_BUTTON = (By.XPATH, "//button[@data-original-title='Delete']")
TITLE = (By.XPATH, '//h1')
SAVE_BUTTON = (By.XPATH, '//button[@data-original-title="Save"]')
CANCEL_BUTTON = (By.XPATH, '//a[@data-original-title="Cancel"]')

class TitlePanel(BasePage):

    def get_title(self):
        title = self.get_text(*TITLE)
        return title

    def add_button_click(self):
        self.click_button(*ADD_BUTTON)

    def delete_button_click(self):
        self.click_button(*DELETE_BUTTON)

    def save_button_click(self):
        self.click_button(*SAVE_BUTTON)

    def return_button_click(self):
        self.click_button(*CANCEL_BUTTON)

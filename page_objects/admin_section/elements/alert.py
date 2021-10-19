from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

'''
Модуль для взаимодействия с локальными алертами opencart (не браузерными)
'''

ALERT_DIV = (By.XPATH, '//div[@class = "alert alert-danger alert-dismissible"]')
CLOSE_BUTTON = (By.XPATH, f'{ALERT_DIV[1]}//button[@class="close"]')


class Alert(BasePage):

    def text(self) -> str:
        alert_text = self.get_text(*ALERT_DIV)
        return alert_text

    def click_close_button(self):
        self.click_button(*CLOSE_BUTTON)

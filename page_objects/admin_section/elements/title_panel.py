from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import allure


class TitlePanel(BasePage):
    ADD_BUTTON = (By.XPATH, "//a[@data-original-title]")
    DELETE_BUTTON = (By.XPATH, "//button[@data-original-title='Delete']")
    TITLE = (By.XPATH, '//h1')
    SAVE_BUTTON = (By.XPATH, '//button[@data-original-title="Save"]')
    CANCEL_BUTTON = (By.XPATH, '//a[@data-original-title="Cancel"]')

    @allure.step("Получить заголовок страницы")
    def get_title(self):
        self.logger.info(f"Получить заголовок страницы")
        title = self.get_text(*self.TITLE)
        return title

    @allure.step('Нажать на кнопку "Добавить"')
    def add_button_click(self):
        self.logger.info(f'Нажать на кнопку "Добавить"')
        self.click_button(*self.ADD_BUTTON)

    @allure.step('Нажать на кнопку "Удалить"')
    def delete_button_click(self):
        self.logger.info(f'Нажать на кнопку "Удалить"')
        self.click_button(*self.DELETE_BUTTON)

    @allure.step('Нажать на кнопку "Сохранить"')
    def save_button_click(self):
        self.logger.info(f'Нажать на кнопку "Сохранить"')
        self.click_button(*self.SAVE_BUTTON)

    @allure.step('Нажать на кнопку "Отмена"')
    def return_button_click(self):
        self.logger.info(f'Нажать на кнопку "Отмена"')
        self.click_button(*self.CANCEL_BUTTON)

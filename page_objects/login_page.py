from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import allure


class LoginPage(BasePage):
    POSTFIX_URL = '/admin'
    USERNAME_INPUT = (By.ID, "input-username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGO = (By.XPATH, '//img[@alt="OpenCart"]'),
    LOGIN_BUTTON = (By.XPATH, '//button[text()=" Login"]')
    PANEL_TITLE = (By.XPATH, '//h1[text()=" Please enter your login details."]')
    FORGOTTEN_PASSWORD_LINK = (
        By.XPATH, '//a[text()="Forgotten Password" and contains (@href, "admin/index.php?route=common/forgotten")]')

    @allure.step("Перейти на страницу авторизации")
    def open_page(self, _url):
        self.logger.info(f"Перейти на страницу авторизации: {_url + self.POSTFIX_URL}")
        self.browser.get(_url + self.POSTFIX_URL)

    @allure.step("Ввести логин ")
    def entering_login(self, login):
        self.logger.info(f"Ввести логин {login}")
        self.enter_input(*self.USERNAME_INPUT, login)

    @allure.step("Ввести пароль")
    def entering_password(self, password):
        self.logger.info(f"Ввести пароль {password}")
        self.enter_input(*self.PASSWORD_INPUT, password)

    @allure.step("Авторизоваться")
    def login_button_click(self):
        self.logger.info(f"Авторизоваться")
        self.click_button(*self.LOGIN_BUTTON)

    def sign_in(self, login, password):
        '''
        вынес наиболее частый сценарий в отдельный метод
        '''
        self.entering_login(login)
        self.entering_password(password)
        self.login_button_click()

    @allure.step("Восстановить пароль")
    def forgotten_password_link_click(self):
        self.logger.info(f"Восстановить пароль")
        link = self.find_element_with_wait(*self.FORGOTTEN_PASSWORD_LINK)
        link.click()

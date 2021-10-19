import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class RegisterPage(BasePage):
    FIRST_NAME_INPUT = (By.XPATH, '//input[@name="firstname"]')
    LAST_NAME_INPUT = (By.XPATH, '//input[@name="lastname"]')
    EMAIL_INPUT = (By.XPATH, '//input[@name="email"]')
    TELEPHONE_INPUT = (By.XPATH, '//input[@name="telephone"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]')
    PASSWORD_CONFIRM_INPUT = (By.XPATH, '//input[@name="confirm"]')
    SUBSCRIBE_RADIOBUTTON_YES = (By.XPATH, '//input[@name="newsletter" and @value="1"]')
    SUBSCRIBE_RADIOBUTTON_NO = (By.XPATH, '//input[@name="newsletter" and @value="0"]')
    PRIVACY_POLICY_CHECKBOX = (By.XPATH, '//input[@name="agree"]')
    CONTINUE_BUTTON = (By.XPATH, '//input[@value="Continue"]')
    SUCCESSFUL_TITLE = (By.XPATH, '//h1[text()="Your Account Has Been Created!"]')

    @allure.step("Ввести имя")
    def enter_first_name(self, first_name: str = 'Joe'):
        self.logger.info(f"Ввести имя - {first_name}")
        self.enter_input(*self.FIRST_NAME_INPUT, first_name)

    @allure.step("Ввести фамилию")
    def enter_last_name(self, last_name: str = 'Smith'):
        self.logger.info(f"Ввести фамилию - {last_name}")
        self.enter_input(*self.LAST_NAME_INPUT, last_name)

    @allure.step("Ввести email")
    def enter_email(self, email: str = 'ed.d.xample@mail.com'):
        self.logger.info(f"Ввести email - {email}")
        self.enter_input(*self.EMAIL_INPUT, email)

    @allure.step("Ввести телефон")
    def enter_telephone(self, phone_number: str = '+12121234567'):
        self.logger.info(f"Ввести телефон - {phone_number}")
        self.enter_input(*self.TELEPHONE_INPUT, phone_number)

    @allure.step("Ввести пароль")
    def enter_password(self, password: str = 'ghf54fdgLL'):
        self.logger.info(f"Ввести пароль - {password}")
        self.enter_input(*self.PASSWORD_INPUT, password)

    @allure.step("Подтвердить пароль")
    def enter_password_confirm(self, password: str = 'ghf54fdgLL'):
        self.logger.info(f"Подтвердить пароль - {password}")
        self.enter_input(*self.PASSWORD_CONFIRM_INPUT, password)

    @allure.step("Подписаться на рассылку")
    def subscribe_newsletter(self, param: bool = True):
        self.logger.info(f"Подписаться на рассылку - {str(param)}")
        if param:
            self.click_button(*self.SUBSCRIBE_RADIOBUTTON_YES)
        else:
            self.click_button(*self.SUBSCRIBE_RADIOBUTTON_NO)

    @allure.step("Принять политику конфиденциальности")
    def click_privacy_policy_checkbox(self):
        self.logger.info("Принять политику конфиденциальности")
        self.click_button(*self.PRIVACY_POLICY_CHECKBOX)

    @allure.step("Продолжить")
    def click_continue(self):
        self.logger.info("Продолжить")
        self.click_button(*self.CONTINUE_BUTTON)

    def enter_all_user_fields(self):
        '''
        общий метод для частого сценария
        '''
        self.enter_first_name()
        self.enter_last_name()
        self.enter_email()
        self.enter_telephone()
        self.enter_password()
        self.enter_password_confirm()

    @allure.step("Проверка успешного окончания регистрации")
    def check_successfully_created(self) -> bool:
        self.logger.info("Проверка успешного окончания регистрации")
        self.find_element_with_wait(*self.SUCCESSFUL_TITLE)
        return True

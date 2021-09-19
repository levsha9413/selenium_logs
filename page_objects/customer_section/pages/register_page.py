from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

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


class RegisterPage(BasePage):

    def enter_first_name(self, first_name: str = 'Joe'):
        self.enter_input(*FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name: str = 'Smith'):
        self.enter_input(*LAST_NAME_INPUT, last_name)

    def enter_email(self, email: str = 'ed.d.xample@mail.com'):
        self.enter_input(*EMAIL_INPUT, email)

    def enter_telephone(self, phone_number: str = '+12121234567'):
        self.enter_input(*TELEPHONE_INPUT, phone_number)

    def enter_password(self, password: str = 'ghf54fdgLL'):
        self.enter_input(*PASSWORD_INPUT, password)

    def enter_password_confirm(self, password: str = 'ghf54fdgLL'):
        self.enter_input(*PASSWORD_CONFIRM_INPUT, password)

    def subscribe_newsletter(self, param: bool = True):
        if param:
            self.click_button(*SUBSCRIBE_RADIOBUTTON_YES)
        else:
            self.click_button(*SUBSCRIBE_RADIOBUTTON_NO)

    def click_privacy_policy_checkbox(self):
        self.click_button(*PRIVACY_POLICY_CHECKBOX)

    def click_continue(self):
        self.click_button(*CONTINUE_BUTTON)

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

    def check_successfully_created(self) -> bool:
        self.find_element_with_wait(*SUCCESSFUL_TITLE)
        return True

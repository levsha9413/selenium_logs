from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import enum
import allure

UPPER_PANEL = '//nav[@id="top"]'


class Currencies(enum.Enum):
    EURO = (By.XPATH, f'{UPPER_PANEL}//button[@name="EUR"]')
    POUND_STERLING = (By.XPATH, f'{UPPER_PANEL}//button[@name="GBP"]')
    USD = (By.XPATH, f'{UPPER_PANEL}//button[@name="USD"]')


class UpperUserPanel(BasePage):
    SWITCH_CURRENCY_BUTTON = (By.XPATH, f'{UPPER_PANEL}//i[@class="fa fa-caret-down"]')
    USD_SYMBOL = (By.XPATH, f'{UPPER_PANEL}//strong[text()="$"]')
    EURO_SYMBOL = (By.XPATH, f'{UPPER_PANEL}//strong[text()="€"]')
    POUND_SYMBOL = (By.XPATH, f'{UPPER_PANEL}//strong[text()="£"]')
    CONTACT_BUTTON = (By.XPATH, f'{UPPER_PANEL}//i[@class="fa fa-phone"]')
    MY_ACCOUNT_BUTTON = (By.XPATH, f'{UPPER_PANEL}//a[@title="My Account"]')
    REGISTER = (By.XPATH, f'{UPPER_PANEL}//a[text()="Register"]')
    LOGIN = (By.XPATH, f'{UPPER_PANEL}//a[text()="Login"]')
    WISH_LIST_BUTTON = (By.XPATH, f'{UPPER_PANEL}//a[@id="wishlist-total"]')
    SHOPPING_CART_BUTTON = (By.XPATH, f'{UPPER_PANEL}//a[@title="Shopping Cart"]')
    CHECKOUT_BUTTON = (By.XPATH, f'{UPPER_PANEL}//a[@title="Checkout"]')

    @allure.step("Переключить валюту")
    def switch_currency(self, currency: Currencies):
        self.logger.info(f'Переключить валюту на {currency.name}')
        self.click_button(*self.SWITCH_CURRENCY_BUTTON)
        selector = currency.value
        self.click_button(*selector)

    @allure.step("Проверка текущей валюты")
    def check_current_currency(self, currency: Currencies):
        self.logger.info(f'Проверить, что текущая валюта {currency.name}')
        selector = None
        if currency.value == Currencies.USD.value:
            selector = self.USD_SYMBOL
        elif currency.value == Currencies.EURO.value:
            selector = self.EURO_SYMBOL
        elif currency.value == Currencies.POUND_STERLING.value:
            selector = self.POUND_SYMBOL
        self.find_element_with_wait(*selector)

    @allure.step("Перейти к контактам")
    def go_to_contact(self):
        self.logger.info('Перейти к контактам')
        self.click_button(*self.CONTACT_BUTTON)

    @allure.step("Перейти к профилю покупателя")
    def go_to_my_account(self):
        self.logger.info('Перейти к профилю покупателя')
        self.click_button(*self.MY_ACCOUNT_BUTTON)

    @allure.step("Перейти в избранное")
    def go_to_wish_list(self):
        self.logger.info('Перейти в избранное')
        self.click_button(*self.WISH_LIST_BUTTON)

    @allure.step("Перейти в корзину")
    def go_to_shopping_cart(self):
        self.logger.info('Перейти в корзину')
        self.click_button(*self.SHOPPING_CART_BUTTON)

    @allure.step("Перейти к заказу")
    def checkout(self):
        self.logger.info('Перейти к заказу')
        self.click_button(*self.CHECKOUT_BUTTON)

    @allure.step("Перейти к регистрации")
    def go_to_register(self):
        self.logger.info('Перейти к регистрации')
        self.go_to_my_account()
        self.click_button(*self.REGISTER)

    @allure.step("Войти")
    def go_to_login(self):
        self.logger.info('Войти')
        self.go_to_my_account()
        self.click_button(*self.LOGIN)

from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import enum

UPPER_PANEL = '//nav[@id="top"]'
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


class Currencies(enum.Enum):
    EURO = (By.XPATH, f'{UPPER_PANEL}//button[@name="EUR"]')
    POUND_STERLING = (By.XPATH, f'{UPPER_PANEL}//button[@name="GBP"]')
    USD = (By.XPATH, f'{UPPER_PANEL}//button[@name="USD"]')


class UpperUserPanel(BasePage):

    def switch_currency(self, currency: Currencies):
        self.click_button(*SWITCH_CURRENCY_BUTTON)
        selector = currency.value
        self.click_button(*selector)

    def check_current_currency(self, currency: Currencies):
        selector = None
        if currency.value == Currencies.USD.value:
            selector = USD_SYMBOL
        elif currency.value == Currencies.EURO.value:
            selector = EURO_SYMBOL
        elif currency.value == Currencies.POUND_STERLING.value:
            selector = POUND_SYMBOL
        self.find_element_with_wait(*selector)

    def go_to_contact(self):
        self.click_button(*CONTACT_BUTTON)

    def go_to_my_account(self):
        self.click_button(*MY_ACCOUNT_BUTTON)

    def go_to_wish_list(self):
        self.click_button(*WISH_LIST_BUTTON)

    def go_to_shopping_cart(self):
        self.click_button(*SHOPPING_CART_BUTTON)

    def checkout(self):
        self.click_button(*CHECKOUT_BUTTON)

    def go_to_register(self):
        self.go_to_my_account()
        self.click_button(*REGISTER)

    def go_to_login(self):
        self.go_to_my_account()
        self.click_button(*LOGIN)

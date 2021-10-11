from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import enum

'''
селектор product_checkbox находится в методе checkbox_click,
т.к. он зависит от передаваемого в метод параметра
'''
INPUT_PRODUCT_NAME_FILTER = (By.XPATH, '//input[@name="filter_name"]')
INPUT_MODEL_FILTER = (By.XPATH, '//input[@name="filter_model"]')
INPUT_PRICE_FILTER = (By.XPATH, '//input[@name="filter_price"]')
INPUT_QUANTITY_FILTER = (By.XPATH, '//input[@name="filter_quantity"]')
SELECT_STATUS = (By.XPATH, '//select')
BUTTON_FILTER = (By.XPATH, '//button[@id="button-filter"]')


class SelectItems(enum.Enum):
    ENABLED = "1"
    DISABLED = "0"


class ProductsPage(BasePage):

    def checkbox_click(self, product_name: str = 'Test product name'):
        '''
        выставляет чекбокс у товара, в название которого входит строка product_name
        '''
        self.logger.info(f'Поставить чекбокс у товара, в названии которого присутствует "{product_name}"')
        product_checkbox = (By.XPATH, f'//tbody/tr[./td[contains(text(), "{product_name}")]]//input')
        self.click_button(*product_checkbox)

    def verification_product_by_name(self, product_name: str = 'Test product name') -> bool:
        self.logger.info(f"Проверить существование товара, в названии которого присутствует '{product_name}'")
        try:
            self.find_element_with_wait(By.XPATH, f'//tbody/tr[./td[contains(text(), "{product_name}")]]')
            return True
        except AssertionError:
            return False

    def enter_product_name_filter(self, product_name: str):
        self.logger.info(f'Заполнить фильтр по имени значением "{product_name}"')
        self.enter_input(*INPUT_PRODUCT_NAME_FILTER, product_name)

    def enter_model_filter(self, model: str):
        self.logger.info(f'Заполнить фильтр по модели значением "{model}"')
        self.enter_input(*INPUT_MODEL_FILTER, model)

    def enter_price_filter(self, price: str):
        self.logger.info(f'Заполнить фильтр по цене значением "{price}"')
        self.enter_input(*INPUT_PRICE_FILTER, price)

    def enter_quantity_filter(self, quantity: str):
        self.logger.info(f'Заполнить фильтр по количеству значением "{quantity}"')
        self.enter_input(*INPUT_QUANTITY_FILTER, quantity)

    def select_status_filter(self, status: SelectItems):
        self.logger.info(f'Заполнить фильтр по статусу значением "{status.name}"')
        select = self.get_select(*SELECT_STATUS)
        text = status.value
        select.select_by_value(text)

    def filter(self):
        self.logger.info('Применить фильтры')
        self.click_button(*BUTTON_FILTER)

from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

POSTFIX_URL = '/index.php?route=product/product&path=20&product_id=42'
PAGE_TITLE = (By.XPATH, '''//head/title[text()='Apple Cinema 30']''')
PRODUCT_NAME = (By.XPATH, '''//h1[text()='Apple Cinema 30"']''')
TAB_DESCRIPTION = (By.XPATH, '''//a[@href="#tab-description"]''')
TAB_SPECIFICATION = (By.XPATH, '''//a[@href="#tab-specification"]''')
TAB_REVIEW = (By.XPATH, '''//a[@href="#tab-review"]''')
DESCRIPTION_CONTENT = (By.XPATH, '''//div[@class='tab-content']''')
CURRENT_PRICE = (By.XPATH, '''//h2[text()='$110.00']''')


class ProductPage(BasePage):

    def open_page(self, _url):
        self.browser.get(_url + POSTFIX_URL)

    def verification_page_title(self):
        self.find_element_with_wait(*PAGE_TITLE)

    def verification_product_name(self):
        self.find_element_with_wait(*PRODUCT_NAME)

    def verification_description_exist(self):
        self.find_element_with_wait(*DESCRIPTION_CONTENT)
        self.find_element_with_wait(*TAB_DESCRIPTION)

    def verification_price(self, price: str):
        product = self.find_element_with_wait(*CURRENT_PRICE)
        rez = False
        if product.text == price:
            rez = True
        return rez

from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

POSTFIX_URL = ''

HOME_LINK = (By.XPATH, '''//a[contains(@href, "/index.php?route=common/home")]''')
BIG_SWIPER = (By.XPATH, '''//div[@id='slideshow0']''')
MENU_BAR = (By.XPATH, '''//nav[@id="menu"]''')
PRODUCT_BAR = (By.XPATH, '''//div[@id="content"]/div[@class="row"]''')
PARTNERS_SWIPER = (By.XPATH, '''//div[@id="carousel0"]''')
FOOTER = (By.XPATH, '''//footer''')
SEARCH_PANEL = (By.XPATH, '''//input[@name = "search"]''')
BUTTON_CART = (By.XPATH, '''//div[@id="cart"]/button''')


class HomePage(BasePage):

    def open_page(self, _url):
        self.browser.get(_url + POSTFIX_URL)

    def verification_big_swiper(self):
        self.find_element_with_wait(*BIG_SWIPER)

    def verification_menu_bar(self):
        self.find_element_with_wait(*MENU_BAR)

    def verification_product_bar(self):
        self.find_element_with_wait(*PRODUCT_BAR)

    def verification_footer(self):
        self.find_element_with_wait(*FOOTER)

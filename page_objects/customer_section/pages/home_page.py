from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import allure


class HomePage(BasePage):
    POSTFIX_URL = ''
    HOME_LINK = (By.XPATH, '//a[contains(@href, "/index.php?route=common/home")]')
    BIG_SWIPER = (By.XPATH, '//div[@id="slideshow0"]')
    MENU_BAR = (By.XPATH, '//nav[@id="menu"]')
    PRODUCT_BAR = (By.XPATH, '//div[@id="content"]/div[@class="row"]')
    PARTNERS_SWIPER = (By.XPATH, '//div[@id="carousel0"]')
    FOOTER = (By.XPATH, '//footer')
    SEARCH_PANEL = (By.XPATH, '//input[@name = "search"]')
    BUTTON_CART = (By.XPATH, '//div[@id="cart"]/button')

    @allure.step("Перейти на домашнюю страницу")
    def open_page(self, _url):
        self.logger.info(f"Перейти на домашнюю страницу: {_url + self.POSTFIX_URL}")
        self.browser.get(_url + self.POSTFIX_URL)

    @allure.step("Проверка наличия большого свайпера")
    def verification_big_swiper(self):
        self.logger.info("Проверка наличия большого свайпера")
        self.find_element_with_wait(*self.BIG_SWIPER)

    @allure.step("Проверка панели меню")
    def verification_menu_bar(self):
        self.logger.info("Проверка панели меню")
        self.find_element_with_wait(*self.MENU_BAR)

    @allure.step("Проверка наличия меню товаров")
    def verification_product_bar(self):
        self.logger.info("Проверка наличия меню товаров")
        self.find_element_with_wait(*self.PRODUCT_BAR)

    @allure.step("Проверка наличия футера")
    def verification_footer(self):
        self.logger.info("Проверка наличия футера")
        self.find_element_with_wait(*self.FOOTER)

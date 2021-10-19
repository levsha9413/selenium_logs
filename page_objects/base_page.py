from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import logging
import allure


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.logger = logging.getLogger(type(self).__name__)

    def find_element_with_wait(self, locator, selector, timeout=5):
        self.logger.debug(f"Поиск элемента '{selector}'")
        try:
            element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((locator, selector)))
        except TimeoutException:
            self.attach_screenshot_to_report()
            raise AssertionError("Не найден элемент с селектором: {}".format(selector))
        return element

    def find_element_with_wait_clickable(self, locator, selector, timeout=5):

        self.logger.debug(f"Поиск с проверкой на кликабельность и видимость элемента '{selector}'")
        try:
            element = WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((locator, selector)))
            element = WebDriverWait(self.browser, timeout).until(EC._element_if_visible(element))
        except TimeoutException:
            self.attach_screenshot_to_report()
            raise AssertionError("Не найден элемент с селектором: {}".format(selector))
        except ElementNotInteractableException:
            self.attach_screenshot_to_report()
            raise AssertionError("Не смог взаимодействовать с элементом с селектором: {}".format(selector))
        return element

    def enter_input(self, locator, selector, input_data):
        self.logger.debug(f"Ввод в input '{selector}'")
        input_field = self.find_element_with_wait(locator, selector)
        input_field.clear()
        input_field.send_keys(input_data)

    def click_button(self, locator, selector):
        self.logger.debug(f"Клик на элемент '{selector}'")
        button = self.find_element_with_wait(locator, selector)
        actions = ActionChains(self.browser)
        actions.pause(1).click(button)
        actions.perform()

    def get_text(self, locator, selector) -> str:
        self.logger.debug(f"Получить текстовую ноду элемента '{selector}'")
        element = self.find_element_with_wait(locator, selector)
        element_text = element.text
        return element_text

    def get_select(self, locator, selector) -> Select:
        self.logger.debug(f"Сформировать объект 'селект' из элемента '{selector}'")
        elem = self.find_element_with_wait(locator, selector)
        select = Select(elem)
        return select

    def attach_screenshot_to_report(self):
        allure.attach(name=self.browser.session_id,
                      body=self.browser.get_screenshot_as_png(),
                      attachment_type=allure.attachment_type.PNG)

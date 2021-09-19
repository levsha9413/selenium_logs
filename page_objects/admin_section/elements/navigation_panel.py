from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import enum


class Sections(enum.Enum):
    CATALOG_SECTION = (By.XPATH, "//a[@href='#collapse1']")
    PRODUCTS_SUBSECTION = (By.XPATH, "//nav//a[contains(text(),'Product')]")
    EXTENSIONS_SECTION = (By.XPATH, "//a[@href='#collapse14']")
    DESIGN_SECTION = (By.XPATH, "//a[@href='#collapse20']")
    SALES_SECTION = (By.XPATH, "//a[@href='#collapse26']")
    CUSTOMERS_SECTION = (By.XPATH, "//a[@href='#collapse33']")
    MARKETING_SECTION = (By.XPATH, "//a[@href='#collapse38']")
    SYSTEM_SECTION = (By.XPATH, "//a[@href='#collapse42']")
    REPORTS_SECTION = (By.XPATH, "//a[@href='#collapse61']")


class NavigationPanel(BasePage):
    def open_section(self, selector: Sections):
        section_selector = selector.value
        self.click_button(*section_selector)

    def open_subsection(self, selector: Sections):
        section_selector = selector.value
        self.click_button(*section_selector)

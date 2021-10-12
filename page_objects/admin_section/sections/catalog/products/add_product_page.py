from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

INPUT_PRODUCT_NAME = (By.XPATH, "//input[@id='input-name1']")
INPUT_DESCRIPTION = (By.XPATH, "//div[@class='note-editable']")
INPUT_META_TEG_TITLE = (By.XPATH, "//input[@id='input-meta-title1']")
INPUT_META_TEG_DESCRIPTION = (By.XPATH, '//textarea[@name="product_description[1][meta_description]"]')
INPUT_META_TEG_KEYWORDS = (By.XPATH, "//textarea[@name='product_description[1][meta_keyword]']")
INPUT_PRODUCT_TEG = (By.XPATH, "//input[@id='input-tag1']")
SAVE_BUTTON = (By.XPATH, '//button[@data-original-title="Save"]')
GENERAL_TAB = (By.XPATH, '//a[text()="General"]')
DATA_TAB = (By.XPATH, '//a[text()="Data"]')
INPUT_MODEL = (By.XPATH, '//input[@name="model"]')


class AddProductPageGeneral(BasePage):

    def switch_to_general_tab(self):
        self.logger.info('Переключиться на вкладку "General"')
        self.click_button(*GENERAL_TAB)

    def enter_product_name(self, product_name: str = 'Test product name'):
        self.logger.info(f'Ввести имя продукта - "{product_name}"')
        self.enter_input(*INPUT_PRODUCT_NAME, product_name)

    def enter_description(self, description: str = 'Test description 123!@#$%^'):
        self.logger.info(f'Ввести описание продукта - "{description}"')
        self.enter_input(*INPUT_DESCRIPTION, description)

    def enter_meta_teg_title(self, teg: str = "Test_meta_teg"):
        self.logger.info(f'Ввести тег заголовка - "{teg}"')
        self.enter_input(*INPUT_META_TEG_TITLE, teg)

    def enter_meta_teg_descriptions(self, meta_teg_descriptions: str = "Test meta teg descriptions"):
        self.logger.info(f'Ввести мета тег - "{meta_teg_descriptions}"')
        self.enter_input(*INPUT_META_TEG_DESCRIPTION, meta_teg_descriptions)

    def enter_meta_teg_keywords(self, keywords: str = "Test keywords"):
        self.logger.info(f'Ввести ключевые слова - "{keywords}"')
        self.enter_input(*INPUT_META_TEG_KEYWORDS, keywords)

    def enter_product_teg(self, product_tag: str = "Test product tag"):
        self.logger.info(f'Ввести тег - "{product_tag}"')
        self.enter_input(*INPUT_PRODUCT_TEG, product_tag)

    def enter_all_fields(self):
        '''
        общий метод для частого сценария
        '''
        self.enter_product_name()
        self.enter_description()
        self.enter_meta_teg_title()
        self.enter_meta_teg_descriptions()
        self.enter_meta_teg_keywords()
        self.enter_product_teg()


class AddProductPageData(BasePage):

    def switch_to_data_tab(self):
        self.logger.info('Переключиться на вкладку "Data"')
        self.click_button(*DATA_TAB)

    def enter_model(self, model: str = 'Test model'):
        self.logger.info(f'Ввести модель - {model}')
        self.enter_input(*INPUT_MODEL, model)

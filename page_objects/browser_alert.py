from page_objects.base_page import BasePage


class BrowserAlert(BasePage):
    '''
    класс для взаимодействия с алертами браузера в модальных окнах
    '''

    def accept_alert(self):
        alert = self.browser.switch_to.alert
        alert.accept()

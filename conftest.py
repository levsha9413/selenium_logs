import pytest
from selenium import webdriver
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
import logging

DRIVERS = os.path.expanduser("~/qa/drivers")
logging.basicConfig(format='%(asctime)s - %(name)s - %(message)s', level=logging.DEBUG, filename="../logs/selenium.log")

def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")  # headless режим нужен для разработчика
    parser.addoption("--browser", default="chrome", choices=["chrome", "firefox", "opera"])
    parser.addoption("--url", default="https://demo.opencart.com/")


@pytest.fixture  # делаем для url отдельную фикстуру, чтобы передавать как отдельный аргумент
def url(request):
    url = request.config.getoption("--url")
    return url


@pytest.fixture(scope="session")
def browser(request):
    _browser = request.config.getoption("--browser")  # _ добавляем для отличия от имени фикстуры
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    if _browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option('w3c', False)
        driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver",
                                  chrome_options=options,
                                  service_log_path='../logs/driver.log')
    elif _browser == "opera":
        driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver")
    elif _browser == "firefox":
        driver = webdriver.Firefox(
            executable_path=f"{DRIVERS}/geckodriver")  # без executebel_path= chrome запускается, но firefox и opera - нет

    def final():  # добавляем финалайзер, чтобы браузер закрывался после теста (chrome сам закрывается, отсальные - нет)
        driver.quit()

    request.addfinalizer(final)

    return driver  # return ставим после финалайзера, иначе финалайзер не выполнится


def find_element_with_wait(locator, selector, driver, timeout=5):
    # кастомный поиск элемента с ожидаением по существованию элемента
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((locator, selector)))
    except TimeoutException:
        raise AssertionError("Не найден элемент с селектором: {}".format(selector))

import pytest
from selenium import webdriver
import os
import logging

DRIVERS = os.path.expanduser("~/qa/drivers")
logging.basicConfig(format='%(asctime)s [%(levelname)s] %(name)s: %(message)s', level=logging.DEBUG,
                    filename="../logs/selenium.log")


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")  # headless режим нужен для разработчика
    parser.addoption("--browser", default="chrome", choices=["chrome", "firefox", "opera"])
    parser.addoption("--browser_version", action="store", default="92.0")  # version занята стандартным параметром
    parser.addoption("--url", default="https://demo.opencart.com/")
    parser.addoption("--log_level", default="INFO", choices=["DEBUG", "INFO"])
    parser.addoption("--executor", action="store", default="0.0.0.0",
                     choices=["local", "127.0.0.1"])  # указываем хост для удаленного запуска
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--videos", action="store_true", default=False)


@pytest.fixture  # выпилить если не смогу пробросить
def log_level(request):
    level = request.config.getoption("--log_level")
    if level == "INFO":
        return logging.INFO
    elif level == "DEBUG":
        return logging.DEBUG


@pytest.fixture  # делаем для url отдельную фикстуру, чтобы передавать как отдельный аргумент
def url(request):
    url = request.config.getoption("--url")
    return url


@pytest.fixture(scope="session")
def browser(request):
    _browser = request.config.getoption("--browser")  # _ добавляем для отличия от имени фикстуры
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--browser_version")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")

    if executor == "local":
        if _browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_experimental_option('w3c', False)  # магическая опция
            driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver",
                                      chrome_options=options,
                                      service_log_path='../logs/driver.log')
            if maximized:
                driver.maximize_window()
        elif _browser == "opera":
            driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver")
        elif _browser == "firefox":
            driver = webdriver.Firefox(
                executable_path=f"{DRIVERS}/geckodriver")
    else:
        driver = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub",
                                  desired_capabilities={
                                      "browserName": _browser,
                                      "browserVersion": version,
                                      "name": "my session name",
                                      "selenoid:options": {
                                          "enableVNC": vnc,
                                          "enableVideo": videos,
                                          "sessionTimeout": "60s"  # на случай отладки
                                      }})

    def final():
        driver.quit()

    request.addfinalizer(final)

    return driver  # return ставим после финалайзера, иначе финалайзер не выполнится

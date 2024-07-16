import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="Failed_Test", attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


def pytest_addoption(parse):
    parse.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture()
def setup(request):
    global driver
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        ser_obj = Service("D:\\SeleniumPython\\chromedriver-win64\\chromedriver.exe")
        driver = webdriver.Chrome(service=ser_obj)

    elif browser_name == "firefox":
        ser_obj = Service("D:\\SeleniumPython\\chromedriver-win64\\chromedriver.exe")
        driver = webdriver.Firefox(service=ser_obj)

    elif browser_name == "edge":
        ser_obj = Service("D:\\SeleniumPython\\chromedriver-win64\\chromedriver.exe")
        driver = webdriver.Edge(service=ser_obj)
    else:
        print("Enter correct Browser Name")

    driver.get("https://www.google.com/")
    request.cls.driver = driver
    yield
    driver.close()

##################### Cross Browser Testing ###############################
# @pytest.fixture(params=["chrome", "firefox", "edge"])
# def setup(request):
#     global driver
#     if request.param == "chrome":
#         ser_obj = Service("D:\\SeleniumPython\\chromedriver-win64\\chromedriver.exe")
#         driver = webdriver.Chrome(service=ser_obj)
#     elif request.param == "firefox":
#         ser_obj = Service("D:\\SeleniumPython\\chromedriver-win64\\chromedriver.exe")
#         driver = webdriver.Firefox(service=ser_obj)
#     elif request.param == "edge":
#         ser_obj = Service("D:\\SeleniumPython\\chromedriver-win64\\chromedriver.exe")
#         driver = webdriver.Edge(service=ser_obj)
#     driver.get("https://www.google.com/")
#     request.cls.driver = driver
#     yield
#     driver.close()

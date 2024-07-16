import allure
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup", "log_on_failure")
class TestData:

    @allure.severity(allure.severity_level.MINOR)
    def test_Google_Home(self):
        self.driver.find_element(By.XPATH, "//textarea[@title='Search']").send_keys("AAK Tak")
        print("This is Google page")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_M2(self):
        print(self.driver.title)
        print("this is method 2")
        assert "test" == 788;

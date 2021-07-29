import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

ch_capabilities = {
        "build" : "Porting test to LambdaTest Selenium Grid (Chrome)",
        "name" : "Porting test to LambdaTest Selenium Grid (Chrome)",
        "platform" : "Windows 10",
        "browserName" : "Chrome",
        "version" : "80.0"
}

@pytest.fixture(params=['chrome', 'firefox'], scope='class')
def init_driver(request):

    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == "firefox":
        #web_driver = webdriver.Firefox(GeckoDriverManager().install())
        web_driver = webdriver.Firefox(executable_path='core/geckodriver')
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    yield
    web_driver.close()


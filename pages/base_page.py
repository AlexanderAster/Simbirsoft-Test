from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class BasePage(object):
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    selenium_grid_url = "http://localhost:4444/wd/hub"
    capabilities = DesiredCapabilities.FIREFOX.copy()
    capabilities['platform'] = "WINDOWS"
    capabilities['version'] = "10"

class AuthPage(BasePage): 
    def __init__(self, driver,timeout=10): 
        super().__init__(driver, timeout) 
        url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
        driver.get(url) 
class OfficePage(BasePage): 
    def __init__(self, driver,timeout=10): 
        super().__init__(driver, timeout)
        url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account"
        driver.get(url)
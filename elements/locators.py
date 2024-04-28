from selenium.webdriver.common.by import By

class loginlocator:
    LOGIN_BTN = (By.XPATH,'//button[contains(text(), "Customer Login")]')
    USER_SELECT = (By.NAME,'userSelect')
    HARRY = (By.XPATH,'//*[@id="userSelect"]/option[3]')
    AUTH_BTN = (By.CLASS_NAME,'btn-default')
    POTTER_HEADER = (By.XPATH, '//span[contains(text(), "Harry Potter")]')

class cablocator:
    TRANSACTIONS_TAB = (By.XPATH, '//button[contains(@ng-class, "btnClass1")]')
    DEPOSIT_TAB = (By.XPATH, '//button[contains(@ng-class, "btnClass2")]')
    WITHDRAWL_TAB = (By.XPATH, '//button[contains(@ng-class, "btnClass3")]')
    DEPOSIT_WITHDRAWL_BTN = (By.CSS_SELECTOR, '.ng-scope .btn-default')
    BACK_BTN = (By.XPATH, '//button[contains(@ng-click, "back()")]')
    AMOUNT_FIELD = (By.XPATH, '//input[contains(@ng-model, "amount")]')
    SUCCESS_MSG = (By.CSS_SELECTOR, '.ng-scope .error.ng-binding')
    BALANCE = (By.XPATH, '//strong[normalize-space()][2]')
    TRANS_DATE_FIRST = (By.XPATH, "//tr[@id='anchor0']//td[@class='ng-binding'][1]")
    TRANS_BAL_FIRST = (By.XPATH, "//tr[@id='anchor0']//td[@class='ng-binding'][2]")
    TRANS_TYPE_FIRST = (By.XPATH, "//tr[@id='anchor0']//td[@class='ng-binding'][3]")
    TRANS_DATE_SEC = (By.XPATH, "//tr[@id='anchor1']//td[@class='ng-binding'][1]")
    TRANS_BAL_SEC = (By.XPATH, "//tr[@id='anchor1']//td[@class='ng-binding'][2]")
    TRANS_TYPE_SEC = (By.XPATH, "//tr[@id='anchor1']//td[@class='ng-binding'][3]")
    TRANS_FIRST = (By.CSS_SELECTOR, ".table #anchor0.ng-scope")
    TRANS_SEC =(By.CSS_SELECTOR, ".table #anchor1.ng-scope")
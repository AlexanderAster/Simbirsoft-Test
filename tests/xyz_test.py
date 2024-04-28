import pytest
import allure
import datetime
import time
import csv
from selenium import webdriver
from elements.locators import loginlocator,cablocator
from pages.base_page import AuthPage,OfficePage

@pytest.fixture(autouse=True,scope='session')    
def driver():
   # options = webdriver.FirefoxOptions() Отголоски непобеждённого Selenium GRID
   # driver = webdriver.Remote(selenium_grid_url,capabilities,options=options)
   driver = webdriver.Firefox()
   yield driver
   driver.quit()
@allure.title("Тест авторизации за Гарри Поттера")
def test_HarryPotter_login(driver):
   '''Вход в систему пользователем Гарри Поттер'''
   AuthPage(driver)
   driver.find_element(*loginlocator.LOGIN_BTN).click()
   driver.find_element(*loginlocator.USER_SELECT).click()
   driver.find_element(*loginlocator.HARRY).click()
   driver.find_element(*loginlocator.AUTH_BTN).click()
   driver.find_element(*loginlocator.POTTER_HEADER)

todaydate = datetime.date.today() # Получаем число фибоначчи из системной даты
day = int(todaydate.day)
Nfib = day + 1
def Fibonacci(n): 
   if n == 1:
      return 0
   elif n == 2:
      return 1
   else:
      return Fibonacci(n-1)+Fibonacci(n-2)
amount = Fibonacci(Nfib)
@allure.title("Пополнение счёта на сумму фибоначчи расчёта")
def test_deposit(driver):
   '''Пополнение счёта на сумму фибоначчи расчёта'''
   OfficePage(driver)
   driver.find_element(*cablocator.DEPOSIT_TAB).click()
   driver.find_element(*cablocator.AMOUNT_FIELD).send_keys(amount)
   driver.find_element(*cablocator.DEPOSIT_WITHDRAWL_BTN).click()
   driver.find_element(*cablocator.SUCCESS_MSG)
@allure.title("Списание со счёта на сумму фибоначчи расчёта")
def test_withdrawl(driver):
   '''Списание со счёта на сумму фибоначчи расчёта'''
   OfficePage(driver)
   driver.find_element(*cablocator.WITHDRAWL_TAB).click()
   time.sleep(1) # Система не успевает обработать переход и производит двойной депозит вместо списания.
   driver.find_element(*cablocator.AMOUNT_FIELD).send_keys(amount)
   driver.find_element(*cablocator.DEPOSIT_WITHDRAWL_BTN).click()
   driver.find_element(*cablocator.SUCCESS_MSG)
@allure.title("Проверка,что баланс равен нулю")
def test_balance(driver):
   '''Проверка,что баланс равен нулю'''
   OfficePage(driver)
   driver.refresh()
   balance = driver.find_element(*cablocator.BALANCE)
   assert balance.text == "0"
@allure.title("Проверка регистрации транзакций и их запись в csv")
def test_transactions(driver):
   '''Проверка регистрации транзакций'''
   OfficePage(driver)
   driver.find_element(*cablocator.TRANSACTIONS_TAB).click()
   try:
      driver.find_element(*cablocator.TRANS_FIRST)
   except:
      time.sleep(2) # Иногда система не успевает обработать и отобразить список транзакций
      driver.refresh()
   finally:
      first = driver.find_element(*cablocator.TRANS_BAL_FIRST)
      assert first.text == f'{amount}'
      second = driver.find_element(*cablocator.TRANS_BAL_SEC)
      assert second.text == f'{amount}'
      dateFIR = driver.find_element(*cablocator.TRANS_DATE_FIRST)
      dateSEC = driver.find_element(*cablocator.TRANS_DATE_SEC)
      sumFIR = driver.find_element(*cablocator.TRANS_BAL_FIRST)
      sumSEC = driver.find_element(*cablocator.TRANS_BAL_SEC)
      typeFIR = driver.find_element(*cablocator.TRANS_TYPE_FIRST)
      typeSEC = driver.find_element(*cablocator.TRANS_TYPE_SEC)
      with open("transactions.csv", mode="a", encoding='utf-8') as w_file:
         file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
         file_writer.writerow([f"{dateFIR.text}",f"{int(sumFIR.text)}",f"{typeFIR.text}"])
         file_writer.writerow([f"{dateSEC.text}",f"{int(sumSEC.text)}",f"{typeSEC.text}"])

# python -m pytest tests\xyz_test.py --alluredir allure-results
# python -m pytest --driver Firefox --driver-path C:{path}\geckodriver.exe tests\xyz_test.py --alluredir allure-results
# allure serve
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="class")
def browser():
	print('\nЗапускаем браузер')
	browser = webdriver.Chrome()
	browser.implicitly_wait(5)
	yield browser
	print('\nЗакрываем браузер')
	browser.quit()

@pytest.fixture(autouse=True)
def prepare_data():
	print()
	print("Какие-то критически важные процессы")

class TestMainPage():
	def test_guest_should_see_login_link(self,browser):
		browser.get(link)
		browser.find_element(By.CSS_SELECTOR, "#login_link")
	
	def test_guest_should_see_basket_link_on_the_main_page(self,browser):
		browser.get(link)
		browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
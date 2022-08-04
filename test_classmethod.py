from selenium import webdriver
from selenium.webdriver.common.by import By 
link = "http://selenium1py.pythonanywhere.com/"

class TestMethod_one_fixture():
	"""Тестовый класс с отдельным запуском браузера для каждого теста"""
	def setup_method(self):
		print('\nТест запущен. Браузер запускается...')
		self.browser = webdriver.Chrome()

	def teardown_method(self):
		print('\nТест завершён. Выполняется выход из браузера...')
		self.browser.quit()

	def test_guest_should_see_login_link(self):
		self.browser.get(link)
		self.browser.find_element(By.CSS_SELECTOR, "#login_link")
	
	def test_guest_should_see_basket_link_on_the_main_page(self):
		self.browser.get(link)
		self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

class TestMethod_Fixture():
	"""Тестовый класс с применением фикстуры @classmethod"""
	@classmethod
	def setup_class(self):
		print('\nТест-сьюит запущен. Браузер запускается...')
		self.browser = webdriver.Chrome()

	@classmethod
	def teardown_class(self):
		print('\nТест-сьюит завершён. Выполняется выход из браузера...')
		self.browser.quit()

	def test_guest_should_see_login_link(self):
		self.browser.get(link)
		self.browser.find_element(By.CSS_SELECTOR, "#login_link")
	
	def test_guest_should_see_basket_link_on_the_main_page(self):
		self.browser.get(link)
		self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
	
		
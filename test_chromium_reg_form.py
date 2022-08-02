import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestReg_Form(unittest.TestCase):
	"""Класс для тестирования заполнения формы регистрации на сайте"""
	def test_reg_1(self):		
		#Запускаем веб-драйвер и переходим на страницу
		browser = webdriver.Chrome()
		browser.get("http://suninjuly.github.io/registration1.html")
		#Код, который заполняет обязательные поля
		#Заполнение поля First name
		first_name = browser.find_element(By.CSS_SELECTOR,'[required].first')
		first_name.send_keys("Valentin")
		#Заполнение поля Last name
		last_name = browser.find_element(By.CSS_SELECTOR,'[required].second')
		last_name.send_keys("Trifonov")
		#Заполнение поля Email
		email = browser.find_element(By.CSS_SELECTOR,'[required].third')
		email.send_keys("ivan_pupkin@mail.com")

		# Отправляем заполненную форму
		button = browser.find_element(By.CSS_SELECTOR, "button.btn")
		button.click()

		# находим элемент, содержащий текст
		welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
		# записываем в переменную welcome_text текст из элемента welcome_text_elt
		welcome_text = welcome_text_elt.text

		# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
		self.assertEqual("Congratulations! You have successfully registered!",welcome_text,"Регистрация не удалась")

	def test_reg_2(self):
		#Запускаем веб-драйвер и переходим на страницу
		browser = webdriver.Chrome()
		browser.get("http://suninjuly.github.io/registration2.html")
		#Код, который заполняет обязательные поля
		#Заполнение поля First name
		first_name = browser.find_element(By.CSS_SELECTOR,'[required].first')
		first_name.send_keys("Valentin")
		#Заполнение поля Last name
		last_name = browser.find_element(By.CSS_SELECTOR,'[required].second')
		last_name.send_keys("Trifonov")
		#Заполнение поля Email
		email = browser.find_element(By.CSS_SELECTOR,'[required].third')
		email.send_keys("ivan_pupkin@mail.com")

		# Отправляем заполненную форму
		button = browser.find_element(By.CSS_SELECTOR, "button.btn")
		button.click()

		# находим элемент, содержащий текст
		welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
		# записываем в переменную welcome_text текст из элемента welcome_text_elt
		welcome_text = welcome_text_elt.text

		# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
		self.assertEqual("Congratulations! You have successfully registered!",welcome_text,"Регистрация не удалась")

	def test_reg_form(self):
		link_s = ["http://suninjuly.github.io/registration1.html",
				  "http://suninjuly.github.io/registration2.html"]

		for link in link_s:
			with self.subTest(link=link):
				#Запускаем веб-драйвер и переходим на страницу
				browser = webdriver.Chrome()
				browser.get(link)
				#Код, который заполняет обязательные поля
				#Заполнение поля First name
				first_name = browser.find_element(By.CSS_SELECTOR,'[required].first')
				first_name.send_keys("Valentin")
				#Заполнение поля Last name
				last_name = browser.find_element(By.CSS_SELECTOR,'[required].second')
				last_name.send_keys("Trifonov")
				#Заполнение поля Email
				email = browser.find_element(By.CSS_SELECTOR,'[required].third')
				email.send_keys("ivan_pupkin@mail.com")

				# Отправляем заполненную форму
				button = browser.find_element(By.CSS_SELECTOR, "button.btn")
				button.click()

				# находим элемент, содержащий текст
				welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
				# записываем в переменную welcome_text текст из элемента welcome_text_elt
				welcome_text = welcome_text_elt.text
				browser.quit()
				# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
				self.assertEqual("Congratulations! You have successfully registered!",welcome_text,\
				"Регистрация не удалась")

	

if __name__ == "__main__":
	unittest.main()

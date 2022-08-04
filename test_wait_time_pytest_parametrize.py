import pytest
import math
import time

from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.mark.main
class TestAnswerForm():
	@pytest.mark.chrome	
	@pytest.mark.parametrize('link',["https://stepik.org/lesson/236895/step/1",
									 "https://stepik.org/lesson/236896/step/1",
									 "https://stepik.org/lesson/236897/step/1",
									 "https://stepik.org/lesson/236898/step/1",
									 "https://stepik.org/lesson/236899/step/1",
									 "https://stepik.org/lesson/236903/step/1",
									 "https://stepik.org/lesson/236904/step/1",
									 "https://stepik.org/lesson/236905/step/1"])
	def test_links_answer(self,browser,link):
		"""Тест правильности работы функции генерации ответа на вопросы"""
		#Переходим по ссылке на страницу для тестирования
		browser.get(link)

		#Генерируем код ответа
		answer_number = math.log(int(time.time()))

		#Находим поле ввода ответа и вписываем вычисленный ответ
		text_area = WebDriverWait(browser,10).until(
			EC.visibility_of_element_located((By.CSS_SELECTOR,'textarea'))
			)
		text_area.send_keys(answer_number)

		#Находим кнопку для ответа и отправляем ответ
		button = WebDriverWait(browser,10).until(
			EC.element_to_be_clickable((By.CSS_SELECTOR,'button.submit-submission'))
			)
		button.click()

		#Определяем текст сообщения о корректности ответа и сравниваем с ожидаемым
		answer_message = WebDriverWait(browser,10).until(
			EC.presence_of_element_located((By.CSS_SELECTOR,'.smart-hints__hint'))
			).text
		print(f"Answer Msg = {answer_message}")
		assert "Correct!" == answer_message


@pytest.mark.subtest
def test_links_answer(browser):
		"""Тест правильности работы функции генерации ответа на вопросы"""
		#Переходим по ссылке на страницу для тестирования
		browser.get("https://stepik.org/lesson/236895/step/1")

		#Генерируем код ответа
		answer_number = math.log(int(time.time()))

		#Находим поле ввода ответа и вписываем вычисленный ответ
		text_area = WebDriverWait(browser,10).until(
			EC.visibility_of_element_located((By.CSS_SELECTOR,'textarea'))
			)
		text_area.send_keys(answer_number)

		#Находим кнопку для ответа и отправляем ответ
		button = WebDriverWait(browser,10).until(
			EC.element_to_be_clickable((By.CSS_SELECTOR,'button.submit-submission'))
			)
		button.click()

		#Определяем текст сообщения о корректности ответа и сравниваем с ожидаемым
		answer_message = WebDriverWait(browser,10).until(
			EC.presence_of_element_located((By.CSS_SELECTOR,'.smart-hints__hint'))
			).text
		print(f"Answer Msg = {answer_message}")
		assert "Correct!" == answer_message
	
		

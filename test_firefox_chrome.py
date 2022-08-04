from selenium import webdriver

def test_browser_option(browser):	
	# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
	browser.get("https://stepik.org/lesson/25969/step/8")
	assert False
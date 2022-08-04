import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
	parser.addoption('--browser_name',action='store',default="chrome",
					 help="Выберите браузер: chrome или firefox")
	parser.addoption('--language',action='store',default="ru",
					 help="Доступные языки интерфейса браузера: \'ru\', \'en\'.")

@pytest.fixture(scope = "function")
def browser(request):
	browser_name = request.config.getoption("browser_name")
	user_language = request.config.getoption("language")
	if user_language not in ["ru", "en"]:
		raise pytest.UsageError("\n--language  может принимать следующие значения: \'ru\', \'en\'.")

	print(f"\nЯзык интерфейса: {user_language}")

	browser = None
	if browser_name == "chrome":		
		print('\n**_Тесты проводятся в браузере \'Google Chrome\'_**')
		options = Options()
		options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
		options.add_argument('--ignore-certificate-errors')
		options.add_argument('--ignore-ssl-errors')
		browser = webdriver.Chrome(options=options,\
								   service=Service(ChromeDriverManager().install()))
	elif browser_name == "firefox":
		print('\n**_Тесты проводятся в браузере \'Firefox\'_**')
		profile = webdriver.FirefoxProfile()
		profile.accept_untrusted_certs = True
		profile.set_preference("intl.accept_languages", user_language)
		browser = webdriver.Firefox(firefox_profile=profile,\
								    service=Service(GeckoDriverManager().install()))

	else:
		raise pytest.UsageError("\n--browser_name может принимать следующие значения: \'chrome\', \'firefox\'.")	
	yield browser
	print(f'\n**_ Браузер \'{browser_name}\' был закрыт_**')
	browser.quit()
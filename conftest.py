import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help='Choose browser: chrome or firefox')
    parser.addoption('--language',
                     action='store',
                     default='en',
                     help='Choose language: ru/es/fr/fi/...')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')
    if browser_name == 'chrome':
        print('\nstart chrome browser for test..')
        options_chrome = OptionsChrome()
        options_chrome.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options_chrome)
    elif browser_name == 'firefox':
        print('\nstart firefox browser for test..')
        options_firefox = OptionsFirefox()
        options_firefox.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    print('\nquit browser..')
    browser.quit()

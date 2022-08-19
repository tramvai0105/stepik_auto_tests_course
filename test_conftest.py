import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
import time

urls = ['https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1']

final = ""

@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome()
    yield browser
    print(final)
    browser.quit()

@pytest.mark.parametrize('url', urls)
def test_guest_should_see_login_link(browser, url):
    global final
    link = url
    browser.get(link)
    browser.implicitly_wait(10)
    browser.find_element(By.TAG_NAME, 'textarea').send_keys(str(math.log(int(time.time()))))
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission'))).click()
    answer = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint'))).text
    try:
        assert 'Correct!' == answer
    except AssertionError:
        final += answer  # собираем ответ про Сов с каждой ошибкой

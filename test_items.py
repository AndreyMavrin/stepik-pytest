import time
from selenium.webdriver.common.by import By


def test_goods_page_has_add_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    add_to_basket = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert add_to_basket, 'кнопка добавления товара отсутвует'

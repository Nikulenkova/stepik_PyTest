import time
import pytest


def test_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    time.sleep(2)

    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button, "Кнопка 'Добавить в корзину' не найдена!"

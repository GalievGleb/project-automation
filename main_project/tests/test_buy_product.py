import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment import Payment_page


@pytest.mark.order(3)
def test_buy_product_1():  # создаем метод
    options = Options()
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver = webdriver.Chrome(
        executable_path='C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\chromedriver.exe',
        chrome_options=options)  # Указали директорию в которой находится хром драйвер, для того чтобы мы могли обращаться к браузеру гугл хром

    print("\nStart Test 1")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_1()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    # cip = Client_information_page(driver)
    # cip.input_information()
    #
    # p = Payment_page(driver)
    # p.click_finish_button()
    #
    # f = Finish_page(driver)
    # f.finish()

    print("Finish Test 1")
    time.sleep(1)


@pytest.mark.order(3)
def test_buy_product_2():  # создаем метод
    options = Options()
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver = webdriver.Chrome(
        executable_path='C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\chromedriver.exe',
        chrome_options=options)  # Указали директорию в которой находится хром драйвер, для того чтобы мы могли обращаться к браузеру гугл хром

    print("\nStart Test 2")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_2()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    print("Finish Test 2")
    time.sleep(1)


@pytest.mark.order(2)
def test_buy_product_3():  # создаем метод
    options = Options()
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver = webdriver.Chrome(
        executable_path='C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\chromedriver.exe',
        chrome_options=options)  # Указали директорию в которой находится хром драйвер, для того чтобы мы могли обращаться к браузеру гугл хром

    print("\nStart Test 3")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_3()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    print("Finish Test 3")
    time.sleep(1)

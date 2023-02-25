import time

import allure
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

@allure.description("Test link about")
def test_link_about():  # создаем метод
    options = Options()
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver = webdriver.Chrome(
        executable_path='C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\chromedriver.exe',
        chrome_options=options)  # Указали директорию в которой находится хром драйвер, для того чтобы мы могли обращаться к браузеру гугл хром

    print("\nStart Test")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_menu_about()

    print("Finish Test")
    time.sleep(1)

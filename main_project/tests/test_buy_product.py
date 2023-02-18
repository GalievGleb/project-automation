import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from pages.login_page import Login_page
from pages.main_page import Main_page


def test_select_product():  # создаем метод
    options = Options()
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver = webdriver.Chrome(
        executable_path='C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\chromedriver.exe',
        chrome_options=options)  # Указали директорию в которой находится хром драйвер, для того чтобы мы могли обращаться к браузеру гугл хром

    print("Start Test")

    login = Login_page(driver)
    login.authorization()
    mp = Main_page(driver)
    mp.select_product()

    time.sleep(5)

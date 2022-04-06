from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36')


def authorization():
    url = 'https://passport.yandex.ru/auth/'
    path_driver = os.path.join(os.getcwd(), 'chromedriver.exe')
    driver = webdriver.Chrome(executable_path=path_driver, options=options)
    try:
        driver.get(url)
        time.sleep(1)
        login_input = driver.find_element_by_id('passp-field-login')
        login_input.clear()
        login_input.send_keys('filimonovicholeg05')
        time.sleep(1)
        button = driver.find_element_by_id('passp:sign-in').click()
        time.sleep(1)
        password = driver.find_element_by_name('passwd')
        password.clear()
        try:
            with open('password', encoding='utf-8-sig') as file:
                password.clear()
                password.send_keys(file.read())
                driver.implicitly_wait(3)
                button_exit = driver.find_element_by_id('passp:sign-in').click()
                driver.implicitly_wait(3)
                data_birthday = driver.find_element_by_class_name('AdditionalPersonalInfo-birthday').click()
                day = driver.find_element_by_id('birthday-day')
                time.sleep(2)
                day.send_keys('05')
                month = driver.find_element_by_class_name('Select2-Control')
                month.send_keys(Keys.ENTER)
                time.sleep(2)
                month.send_keys(Keys.ARROW_DOWN)
                time.sleep(2)
                month.send_keys('н')
                time.sleep(2)
                month.send_keys(Keys.ENTER)
                year = driver.find_element_by_id('birthday-year')
                year.send_keys('1991')
                time.sleep(2)
                city = driver.find_element_by_id('city')
                city.send_keys('Калининград')
                driver.implicitly_wait(3)
                city.send_keys(Keys.ENTER)
                time.sleep(5)
                url_profile = driver.current_url

        except FileNotFoundError as er:
            print(er)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
        return url_profile

print(authorization())
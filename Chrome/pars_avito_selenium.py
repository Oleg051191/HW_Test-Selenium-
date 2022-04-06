import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://www.avito.ru/kaliningrad/avtomobili/mazda-ASgBAgICAUTgtg3mmCg?radius=200'
path_driver = os.path.join(os.getcwd(), 'chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36')
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(executable_path=path_driver, options=options)

# driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
def get_site():
    # Функция, переходящая на сайт Авито с автомобилем Мазда с определенными параметрами
    try:
        driver.get(url)
        driver.implicitly_wait(15)
        model = driver.find_elements_by_class_name('popular-rubricator-link-Hrkjd')[4].click()
        driver.implicitly_wait(15)
        model_year = driver.find_elements_by_class_name('popular-rubricator-link-Hrkjd')[5].click()
        driver.implicitly_wait(15)
        sort_data = driver.find_element_by_css_selector("option[data-marker='option(104)']").click()
        driver.implicitly_wait(5)
        city_kaliningrad = driver.find_elements_by_xpath("//*[@class='checkbox-label-OmC9T text-text-LurtD text-size-s-BxGpL text-color-default-_QyDA']")[2]
        city_kaliningrad.click()
        driver.implicitly_wait(5)
        price_from = driver.find_element_by_css_selector("input[data-marker='price/from']")
        price_from.send_keys('1500000')
        driver.implicitly_wait(5)
        price_to = driver.find_element_by_css_selector("input[data-marker='price/to']")
        price_to.send_keys('3500000')
        driver.implicitly_wait(5)
        driver.find_element_by_class_name('styles-box-rgPSN').click()
        driver.implicitly_wait(5)
        print(f"Current URL: {driver.current_url}")
    except Exception as er:
        print(er)


def info_auto():
    # Функция, получающая информацию о автомобилях переходя по ссылкам
    try:
        get_site()
        items = driver.find_elements_by_xpath("//div[@data-marker='item']")[:3]
        info_automobile = {'Модель, год': [], 'Цена': [], 'Пробег': [], 'Количество владельцев': [],
                           'Двигатель': [],'Ссылка на Авито': []
                           }
    ## Информация о автомобилях
        for item in items:
            item.click()
            time.sleep(3)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(3)
            href = driver.current_url
            model = driver.find_element_by_class_name('title-info-title-text').text
            price = driver.find_element_by_xpath("//span[@itemprop='price']").text
            km = driver.find_elements_by_class_name('item-params-list-item')[2].text[8:]
            owner = driver.find_elements_by_class_name('item-params-list-item')[4].text[17:]
            engine = driver.find_elements_by_class_name('item-params-list-item')[6].text[11:]
            info_automobile['Модель, год'] += [model]
            info_automobile['Цена'] += [f"{price} р."]
            info_automobile['Пробег'] += [km]
            info_automobile['Количество владельцев'] += [owner]
            info_automobile['Двигатель'] += [engine]
            info_automobile['Ссылка на Авито'] += [href]
            time.sleep(3)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
    except Exception as er:
        print(er)
    finally:
        driver.quit()
        driver.close()
        return info_automobile

if __name__ == '__main__':
    print(info_auto())
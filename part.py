import time                                                                                                             # Импортируем модуль со временем
import csv                                                                                                              # Импортируем модуль csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = "https://colorlon.ru/catalog/lyustry"
driver.get(url)
time.sleep(3)

lustras = driver.find_elements(By.CSS_SELECTOR, 'div.product-card')

parsed_data = []

for lustra in lustras:
    try:
        title_element = lustra.find_element(By.CSS_SELECTOR, 'a.product-card__name')
        title = title_element.text
        link = title_element.get_attribute('href')
        try:
            salary = lustra.find_element(By.CSS_SELECTOR, 'div.product-card__price').text
        except:
            salary = "Не указана"

    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

    parsed_data.append([title, salary, link])

driver.quit()

with open("kl.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название люстры', 'цена', 'Ссылка'])
    writer.writerows(parsed_data)
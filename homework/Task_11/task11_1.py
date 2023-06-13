# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep


sbis_site = 'https://sbis.ru/'
driver = webdriver.Chrome()
try:
    driver.get(sbis_site)
    sleep(1)
    button_contacts = driver.find_element(By.CSS_SELECTOR, ".sbisru-Header__menu-item>a[href='/contacts']")
    sleep(1)
    button_contacts.click()
    sleep(1)
    image_tensor = driver.find_element(By.CSS_SELECTOR, "#contacts_clients > div.sbis_ru-container > div > div > "
                                                        "div.s-Grid-col.s-Grid-col--4 > div > a > img")
    image_tensor.click()
    driver.switch_to.window(driver.window_handles[1])
    sleep(2)
    action = ActionChains(driver)
    news = driver.find_element(By.CSS_SELECTOR, ".tensor_ru-Index__block4-content")
    action.move_to_element(news)
    action.perform()
    sleep(5)
    news_title = driver.find_element(By.CSS_SELECTOR, ".tensor_ru-Index__block4-content .tensor_ru-Index__card-title")
    assert news_title.text == 'Сила в людях'
    print("Заголовок новости - верный: 'Сила в людях'")
    news_more = driver.find_element(By.CSS_SELECTOR, "#container > div.tensor_ru-content_wrapper > div > "
                                                     "div.tensor_ru-Index__block4-bg > div > div > div:nth-child(1) > "
                                                     "div > p:nth-child(4) > a")
    sleep(2)
    news_more.click()
    sleep(1)
    url = 'https://tensor.ru/about'
    get_url = driver.current_url
    assert get_url == url
    print("Верный адрес при переходе в блоке новости в 'Подробнее': 'https://tensor.ru/about'")
finally:
    driver.quit()

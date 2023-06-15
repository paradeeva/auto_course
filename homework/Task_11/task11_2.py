# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from time import sleep


sbis_site = 'https://fix-online.sbis.ru/'
driver = webdriver.Chrome()
try:
    driver.get(sbis_site)
    sleep(5)
    user_login, user_password = 'релакс', 'релакс123'
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)
    sleep(5)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)
    driver.maximize_window()
    url = 'https://fix-online.sbis.ru/page/dialogs'
    sleep(5)
    driver.get(url)
    sleep(5)
    driver.switch_to.window(driver.window_handles[0])
    get_url = driver.current_url
    assert get_url == url
    print('Адрес сайта верный: "https://fix-online.sbis.ru/page/dialogs"')
    # action_chains = ActionChains(driver)
    button_plus = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    sleep(1)
    button_plus.click()
    sleep(2)
    message_recipient = driver.find_element(By.XPATH, "//*[@id='popup']/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div/div/div/div[2]/input")
    message_recipient.click()
    sleep(1)
    message_recipient.send_keys("Старшова")
    sleep(5)
    contact = driver.find_element(By.CSS_SELECTOR, '[title = "Старшова Лилия"]')
    driver.execute_script("return arguments[0].scrollIntoView(true);", contact)
    contact.click()
    sleep(2)
    text_message = driver.find_element(By.CSS_SELECTOR, "[data-qa='textEditor_slate_Field']")
    sleep(2)
    text = 'Задача 2023'
    text_message. send_keys(text)
    button_sending = driver.find_element(By.CSS_SELECTOR, "[data-qa='msg-send-editor__send-button']")
    button_sending.click()
    sleep(2)
    message_registry = driver.find_element(By.CSS_SELECTOR, "[data-qa='msg-dialogs-item__addressee']")
    assert message_registry.text == "Старшова Лилия"
    print("Сообщение 'Старшова Лилия' отображается в реестре")
    message_registry.click()
    sleep(5)
    button_message_del = driver.find_element(By.CSS_SELECTOR, '.controls-Toolbar_content [data-qa="remove"]')
    sleep(5)
    button_message_del.click()
    try:
        message_registry = driver.find_element(By.CSS_SELECTOR, "[data-qa='msg-dialogs-item__addressee']")
        raise Exception
    except Exception:
        print("Сообщение 'Старшова Лилия' удалено из реестра")
finally:
    driver.quit()

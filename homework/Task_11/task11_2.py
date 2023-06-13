# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
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
    action_chains = ActionChains(driver)
    new_message = driver.find_element(By.XPATH, '//*[@id="wasaby-content"]/div/div/div[2]/div[3]/div/div/div[1]/div/'
                                                'div[2]/div/div/div/div[2]/a[10]/span[3]')
    new_message.click()
    sleep(2)
    action_chains.double_click(new_message).perform()
    sleep(2)
    action_chains.double_click(new_message).perform()
    sleep(2)
    message_recipient = driver.find_element(By.XPATH, "//input[@tabindex='0']")
    recipient = 'Старшова'
    message_recipient.send_keys(recipient, Keys.ENTER)
    sleep(2)
    text_message = driver.find_element(By.XPATH, "//p[@class='textEditor_Viewer__Paragraph']")
    text = 'Задача'
    text_message.send_keys(text, Keys.ENTER)
    button = driver.find_element(By.CSS_SELECTOR, "//*[@id='DropArea__overlaidElement__40b41703-332f-4f3d-b203-9aab1e30da15']/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/div[3]/div/span/span" )
    button.click()
    message_registry = driver.find_element(By.XPATH,"//*[@id='wasaby-content']/div/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div[1]/div/div/div[2]/a[10]/span[3]")
    action_chains.double_click(message_registry).perform()
    message = driver.find_element(By.CSS_SELECTOR, "#wasaby-content > div > div > div.page-Controller.bodyContent__zIndex-context > div.ws-flexbox.ws-flex-column.sabyPage-MainLayout.controls-BlockLayout_background.ws-site-width-1024.page-Controller__content.controls-hint-area > div > div > div.sabyPage-MainLayout__workspaceWrapper.controls-Popup__dialog-target-container.sabyPage-MainLayout__workspaceWrapper_contrast.ws-flexbox.ws-flex-column.ws-flex-grow-1.ws-flex-shrink-1.sabyPage-MainLayout__content > div.sabyPage-MainLayout__workspace.ws-flexbox.ws-flex-grow-1.ws-flex-shrink-1.ws-flex-column > div.sabyPage-MainLayout__middle.ws-flexbox.SbisEnvUI-ParkingBody_same-background > div > div > div.controls-MasterDetail_details.controls-MasterDetail_details-contrast.ws-flexbox.ws-flex-grow-1 > div > div.layout-Browser.controls_Layout_theme-default.msg-dialogs-detail__layout > div.layout-Browser__content.layout-Browser__content > div > div > div.controls-Scroll-ContainerBase.controls_scroll_theme-default.controls-Scroll__content.controls-Scroll__content_hideNativeScrollbar.controls-Scroll__content_hideNativeScrollbar_ff-ie-edge.controls-Scroll-ContainerBase__scroll_vertical.controls-Scroll-ContainerBase__scrollPosition-regular.controls-Scroll-Container__base.controls-BlockLayout__blockGroup.undefined > div > div > div > div.controls-BaseControl__viewContainer.controls-BaseControl__View_5f4c237c-efe2-4764-9c77-26ce4095c0b2 > div.controls-ListViewV.controls_list_theme-default.controls-ListView_default.controls-itemActionsV_menu-hidden > div.controls-ListViewV__itemsContainer.controls-BaseControl_showActions.controls-BaseControl_showActions_onhover.controls-BaseControl_hover_enabled.controls-BaseControl__itemsContainer_5f4c237c-efe2-4764-9c77-26ce4095c0b2 > div:nth-child(1) > div.controls-ListView__itemContent.controls-ListView__item_default-topPadding_s.controls-ListView__item_default-bottomPadding_s.controls-ListView__item-rightPadding_null.controls-ListView__itemContent_withCheckboxes.controls-ListView__itemContent_withCheckboxes_default > div.msg-dialogs-item.ws-flexbox.ws-flex-column.msg-dialogs-item_unread > div.ws-flexbox.ws-align-items-start.msg-entity-content.msg-entity-content_outgoing.msg-entity-content_indent_m.msg-dialogs-item__content > div.msg-dialogs-item__content-inner.msg-entity-content__inner.ws-flex-shrink-1.ws-flex-grow-1 > div > div.msg-entity-text.msg-entity_font_croppless.richEditor_richContentRender_fontSize-m_theme-default.controls_RichEditor_theme-default.richEditor_richContentRender_theme-default.richEditor_richContentRender.richEditor_richContentRender_lineHeight-s.richEditor_richContentRender_colorPalette-first.richEditor_richContentRender_readOnly.msg-dialogs-item__message-text.msg-entity-text_normalized.controls-List_DragNDrop__notDraggable.ws-flex-shrink-1.msg-entity-expander__content.ws-flex-grow-1.ws-flex-shrink-1 > p")
    assert message.text == "Задача"
finally:
    driver.quit()

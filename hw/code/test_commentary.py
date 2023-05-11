import pytest

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from ui.pages.base_page import BasePage, WrongValue, PageNotOpenedExeption, ElementCheckException
from ui.pages.base_case import BaseCase, cookies, credentials
from ui.pages.article_page import ArticlePage


class TestCommentariesUnauthPost(BaseCase):
    authorize=False

    def test_alert_check(self):
        page = ArticlePage(self.driver, 1)

        form = page.find((By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div/div[1]'))
        form.send_keys('Test commentary')
        page.click((By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div'))

        if not page.exist((By.XPATH, '//div[text()=\'Для отправки комментариев нужно авторизироваться\']')):
            raise ElementCheckException('No alert message after trying to post')

    def test_check_no_commentary(self):
        page = ArticlePage(self.driver, 1)

        commentary_text = 'Test commentary'
        i = 1
        while page.exist((By.XPATH, f'//div[text()=\'{commentary_text + str(i)}\']')):
            i = i + 1

        form = page.find((By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div/div[1]'))
        form.send_keys(commentary_text + str(i))
        page.click((By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div'))

        page.refresh()

        if page.exist((By.XPATH, f'//div[text()=\'{commentary_text + str(i)}\']')):
            raise ElementCheckException('Commentary posted if unauthorized')


class TestCommentariesReplyBox(BaseCase):
    authorize=True
    
    def test_opening_reply_box(self):
        page = ArticlePage(self.driver, 4)
        
        reply_button = page.find((By.XPATH, '//div[text()=\'Ответить\']'))
        parent = reply_button.find_element(By.XPATH,'..')
        try:
            reply_form = parent.find_element(By.ID,'title')
            raise ElementCheckException('Reply form is opened without clicking')
        except NoSuchElementException:
            pass

        reply_button.click()
        try:
            reply_form = parent.find_element(By.ID,'title')
        except NoSuchElementException:
            raise ElementCheckException('Reply form isnt opened after clicking')
    
    def test_closing_reply_box(self):
        page = ArticlePage(self.driver, 4)
        
        reply_button = page.find((By.XPATH, '//div[text()=\'Ответить\']'))
        parent = reply_button.find_element(By.XPATH,'..')
        try:
            reply_form = parent.find_element(By.ID,'title')
            raise ElementCheckException('Reply form is opened without clicking')
        except NoSuchElementException:
            pass

        reply_button.click()
        reply_button.click()
        try:
            reply_form = parent.find_element(By.ID,'title')
            raise ElementCheckException('Reply form isnt opened after clicking')
        except NoSuchElementException:
            pass
    

class TestCommentariesPost(BaseCase):
    authorize=True
    
    def test_enter_post(self):
        page = ArticlePage(self.driver, 1)
        
        commentary_text = 'Test commentary'
        i = 1
        while page.exist((By.XPATH, f'//div[text()=\'{commentary_text + str(i)}\']')):
            i = i + 1
        commentary_text = commentary_text + str(i)

        form = page.find((By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div/div[1]'))
        form.send_keys(commentary_text)
        form.send_keys(Keys.ENTER)

        if not page.exist((By.XPATH, f'//div[text()=\'{commentary_text}\']')):
            raise ElementCheckException('Commentary not posted by pressing enter')

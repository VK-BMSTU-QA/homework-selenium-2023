import pytest

from test_login import BaseCase, MainPage, cookies, credentials
from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage, WrongValue, PageNotOpenedExeption, ElementCheckException

from test_article_watch import ArticlePage

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

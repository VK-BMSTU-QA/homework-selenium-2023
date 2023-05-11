import time
import pytest

from selenium.webdriver.common.by import By

from ui.pages.base_page import WrongValue, PageNotOpenedExeption, ElementCheckException
from ui.pages.base_case import BaseCase, cookies, credentials
from ui.pages.main_page import MainPage
from ui.pages.author_page import AuthorPage
from selenium.webdriver.support.ui import Select


class TestSubscribe(BaseCase):
    authorize = True

    def test_sub_unsub(self):
        timeout = 20
        page = AuthorPage(self.driver, "boris")

        elem = page.find((By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[4]/div[2]'), timeout)
        subs_count = int(elem.text.split()[0])
        if page.exist((By.XPATH, f'//div[text()=\'Подписаться\']'), timeout):
            page.click((By.XPATH, f'//div[text()=\'Подписаться\']'), timeout)
            cur_elem = page.find((By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[4]/div[2]'), timeout)
            cur_subs_count = int(cur_elem.text.split()[0])
            if subs_count + 1 != cur_subs_count:
                raise ElementCheckException("Count of subs dont increase")
            if not page.exist(By.XPATH, f'//div[text()=\'Вы подписаны\']'):
                raise ElementCheckException("Button \"Отписаться\" did not appear")
        elif page.exist((By.XPATH, f'//div[text()=\'Вы подписаны\']'), timeout):
            page.click((By.XPATH, f'//div[text()=\'Вы подписаны\']'), timeout)
            cur_elem = page.find((By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[4]/div[2]'), timeout)
            cur_subs_count = int(cur_elem.text.split()[0])
            if subs_count - 1 != cur_subs_count:
                raise ElementCheckException("Count of subs dont decrease")
            if not page.exist(By.XPATH, f'//div[text()=\'Вы подписаны\']'):
                raise ElementCheckException("Button \"Подписаться\" did not appear")
        else:
            raise ElementCheckException("Subscribe/Unsubscribe button dont exist")

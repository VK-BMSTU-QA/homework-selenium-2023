import time
import pytest

from selenium.webdriver.common.by import By

from ui.pages.base_page import WrongValue, PageNotOpenedExeption, ElementCheckException
from ui.pages.base_case import BaseCase, cookies, credentials
from ui.pages.main_page import MainPage
from ui.pages.create_article_page import CreateArticlePage
from ui.pages.edit_article_page import EditArticlePage
from selenium.webdriver.support.ui import Select


class TestAricleMainPageClickCreate(BaseCase):
    authorize = True

    def test_new_title_click(self):
        timeout = 20
        page = MainPage(self.driver)

        url = 'https://95.163.213.142/new_article'
        title_xpath = '//div[text()=\'Новая статья\']'

        page.click((By.XPATH, title_xpath), timeout)
        if not page.driver.current_url.startswith(url):
            raise PageNotOpenedExeption(f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')


class TestArticlCreate(BaseCase):
    authorize = True

    def test_category_selected(self):
        timeout = 20
        page = CreateArticlePage(self.driver)
        select_menu = Select(page.find((By.CLASS_NAME, "select_menu"), timeout))
        text_category = 'Видео'
        select_menu.select_by_visible_text(text_category)
        new_value = select_menu.first_selected_option.get_attribute("value")

        if new_value != text_category:
            raise ElementCheckException('Category dont selected')

    def test_tag_selected(self):
        timeout = 20
        page = CreateArticlePage(self.driver)
        time.sleep(1)
        page.refresh()
        select_tag = Select(page.find((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/select"), timeout))
        text_tag = 'Торговля'
        select_tag.select_by_visible_text(text_tag)

        title_xpath = '/html/body/div[2]/div[2]/div/div[1]/div/div'
        text_el = page.find((By.XPATH, title_xpath), timeout)
        text_el_value = text_el.text

        if text_el_value != text_tag:
            raise ElementCheckException('Tag dont selected')

    def test_tag_delete(self):
        timeout = 20
        page = CreateArticlePage(self.driver)
        time.sleep(1)
        page.refresh()

        select_tag = Select(page.find((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/select"), timeout))
        select_tag.select_by_index(2)
        select_tag.select_by_index(3)

        title_xpath = '/html/body/div[2]/div[2]/div/div[1]/div/div'
        page.click((By.XPATH, title_xpath), timeout)

        row_div = page.find((By.CLASS_NAME, 'row.article_edit__tags_row'), timeout)
        tags_count = len(list(row_div.find_elements(By.TAG_NAME, 'div')))

        if tags_count != 1:
            raise ElementCheckException('Tag dont deleted. Tags count == ', tags_count)

    def test_tag_delete_message(self):
        timeout = 20
        page = CreateArticlePage(self.driver)
        time.sleep(1)
        page.refresh()

        select_tag = Select(page.find((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/select"), timeout))
        select_tag.select_by_index(2)
        select_tag.select_by_index(3)
        select_tag.select_by_index(4)

        row_div = page.find((By.CLASS_NAME, 'row.article_edit__tags_row'), timeout)
        divs = list(row_div.find_elements(By.TAG_NAME, 'div'))
        tags_count = len(divs)

        i = 0
        while i < tags_count:
            tag_xpath = '/html/body/div[2]/div[2]/div/div[1]/div/div'
            page.click((By.XPATH, tag_xpath), timeout)
            i += 1

        if not page.exist((By.XPATH, f'//div[text()=\'Теги не выбраны\']')):
            raise ElementCheckException('Tag dont deleted')

    def test_publish_all_fill(self):
        timeout = 20
        page = CreateArticlePage(self.driver)
        time.sleep(1)
        page.refresh()

        select_tag = Select(page.find((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/select"), timeout))
        select_tag.select_by_index(2)

        title_xpath = '/html/body/div[2]/div[2]/div/div[1]/div/div'
        page.click((By.XPATH, title_xpath), timeout)

        title = 'a'
        description = 'a'
        body = 'a'

        form = page.find((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]'))
        form.send_keys(title)

        form = page.find((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[2]'))
        form.send_keys(description)

        form = page.find((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]'))
        form.send_keys(body)

        page.click((By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/div'), timeout)

        url = 'https://95.163.213.142/feed'
        if not page.driver.current_url.startswith(url):
            raise PageNotOpenedExeption(f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def test_publish_without_description(self):
        timeout = 20
        page = CreateArticlePage(self.driver)
        time.sleep(1)
        page.refresh()

        select_tag = Select(page.find((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/select"), timeout))
        select_tag.select_by_index(2)

        title_xpath = '/html/body/div[2]/div[2]/div/div[1]/div/div'
        page.click((By.XPATH, title_xpath), timeout)

        title = 'a'
        body = 'a'

        form = page.find((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]'))
        form.send_keys(title)

        form = page.find((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]'))
        form.send_keys(body)

        page.click((By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/div'), timeout)

        url = 'https://95.163.213.142/feed'
        if not page.driver.current_url.startswith(url):
            raise PageNotOpenedExeption(f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def test_publish_without_title(self):
        timeout = 20
        page = CreateArticlePage(self.driver)
        time.sleep(1)
        page.refresh()

        select_tag = Select(page.find((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/select"), timeout))
        select_tag.select_by_index(2)

        title_xpath = '/html/body/div[2]/div[2]/div/div[1]/div/div'
        page.click((By.XPATH, title_xpath), timeout)

        body = 'a'

        form = page.find((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]'))
        form.send_keys(body)

        page.click((By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/div'), timeout)

        error_text = 'Необходим заголовок'
        if not page.exist((By.XPATH, f'//div[text()=\'{error_text}\']')):
            raise ElementCheckException('Commentary not posted by pressing enter')

    def test_publish_without_all(self):
        timeout = 20
        page = CreateArticlePage(self.driver)
        time.sleep(1)
        page.refresh()

        select_tag = Select(page.find((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/select"), timeout))
        select_tag.select_by_index(2)

        title_xpath = '/html/body/div[2]/div[2]/div/div[1]/div/div'
        page.click((By.XPATH, title_xpath), timeout)

        page.click((By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/div'), timeout)

        error_text = 'Вы не можте сохранить пустую статью'
        if not page.exist((By.XPATH, f'//div[text()=\'{error_text}\']')):
            raise ElementCheckException('Commentary not posted by pressing enter')


class TestArticlEdit(BaseCase):
    authorize = True

    def test_click_edit_aricle_button(self):
        timeout = 20
        page = MainPage(self.driver)

        url = 'https://95.163.213.142/article/'
        edit_xpath = '/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]'

        page.click((By.XPATH, edit_xpath), timeout)

        if not page.driver.current_url.startswith(url) or not page.driver.current_url.endswith('/edit/'):
            raise PageNotOpenedExeption(f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def test_category_update(self):
        timeout = 20
        page = EditArticlePage(self.driver, 1)
        select_menu = Select(page.find((By.CLASS_NAME, "select_menu"), timeout))
        text_category = 'Видео'
        select_menu.select_by_visible_text(text_category)
        new_value = select_menu.first_selected_option.get_attribute("value")

        if new_value != text_category:
            raise ElementCheckException('Category dont selected')

    def test_tag_add_update(self):
        timeout = 20
        page = EditArticlePage(self.driver, 1)
        time.sleep(1)
        page.refresh()

        select_tag = Select(page.find((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/select"), timeout))
        text_tag = 'Торговля'
        select_tag.select_by_visible_text(text_tag)

        row_div = page.find((By.CLASS_NAME, 'row.article_edit__tags_row'), timeout)
        divs = list(row_div.find_elements(By.TAG_NAME, 'div'))
        last_div = divs[len(divs) - 1]
        last_div_text = last_div.text

        if text_tag != last_div_text:
            raise ElementCheckException('Tag dont selected')

    def test_tag_update_delete(self):
        timeout = 20
        page = EditArticlePage(self.driver, 1)
        time.sleep(1)
        page.refresh()

        select_tag = Select(page.find((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/select"), timeout))
        select_tag.select_by_index(2)
        select_tag.select_by_index(3)

        title_xpath = '/html/body/div[2]/div[2]/div/div[1]/div/div'
        page.click((By.XPATH, title_xpath), timeout)

        row_div = page.find((By.CLASS_NAME, 'row.article_edit__tags_row'), timeout)
        divs = list(row_div.find_elements(By.TAG_NAME, 'div'))
        tags_count = len(divs)

        if tags_count != 1:
            raise ElementCheckException('Tag dont deleted')

    def test_tag_update_delete_all(self):
        timeout = 20
        page = EditArticlePage(self.driver, 1)
        time.sleep(1)
        page.refresh()

        select_tag = Select(page.find((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/select"), timeout))
        select_tag.select_by_index(2)

        row_div = page.find((By.CLASS_NAME, 'row.article_edit__tags_row'), timeout)
        divs = list(row_div.find_elements(By.TAG_NAME, 'div'))
        tags_count = len(divs)

        i = 0
        while i < tags_count:
            tag_xpath = '/html/body/div[2]/div[2]/div/div[1]/div/div'
            page.click((By.XPATH, tag_xpath), timeout)
            i += 1

        if not page.exist((By.XPATH, f'//div[text()=\'Теги не выбраны\']')):
            raise ElementCheckException('Tag dont deleted')

    def test_edit_all_fill(self):
        timeout = 20
        page = EditArticlePage(self.driver, 1)
        time.sleep(1)
        page.refresh()

        select_tag = Select(page.find((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/select"), timeout))
        select_tag.select_by_index(2)

        title_xpath = '/html/body/div[2]/div[2]/div/div[1]/div/div'
        page.click((By.XPATH, title_xpath), timeout)

        title = 'a'
        description = 'a'
        body = 'a'

        form = page.find((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]'))
        form.send_keys(title)

        form = page.find((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[2]'))
        form.send_keys(description)

        form = page.find((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]'))
        form.send_keys(body)

        page.click((By.XPATH, f'//div[text()=\'Сохранить\']'), timeout)

        url = 'https://95.163.213.142/article/' + str(1) + '/edit/'
        if not page.driver.current_url.startswith(url):
            raise PageNotOpenedExeption(f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def test_edit_without_description(self):
        timeout = 20
        page = EditArticlePage(self.driver, 1)
        time.sleep(1)
        page.refresh()

        select_tag = Select(page.find((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/select"), timeout))
        select_tag.select_by_index(2)

        title_xpath = '/html/body/div[2]/div[2]/div/div[1]/div/div'
        page.click((By.XPATH, title_xpath), timeout)

        title = 'a'
        body = 'a'

        form = page.find((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]'))
        form.send_keys(title)

        form = page.find((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]'))
        form.send_keys(body)

        page.click((By.XPATH, f'//div[text()=\'Сохранить\']'), timeout)

        url = 'https://95.163.213.142/article/' + str(1) + '/edit/'
        if not page.driver.current_url.startswith(url):
            raise PageNotOpenedExeption(f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def test_edit_without_title(self):
        timeout = 20
        page = EditArticlePage(self.driver, 1)
        time.sleep(1)
        page.refresh()

        select_tag = Select(page.find((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/select"), timeout))
        select_tag.select_by_index(2)

        title_xpath = '/html/body/div[2]/div[2]/div/div[1]/div/div'
        page.click((By.XPATH, title_xpath), timeout)

        body = 'a'

        form = page.find((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[3]'))
        form.send_keys(body)

        page.click((By.XPATH, f'//div[text()=\'Сохранить\']'), timeout)

        error_text = 'Необходим заголовок'
        if not page.exist((By.XPATH, f'//div[text()=\'{error_text}\']')):
            raise ElementCheckException('No error message')

    def test_edit_without_all(self):
        timeout = 20
        page = EditArticlePage(self.driver, 1)
        time.sleep(1)
        page.refresh()

        page.click((By.XPATH, f'//div[text()=\'Сохранить\']'), timeout)

        error_text = 'Вы не можте сохранить пустую статью'
        if not page.exist((By.XPATH, f'//div[text()=\'{error_text}\']')):
            raise ElementCheckException('No error message')

    def test_delete_article_show(self):
        timeout = 20
        page = EditArticlePage(self.driver, 1)
        time.sleep(1)
        page.refresh()

        page.click((By.CLASS_NAME, 'article_edit__delete_button'), timeout)

        warning_text = 'Удалить статью?'
        yes_button = 'Да'
        no_button = 'Нет'
        if not page.exist((By.XPATH, f'//div[text()=\'{warning_text}\']')):
            raise ElementCheckException('No warning message')
        if not page.exist((By.XPATH, f'//div[text()=\'{yes_button}\']')):
            raise ElementCheckException('No yes button')
        if not page.exist((By.XPATH, f'//div[text()=\'{no_button}\']')):
            raise ElementCheckException('No no button')
    def test_delete_article(self):
        timeout = 20
        page = EditArticlePage(self.driver, 1)
        time.sleep(1)
        page.refresh()

        page.click((By.CLASS_NAME, 'article_edit__delete_button'), timeout)

        yes_button = 'Да'
        page.click((By.XPATH, f'//div[text()=\'{yes_button}\']'), timeout)

        url = 'https://95.163.213.142/feed'
        if not page.driver.current_url.startswith(url):
            raise PageNotOpenedExeption(f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')
        
        deletedpage = EditArticlePage(self.driver, 1)
        if not deletedpage.driver.getPageSource().contains("404"):
            raise ElementCheckException('Page dont deleted')
        
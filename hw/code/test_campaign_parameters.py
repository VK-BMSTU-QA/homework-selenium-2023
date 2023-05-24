import pytest

import time

import os

from datetime import datetime, timedelta

from selenium.webdriver.common.by import By

from ui.fixtures import get_driver
from ui.pages.base_case import BaseCase, cookies, credentials
from ui.pages.new_campaign_page import NewCampaignPage
from ui.pages.dashboard_page import DashboardPage
from ui.pages.base_page import ElementCheckException, WrongValue

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


testing_group = "https://vk.com/club220608488"
  
class TestCampaignCreationParameters(BaseCase):
     def open_creating_page(self, page):
          #writing a link
          page.click((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]'), 15)
          page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[2]/div/div[3]/div[1]/div/div[1]/div/div/input'), 15).send_keys(testing_group)
     
     
     def test_title(self, credentials):
          page = NewCampaignPage(self.driver)
          self.open_creating_page(page)
          title_input = page.wait(5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[2]/div/div[10]/div/div[2]/div/div[2]/input')))

          error_message = "Введите название кампании"
          title_input.clear()
          title_input.send_keys("a")
          title_input.send_keys(Keys.BACKSPACE)
          if not page.exist((By.XPATH, f'//div[text()="{error_message}"]')):
               raise ElementCheckException(f'No "{error_message}" message with empty title')

          error_message = "В названии кампании присутствуют некорректные символы (カ, タ)"
          title_input.clear()
          title_input.send_keys("カタ")
          if not page.exist((By.XPATH, f'//div[text()="{error_message}"]')):
               raise ElementCheckException(f'No "{error_message}" message with wrong symbols')

          title_input.clear()
          title_input.send_keys("a"*256)
          if len(title_input.get_attribute('value')) != 255:
               raise ElementCheckException(f'Max title length isnt 255')
          
     
     def test_sex(self, credentials):
          page = NewCampaignPage(self.driver)
          self.open_creating_page(page)

          page.click((By.XPATH, '//div[@data-scroll-name="setting-sex"]'))
          male_checkbox = page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[4]/ul/li[3]/li/div[2]/div/ul/li[1]/input'))
          female_checkbox = page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[4]/ul/li[3]/li/div[2]/div/ul/li[2]/input'))
          male_checkbox.click()
          female_checkbox.click()
          if (not male_checkbox.is_selected()) and (not female_checkbox.is_selected()):
               raise ElementCheckException(f'Both sex checkboxes are unchecked')

          page.refresh()
          self.open_creating_page(page)

          page.click((By.XPATH, '//div[@data-scroll-name="setting-sex"]'))
          male_checkbox = page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[4]/ul/li[3]/li/div[2]/div/ul/li[1]/input'))
          female_checkbox = page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[4]/ul/li[3]/li/div[2]/div/ul/li[2]/input'))
          female_checkbox.click()
          male_checkbox.click()
          if (not male_checkbox.is_selected()) and (not female_checkbox.is_selected()):
               raise ElementCheckException(f'Both sex checkboxes are unchecked')
     
     def test_age_scroll(self, credentials):
          page = NewCampaignPage(self.driver)
          self.open_creating_page(page)

          age_section = page.find((By.XPATH, '//li[@data-setting-name="age"]'))
          age_section.click()
          left_scroll = age_section.find_elements(By.XPATH, '//div[@data-class-name="Handle"]')[0]
          right_scroll = age_section.find_elements(By.XPATH, '//div[@data-class-name="Handle"]')[1]
          age_20 = page.find((By.XPATH, '//span[text()="20"]'))
          age_60 = page.find((By.XPATH, '//span[text()="60"]'))

          ActionChains(page.driver).drag_and_drop(left_scroll, age_20).perform()
          if not page.exist((By.XPATH, '//span[text()="20 лет и старше"]'), 5):
               raise ElementCheckException('Age didnt change after moving left circle')
          
          ActionChains(page.driver).drag_and_drop(right_scroll, age_60).perform()
          if not page.exist((By.XPATH, '//span[text()="от 20 до 60 лет"]'), 5):
               raise ElementCheckException('Age didnt change after moving right circle')
     
     def test_age_change_mode(self, credentials):
          page = NewCampaignPage(self.driver)
          self.open_creating_page(page)

          age_section = page.find((By.XPATH, '//li[@data-setting-name="age"]'))
          age_section.click()

          age_section.find_element(By.XPATH, '//div[@data-class-name="SelectView"]').click()
          page.click((By.XPATH, '//li[@data-id="unknown"]'))
          if not page.exist((By.XPATH, '//span[text()="Реклама будет показана только тем людям, возраст которых неизвестен."]'), 5):
               raise ElementCheckException('Unknown age mode isnt opened')

          age_section.find_element(By.XPATH, '//div[@data-class-name="SelectView"]').click()
          page.click((By.XPATH, '//li[@data-id="custom"]'))
          try:
               age_section.find_element(By.XPATH, ".//textarea")
          except NoSuchElementException:
               raise ElementCheckException('Custom age mode isnt opened')
     
     def test_campaign_time_presets(self, credentials):
          page = NewCampaignPage(self.driver)
          self.open_creating_page(page)

          age_section = page.find((By.XPATH, '//li[@data-setting-name="fulltime"]'))
          age_section.click()
          cur_settings = age_section.find_element(By.CLASS_NAME, 'setting-header__value-wrapper_fulltime')

          page.click((By.XPATH, '//li[@data-name="weekDays"]'))
          if cur_settings.text != "будни":
               raise WrongValue("Weekdays mode wasnt chosen")

          page.click((By.XPATH, '//li[@data-name="weekends"]'))
          if cur_settings.text != "выходные":
               raise WrongValue("Weekends mode wasnt chosen")
          
          page.click((By.XPATH, '//li[@data-name="workTime"]'))
          if cur_settings.text != "рабочее время":
               raise WrongValue("Work time mode wasnt chosen")

          page.click((By.XPATH, '//li[@data-name="allDays"]'))
          if cur_settings.text != "круглосуточно":
               raise WrongValue("All days mode wasnt chosen")
     
     def test_campaign_time_manual(self, credentials):
          page = NewCampaignPage(self.driver)
          self.open_creating_page(page)

          age_section = page.find((By.XPATH, '//li[@data-setting-name="fulltime"]'))
          age_section.click()
          cur_settings = age_section.find_element(By.CLASS_NAME, 'setting-header__value-wrapper_fulltime')
          
          page.click((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[6]/ul/li[1]/li/div[2]/div/div[1]/div/ul[1]/li[1]'))
          if cur_settings.text != "выбрано 167/168 ч":
               raise WrongValue("Hours didnt decrease after click")

          page.click((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[6]/ul/li[1]/li/div[2]/div/div[1]/div/ul[1]/li[1]'))
          if cur_settings.text != "круглосуточно":
               raise WrongValue("Hours didnt increase after repeated click")

          page.click((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[6]/ul/li[1]/li/div[2]/div/ul[2]/li[1]'))
          if cur_settings.text != "выбрано 144/168 ч":
               raise WrongValue("Hours didnt decrease after click on weekday")

          page.click((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[6]/ul/li[1]/li/div[2]/div/div[1]/div/ul[1]/li[1]'))
          page.click((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[6]/ul/li[1]/li/div[2]/div/ul[2]/li[1]'))
          if cur_settings.text != "круглосуточно":
               raise WrongValue("Hours didnt increase after click on weekday with some missed hours")

          page.click((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[6]/ul/li[1]/li/div[2]/div/ul[3]/li[1]'))
          if cur_settings.text != "выбрано 161/168 ч":
               raise WrongValue("Hours didnt decrease after click on hour")

          page.click((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[6]/ul/li[1]/li/div[2]/div/div[1]/div/ul[1]/li[1]'))
          page.click((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[6]/ul/li[1]/li/div[2]/div/ul[3]/li[1]'))
          if cur_settings.text != "круглосуточно":
               raise WrongValue("Hours didnt increase after click on hor with some missed days")  

     
     def test_geography_add_and_delete(self, credentials):
          page = NewCampaignPage(self.driver)
          self.open_creating_page(page)

          country = "Беларусь"
          page.click((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[4]/ul/li[6]/li/div[2]/div/div[2]/div/div[1]/div[1]/div[2]'))
          page.find((By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[1]/textarea')).send_keys(country)
          page.click((By.XPATH, '/html/body/div[3]/div/div[2]/div/div[3]/div/div[1]/div'))
          region_box = page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[4]/ul/li[6]/li/div[2]/div/div[2]/div/div[1]/div[3]'))
          try:
               country_row = region_box.find_element(By.XPATH, f".//span[@title='{country}']").find_element(By.XPATH, '..')
          except NoSuchElementException:
               raise ElementCheckException(f'Country isnt added')
          
          delete_button = page.wait(5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'selectedRegions-module-itemClose-sh178b')))
          delete_button.click()
          try:
               region_box.find_element(By.XPATH, f".//span[text()='{country}']")
               raise ElementCheckException('Country isnt deleted')
          except NoSuchElementException:
               pass
     
     def test_geography_no_countries(self, credentials):
          page = NewCampaignPage(self.driver)
          self.open_creating_page(page)

          expected_message = "Объявления будут транслироваться на весь мир."

          page.click((By.CLASS_NAME, 'selectedRegions-module-itemClose-sh178b'))
          if not page.exist((By.XPATH, f'//div[contains(., "{expected_message}")]')):
               raise ElementCheckException(f'No "{expected_message}" message without countries')
     
     def test_campaign_period(self, credentials):
          page = NewCampaignPage(self.driver)
          self.open_creating_page(page)

          today = datetime.today().strftime('%d.%m.%Y')
          tomorrow = (datetime.today() + timedelta(days=1)).strftime('%d.%m.%Y')

          page.click((By.XPATH, '//div[@data-scroll-name="setting-date"]'))
          start_input = page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[6]/ul/li[2]/li/div[2]/div/div[2]/input'))
          end_input = page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[6]/ul/li[2]/li/div[2]/div/div[4]/input'))

          start_input.send_keys(tomorrow)
          end_input.send_keys(today)
          if start_input.get_attribute('value') != today and end_input.get_attribute('value') != tomorrow:
               raise ElementCheckException('Period dates didnt switch when end is before start')

     
     
     def test_budget_error_messages(self, credentials):
          page = NewCampaignPage(self.driver)
          self.open_creating_page(page)

          daily_budget = page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[7]/ul/li[4]/li/div[2]/div/div[1]/div[2]/div[1]/div[1]/div/div/input'))
          overall_budget = page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[7]/ul/li[4]/li/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/input'))

          error_message = "Ограничение бюджета меньше минимально возможного значения"
          daily_budget.send_keys('99')
          if not page.exist((By.XPATH, f'//div[text()="{error_message}"]')):
               raise ElementCheckException(f'No "{error_message}" message with little daily budget')
          daily_budget.clear()

          error_message = "Ограничение бюджета меньше минимально возможного значения"
          overall_budget.send_keys('99')
          if not page.exist((By.XPATH, f'//div[text()="{error_message}"]')):
               raise ElementCheckException(f'No "{error_message}" message with little overall budget')
          overall_budget.clear()

          error_message = "Шаг изменения — 100 ₽ ( ₽, 200 ₽ и т.д.)"
          overall_budget.send_keys('150')
          if not page.exist((By.XPATH, f'//div[text()="{error_message}"]')):
               raise ElementCheckException(f'No "{error_message}" message with overak budget not multiple 100')
          overall_budget.clear()

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

class TestCampaignCreationEditing(BaseCase):
     authorize = True

     def open_creating_page(self, page):
          #writing a link
          page.click((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]'), 15)
          page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[2]/div/div[3]/div[1]/div/div[1]/div/div/input'), 15).send_keys(testing_group)
     
     def test_creation_deleting_restoring_editing(self, credentials):
          page = NewCampaignPage(self.driver)
          self.open_creating_page(page)

          #typing balance
          page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[7]/ul/li[4]/li/div[2]/div/div[1]/div[2]/div[1]/div[1]/div/div/input')).send_keys('100')
          page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[7]/ul/li[4]/li/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/input')).send_keys('100')

          #making banner
          page.click((By.ID, 'patterns_banner_4'))
          page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div/div/div[2]/input')).send_keys(os.getcwd() + '/hw/code/bannerExample.jpg')
          page.click((By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[3]/input'))
          #waiting for upload
          page.find((By.CLASS_NAME, 'patternTabs-module-green-38duiQ'), 5)

          #getting a name
          name = page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[5]/div/div[2]/div/div[2]/input')).get_attribute('value')
          page.click((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[1]/div[1]/button/div'))

          page = DashboardPage(self.driver)
          if not page.exist((By.XPATH, f'//a[text()=\'{name}\']'), 15):
               raise ElementCheckException(f'Сampaign with name "{name}" isnt created')

          link_button = page.find((By.XPATH, f'//a[text()=\'{name}\']'))
          campaign_id = link_button.get_attribute('href')[31:-1]
          #click settings
          page.click((By.XPATH, f'//div[@data-test=\'setting-{campaign_id} row-{campaign_id}\']'))
          #click delete
          page.click((By.XPATH, f'//li[@data-test=\'3\']'))
          page.refresh()

          if page.exist((By.XPATH, f'//a[text()=\'{name}\']'), 15):
               raise ElementCheckException(f'Сampaign with name "{name}" isnt deleted')
               
          page.click((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div[1]/div[2]/div/div/div[1]/span'))
          page.click((By.XPATH, f'//li[@data-test=\'3\']'))

          #click settings
          page.click((By.XPATH, f'//div[@data-test=\'setting-{campaign_id} row-{campaign_id}\']'))
          #click restore
          page.click((By.XPATH, f'//li[@data-test=\'4\']'))

          page.click((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div[1]/div[2]/div/div/div[1]/span'))
          page.click((By.XPATH, f'//li[@data-test=\'1\']'))

          if not page.exist((By.XPATH, f'//a[text()=\'{name}\']'), 15):
               raise ElementCheckException(f'Сampaign with name "{name}" isnt restored as stopped')

          #
          #editing
          #
          new_name = "New name"

          i = 1
          name_to_edit = new_name
          while page.exist((By.XPATH, f'//a[text()=\'{name_to_edit}\']')):
               name_to_edit = new_name + " " + str(i)
               i = i + 1

          link_button = page.find((By.XPATH, f'//a[text()=\'{name}\']'))
          campaign_id = link_button.get_attribute('href')[31:-1]
          #click settings
          page.click((By.XPATH, f'//div[@data-test=\'setting-{campaign_id} row-{campaign_id}\']'))
          #click edit
          page.click((By.XPATH, f'//li[@data-test=\'5\']'))
          page.driver.close()
          page.driver.switch_to.window(page.driver.window_handles[0])

          #change title
          title_input = page.wait(5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[2]/div/div[10]/div/div[2]/div/div[2]/input')))
          title_input.clear()
          title_input.send_keys(name_to_edit)

          #change sex to female only
          page.click((By.XPATH, '//div[@data-scroll-name="setting-sex"]'))
          page.click((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[4]/ul/li[3]/li/div[2]/div/ul/li[1]/input'))
          
          #change age to from 20
          age_section = page.find((By.XPATH, '//li[@data-setting-name="age"]'))
          age_section.click()
          left_scroll = age_section.find_elements(By.XPATH, '//div[@data-class-name="Handle"]')[0]
          age_20 = page.find((By.XPATH, '//span[text()="20"]'))
          ActionChains(page.driver).drag_and_drop(left_scroll, age_20).perform()

          #change time to weekdays
          age_section = page.find((By.XPATH, '//li[@data-setting-name="fulltime"]'))
          age_section.click()
          page.click((By.XPATH, '//li[@data-name="weekDays"]'))

          #change region
          country = "Беларусь"
          page.click((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[4]/ul/li[6]/li/div[2]/div/div[2]/div/div[1]/div[1]/div[2]'))
          page.find((By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[1]/textarea')).send_keys(country)
          page.click((By.XPATH, '/html/body/div[3]/div/div[2]/div/div[3]/div/div[1]/div'))
          
          #change campaign period
          tomorrow = (datetime.today() + timedelta(days=1)).strftime('%d.%m.%Y')
          day_after_tomorrow = (datetime.today() + timedelta(days=2)).strftime('%d.%m.%Y')
          page.click((By.XPATH, '//div[@data-scroll-name="setting-date"]'))
          start_input = page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[6]/ul/li[2]/li/div[2]/div/div[2]/input'))
          end_input = page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[6]/ul/li[2]/li/div[2]/div/div[4]/input'))
          start_input.send_keys(tomorrow)
          end_input.send_keys(day_after_tomorrow)

          #change budget
          page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[7]/ul/li[4]/li/div[2]/div/div[1]/div[2]/div[1]/div[1]/div/div/input')).clear()
          page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[7]/ul/li[4]/li/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/input')).clear()
          page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[7]/ul/li[4]/li/div[2]/div/div[1]/div[2]/div[1]/div[1]/div/div/input')).send_keys('200')
          page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[7]/ul/li[4]/li/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/input')).send_keys('1000')

          #click save
          page.click((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[1]/div[1]/button/div'))

          #
          #checking stage
          #
          page = DashboardPage(self.driver)
          if not page.exist((By.XPATH, f'//a[text()=\'{name_to_edit}\']'), 15):
               raise ElementCheckException(f'Changed title to {name_to_edit} isnt saved')

          link_button = page.find((By.XPATH, f'//a[text()=\'{name_to_edit}\']'))
          campaign_id = link_button.get_attribute('href')[31:-1]
          #click settings
          page.click((By.XPATH, f'//div[@data-test=\'setting-{campaign_id} row-{campaign_id}\']'))
          #click edit
          page.click((By.XPATH, f'//li[@data-test=\'5\']'))
          page.driver.close()
          page.driver.switch_to.window(page.driver.window_handles[0])

          if page.find((By.CLASS_NAME, 'setting-header__value-wrapper_sex')).text != 'женщины':
               raise WrongValue('Changed sex isnt saved')
          
          if page.find((By.CLASS_NAME, 'setting-header__value-wrapper_age')).text != '20 лет и старше':
               raise WrongValue('Changed age isnt saved')

          if page.find((By.CLASS_NAME, 'setting-header__value-wrapper_geo')).text != 'Россия, Беларусь':
               raise WrongValue('Changed countries isnt saved')

          if page.find((By.CLASS_NAME, 'setting-header__value-wrapper_fulltime')).text != 'будни':
               raise WrongValue('Changed time isnt saved')

          if page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[6]/ul/li[2]/li/div[2]/div/div[2]/input')).get_attribute('value') != tomorrow and \
             page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[6]/ul/li[2]/li/div[2]/div/div[4]/input')).get_attribute('value') != day_after_tomorrow:
               raise WrongValue('Changed period isnt saved')

          if page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[7]/ul/li[4]/li/div[2]/div/div[1]/div[2]/div[1]/div[1]/div/div/input')).get_attribute('value') != "200" and \
             page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[7]/ul/li[4]/li/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/input')).get_attribute('value') != "100":
               raise WrongValue('Changed budget isnt saved')

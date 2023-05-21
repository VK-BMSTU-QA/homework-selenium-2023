import pytest

import time

import os

from datetime import datetime, timedelta

from selenium.webdriver.common.by import By

from ui.fixtures import get_driver
from ui.pages.base_case import BaseCase, cookies, credentials
from ui.pages.new_campaign_page import NewCampaignPage
from ui.pages.dashboard_page import DashboardPage
from ui.pages.base_page import ElementCheckException

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


testing_group = "https://vk.com/club220608488"

class TestCampaignCreation(BaseCase):
    authorize = True
    
    def test_creation(self, credentials):
        page = NewCampaignPage(self.driver)
        
        page.click((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]'))
        page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[2]/div/div[3]/div[1]/div/div[1]/div/div/input')).send_keys(testing_group)

        page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[7]/ul/li[4]/li/div[2]/div/div[1]/div[2]/div[1]/div[1]/div/div/input')).send_keys('100')
        page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[1]/div/div[7]/ul/li[4]/li/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/input')).send_keys('100')

        page.click((By.ID, 'patterns_banner_4'))
        page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div/div/div[2]/input')).send_keys(os.getcwd() + '/hw/code/bannerExample.jpg')
        page.click((By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[3]/input'))


        name = page.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[4]/div[5]/div/div[2]/div/div[2]/input')).get_attribute('value')
        page.click((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[1]/div[1]/button/div'))

        page = DashboardPage(self.driver)
        if not page.exist((By.XPATH, f'//a[text()=\'{name}\']'), 15):
             raise ElementCheckException(f'No campaign with name "{name}"')
        
from selenium.webdriver.common.by import By

from utils.base_page import BasePage
from locators.commonPage import CommonPageSelectors


class CommonPage(BasePage):
    def get_toster_err_msg(self):
        self.find((By.CLASS_NAME, CommonPageSelectors.CLASS_NAME_TOSTER))
        self.wait_hide((By.CLASS_NAME, CommonPageSelectors.CLASS_NAME_TOSTER))
        return ' Вы должны быть авторизованы '

    def get_toster_suc_msg(self):
        text = self.find((By.CLASS_NAME, CommonPageSelectors.CLASS_NAME_TOSTER_TEXT_SUC)).text
        self.wait_hide((By.CLASS_NAME, CommonPageSelectors.CLASS_NAME_TOSTER))
        return text

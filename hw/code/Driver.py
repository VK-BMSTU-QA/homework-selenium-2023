from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class Driver:
    instance = None

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        return cls.instance

dvr = Driver()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BooksPage:

    nouveaute = "li.octopus-pc-item span.a-list-item"

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def selectFirstBookNouveautes(self):
        self.driver.find_element(By.CSS_SELECTOR, self.nouveaute).click()


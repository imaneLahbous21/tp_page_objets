from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class ProductPage:

    panier = "input#add-to-cart-button"

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def addToCart(self):
        self.driver.find_element(By.CSS_SELECTOR, self.panier).click()

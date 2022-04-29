from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class ConfirmationPage:
    aller_au_panier = "a#nav-cart"

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def openCart(self):
        self.driver.find_element(By.CSS_SELECTOR, self.aller_au_panier).click()
        wait = WebDriverWait(self.driver, 3)
        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.aller_au_panier)))


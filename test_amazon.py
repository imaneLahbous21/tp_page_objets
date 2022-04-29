import selenium
from page_object.HomePage import HomePage
from page_object.BooksPage import BooksPage
from page_object.ProductPage import ProductPage
from page_object.ConfirmationPage import ConfirmationPage
from page_object.CartPage import CartPage


from selenium import webdriver


def test_amazon1():
    driver = selenium.webdriver.Chrome()
    driver.get("https://www.amazon.fr/")
    driver.maximize_window()
    driver.quit()

def test_page_object():
    driver = selenium.webdriver.Chrome()
    driver.get("https://www.amazon.fr/")
    driver.maximize_window()
    quantite = "2"

    homePage = HomePage(driver)
    homePage.closeCookies()
    homePage.openAllMenu()
    homePage.openBookCategory()
    homePage.openAllBooks()

    booksPage = BooksPage(driver)
    booksPage.selectFirstBookNouveautes()

    productPage = ProductPage(driver)
    productPage.addToCart()

    confirmationPage = ConfirmationPage(driver)
    confirmationPage.openCart()

    cart = CartPage(driver)
    cart.changeQuantity("2")
    cart.getQuantity()
    assert quantite == cart.getQuantity(), "la quantite_saisie et la quantite  de la selection sont differents"







import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

link = "https://store.steampowered.com/app/1430190/Killing_Floor_3/"
browser = webdriver.Chrome()
browser.get(link)

find_game_name = browser.find_element(By.CLASS_NAME, "apphub_AppName")
game_name = find_game_name.text

time.sleep(2)
#Находит цену на странице
game_purchase_price = browser.find_element(By.CLASS_NAME, "game_purchase_price")
game_price = game_purchase_price.text

searchbox = browser.find_element(By.ID, "btn_add_to_cart_502324")
searchbox.send_keys(Keys.ENTER)

time.sleep(2)
game_in_basket = browser.find_element(By.CLASS_NAME, "EflKs0JjldhDSxbUBaiOp")
game_name_in_basket = game_in_basket.text

def test_check_game_name():
    assert game_name == game_name_in_basket, f"Ожидаемый результат. Фактический результат:"
#Находит цену в корзине

time.sleep(2)
find_price_in_basket = browser.find_element(By.CLASS_NAME, "pk-LoKoNmmPK4GBiC9DR8")
price_in_basket = find_price_in_basket.text

def test_check_price():
    assert price_in_basket in game_price, f"Ожидаемый результат {game_price}. Фактический результат {price_in_basket}"


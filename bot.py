import telebot
from variables import *
from selenium import webdriver
import time


def site(message):
    driver = webdriver.Firefox()
    driver.get('https://edadeal.ru/kazan/offers?search=' + message.text + '&sort=ddiscount&title=' + message.text)
    time.sleep(10)
    mes1 = []
    mes2 = []
    mes3 = []
    mes4 = []
    mes5 = []
    mes6 = []
    mes7 = []
    mes8 = []
    mes9 = []
    title(driver, mes1, mes2, mes3)
    price_food(driver, mes4, mes5, mes6)
    shop_name(driver, message, mes1, mes2, mes3, mes4, mes5, mes6, mes7, mes8, mes9)
    driver.quit()


def title(driver, mes1, mes2, mes3):
    names = driver.find_elements_by_class_name('b-offer__description')
    i = 0
    for name in names[0:3]:
        i = i + 1
        if i == 1:
            mes1.append('1) ' + name.text + '\n')
        elif i == 2:
            mes2.append('2) ' + name.text + '\n')
        else:
            mes3.append('3) ' + name.text + '\n')


def price_food(driver, mes4, mes5, mes6):
    prices = driver.find_elements_by_class_name('b-offer__prices')
    i = 0
    for price in prices[0:3]:
        i = i + 1
        if (i - 1 == 0) or (i - 4 == 0):
            mes4.append('Цена со скидкой: ' + price.text + ' - цена без скидки' + '\n')
        elif (i - 2 == 0) or (i - 5 == 0):
            mes5.append('Цена со скидкой: ' + price.text + ' - цена без скидки' + '\n')
        else:
            mes6.append('Цена со скидкой: ' + price.text + ' - цена без скидки' + '\n')


def shop_name(driver, message, mes1, mes2, mes3, mes4, mes5, mes6, mes7, mes8, mes9):
    shops = driver.find_elements_by_class_name('b-image__img')
    i = 0
    for shop in shops[1:7:2]:
        i = i + 1
        if i == 1:
            mes7.append('Магазин: ' + shop.get_attribute('alt') + '\n')
        elif i == 2:
            mes8.append('Магазин: ' + shop.get_attribute('alt') + '\n')
        else:
            mes9.append('Магазин: ' + shop.get_attribute('alt') + '\n')
    if len(mes1) == 0:
        bot.send_message(message.from_user.id, 'По вашему запросу ничего не найдено :(')
    else:
        bot.send_message(message.from_user.id, mes1)
        bot.send_message(message.from_user.id, mes4)
        bot.send_message(message.from_user.id, mes7)
        bot.send_message(message.from_user.id, '_____________________')
        bot.send_message(message.from_user.id, mes2)
        bot.send_message(message.from_user.id, mes5)
        bot.send_message(message.from_user.id, mes8)
        bot.send_message(message.from_user.id, '_____________________')
        bot.send_message(message.from_user.id, mes3)
        bot.send_message(message.from_user.id, mes6)
        bot.send_message(message.from_user.id, mes9)


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.from_user.id, start_mess)


@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.from_user.id, help_mess)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    site(message)


bot.polling()

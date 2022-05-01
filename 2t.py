import re
import threading
import typing
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import db
from object import Phone, PhoneList

class Driver:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_phones(self, page: str) -> typing.List[Phone]:
        self.driver.get(
            'https://www.dns-shop.ru/catalog/17a8a01d16404e77/smartfony/?order=2&groupBy=avails&stock=now-today-tomorrow-later&p={0}'.format(page))
        phones_list = PhoneList()
        html = self.driver.find_element_by_xpath('html')
        for i in range(30):
            html.send_keys(Keys.PAGE_DOWN)
        phone_elem = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div/div[3]')
        for phone in phones_elem.find_elements_by_xpath('div'):
            name = phones.find_element_by_xpath('a/span').text
            url = phones.find_element_by_xpath('a').get_attribute('href')
            price = phones.find_element_by_xpath('div[4]/div/div[1]').text.replace(' ', '')
            price = re.findall('[0-9]*', price)[0]
            phones_list.add(Phone(name, price, url))
        return phones_list.phones_list

    def get_amount_str(self):
        self.driver.get('https://www.dns-shop.ru/catalog/17a8a01d16404e77/smartfony/?order=2&groupBy=avails&stock=now-today-tomorrow-later')
        html = self.driver.find_element_by_xpath('html')
        for i in range(30):
            html.send_keys(Keys.PAGE_DOWN)
        href = self.driver.find_element_by_xpath('//*[@id="products-list-pagination"]/ul/li[12]/a').get_attribute(
            'href')
        return href.split('/')[-1].replace('?p=', '')

if __name__ == '__main__':
    db = db.Database()
    driver = Driver()
    amount = 0
    for i in range(1, int(driver.get_amount_str()) + 1):
        phones_list = driver.get_phones(str(i))
        for phones in phones_list:
            if amount < 30:
                db.upload_phones(phones)
                amount += 1
            else:
                exit(1)
                break
        db.commit()

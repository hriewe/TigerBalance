# Hayden Riewe
# github.com/hriewe
# hrcyber.tech

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import requests
from bs4 import BeautifulSoup
import time
from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

options = Options()
options.headless = True

url = 'https://t1online.app.clemson.edu/accounts'
driver = webdriver.Firefox(options=options)
driver.get(url)

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

username.send_keys("")
password.send_keys('')

driver.find_element_by_id('submitButton').click()

time.sleep(5)

html = driver.page_source

soup = BeautifulSoup(html, features="lxml")

for tr in soup.find_all('tr')[1]:
   for td in soup.find_all('td')[1]:
      currentBalance = td

message = client.messages \
    .create(
         body='Your TigerOne card balance is: ' + currentBalance,
         from_='',
         to=''
     )

driver.quit()


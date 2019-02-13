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

# Twilio account credentials
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

# Run Firefox with no window
options = Options()
options.headless = True

url = 'https://t1online.app.clemson.edu/accounts'
driver = webdriver.Firefox(options=options)
driver.get(url)

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

# iROAR username and password go here
username.send_keys("")
password.send_keys("")

driver.find_element_by_id('submitButton').click()

# Wait to load page
time.sleep(5)

html = driver.page_source

soup = BeautifulSoup(html, features="lxml")

# Scrape the page for the balance
for tr in soup.find_all('tr')[1]:
   for td in soup.find_all('td')[1]:
      currentBalance = td

# Use the Twilio API to send a text message to your phone with the balance
message = client.messages \
    .create(
         body='Your TigerOne card balance is: ' + currentBalance,
         from_='',
         to=''
     )

# Close Firefox
driver.quit()


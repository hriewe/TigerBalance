# Hayden Riewe
# github.com/hriewe
# hrcyber.tech

# Generates a graph of TigerOne spending habits.

import matplotlib.pyplot as plt
import csv
import yagmail

balances = []
dates = []

# Get data from csv file
with open('balancehistory.csv') as database:
  balancehistory = csv.reader(database, delimiter=',')
  for balance in balancehistory:
    balances.append(float(balance[0]))
    dates.append(balance[1])

# Build graph
plt.plot(dates, balances, color='g')
plt.xlabel('Date (d/m/y)')
plt.ylabel('Balance ($)')
plt.title('TigerOne Balance Summary')
plt.savefig('graph.jpeg')

# Email graph to yourself
yag = yagmail.SMTP('YourEmailAddress')
yag.send(to='YourEmailAddressAgain',subject='Weekly TigerOne Spending Report',
contents='graph.jpeg')
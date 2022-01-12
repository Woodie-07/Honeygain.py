# EarnApp.py testing script

from honeygain import honeygain

token = "BEARER TOKEN HERE"
proxy = {'https': 'socks5://user:pass@ip:port'}

print("Initializing user class")
user = honeygain.User()
print("Got user class")

#user.setProxy(proxy) 

print("Attempting to log in with token " + token)
loggedIn = user.login(token)

if loggedIn == True:
    print("Successfully logged in!")
else:
    print("Failed to log in")
    
print("Earnings Stats: " + str(user.earningsStats()))
print("Balance: " + str(user.balance()))
print("Referral Earnings: " + str(user.refEarnings()))
print("Earnings Today: " + str(user.earningsToday()))
print("Devices: " + str(user.devices()))
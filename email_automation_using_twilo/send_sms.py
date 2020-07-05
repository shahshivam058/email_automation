from twilio.rest import Client
from twilo_keys import *

client =  Client(account_sid,account_token)
blacklist = []
receivers = list(set(recipeant_mobile_number).difference(set(blacklist)))

for receiver in receivers:
    client.messages.create(to=receiver,from_=account_number,body = message)
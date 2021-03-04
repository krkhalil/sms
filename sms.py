from twilio.rest import Client
account_sid = "*******************"
account_token = "********************"
client = Client(account_sid,account_token)
for i in range(0,10):
    client.messages.create(from_="+19999999999", body="hi how are you", to="+9288888888888") 
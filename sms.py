from twilio.rest import Client
account_sid = "AC22fe5a5458844423b9ca7346b0b684e3"
account_token = "70b122261d428929df4041e69a75c8de"
client = Client(account_sid,account_token)
for i in range(0,10):
    client.messages.create(from_="+18184958325", body="hi Madam Someone is waiting for you on whatapp!", to="+923374885655") 
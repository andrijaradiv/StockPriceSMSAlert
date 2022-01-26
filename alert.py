from config import ACCOUNT_SID, AUTH_TOKEN, PHONE_NUMBER, FROM_NUMBER
from twilio.rest import Client

client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Send string parameter message to phone number from config file
def sendSMS(message): 
    return client.messages.create(
        body=message,
        from_=FROM_NUMBER,
        to=PHONE_NUMBER
    )   
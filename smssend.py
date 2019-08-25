import os
from twilio import Client

account_sid=os.environ["TWILIO_ACCOUNT_SID"]
auth_token=os.environ["TWILIO_AUTH_TOKEN"]

client = Client(account_sid,auth_token)

client.messages.create(
    to=os.environ["MY_PHONE_NUMBER"],
    from_="+142320568304232056830",
    body="success"
)   
    


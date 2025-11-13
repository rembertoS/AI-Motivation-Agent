from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

client = Client(
    os.getenv("TWILIO_SID"),
    os.getenv("TWILIO_AUTH")

)

message = client.messages.create(
    body = "You got this! Keep pushing Forward" ,
    from_=os.getenv("TWILIO_NUMBER") ,
    to = os.getenv("MY_PHONE")

)

print("Message sent! SID: " , message.sid)


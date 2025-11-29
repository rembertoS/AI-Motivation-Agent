from twilio.rest import Client
from dotenv import load_dotenv
import os

from Utils.ai_generator import generate_motivational_quote

load_dotenv()


twilio_sid = os.getenv("TWILIO_ACCOUNT_SID")
twilio_auth = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone = os.getenv("TWILIO_PHONE_NUMBER")
user_phone = os.getenv("MY_PHONE")

client = Client(twilio_sid , twilio_auth)

def send_daily_motivation(user_number):
 
    quote = generate_motivational_quote()
    
    message = client.messages.create(
        body = quote,
        from_=twilio_phone,
        to=user_number
    )
    return message.sid


if __name__ == "__main__":
    sid = send_daily_motivation(user_phone)
    print("Message sent, SID:", sid)


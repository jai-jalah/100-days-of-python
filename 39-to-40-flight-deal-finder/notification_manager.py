from decouple import config
from twilio.rest import Client

TWILIO_SID = config("TWILIO_SID")
TWILIO_AUTH_TOKEN = config("TWILIO_AUTH_TOKEN")
TWILIO_NUM = config("TWILIO_NUM")
DESTINATION_NUM = config("DESTINATION_NUM")


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_NUM,
            to=DESTINATION_NUM,
        )
        # Prints if successfully sent.
        print(message.sid)

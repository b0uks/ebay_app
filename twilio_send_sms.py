import SMS
from twilio.rest import Client

client = Client(SMS.twilio_sid, SMS.twilio_auth)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_= SMS.twilio_from,
                     to='+18472194804'
                 )

print(message.sid)
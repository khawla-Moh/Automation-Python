from twilio.rest import Client

account_sid = 'AC94176aae8a63d803065ad3e315bc7276'
auth_token = 'd97caecdf08e4901de3c44702d0dc7c8'

client = Client(account_sid, auth_token)
message = client.messages.create(
    body='Hello, World!',  # Message content
    from_='+13344543661',  # Your Twilio phone number
    to='+967774642534'     # Recipient's phone number
)

print(message.sid)
print("sent o_-")

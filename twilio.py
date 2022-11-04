# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['AC7800886fdaa68201dee4d08b59588e75']
auth_token = os.environ['e29d0b3df128c15f65bd93800a6d7761']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Платформа Каллакалон просит вас пнуть Амаля при встречи с ним",
                     from_='+19136755638',
                     to='+998973943124'
                 )

print(message.sid)
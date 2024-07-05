from twikit import Client
import json

USERNAME = 'Eroticdreamz1'
'EMAIL = 'email@example.com'
PASSWORD = 'TwiEro2001*'

# Initialize client
client = Client('en-US')

client.login(
    auth_info_1=USERNAME ,
    'auth_info_2=EMAIL,
    password=PASSWORD
)

client.save_cookies('cookies.json')


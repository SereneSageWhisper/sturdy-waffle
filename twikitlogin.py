from twikit import Client
import json

USERNAME = 'username'
'EMAIL = 'email@example.com'
PASSWORD = 'password'

# Initialize client
client = Client('en-US')

client.login(
    auth_info_1=USERNAME ,
    'auth_info_2=EMAIL,
    password=PASSWORD
)

client.save_cookies('cookies.json')


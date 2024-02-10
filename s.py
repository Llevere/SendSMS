from twilio.rest import Client
import time
import requests
import os

from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
client = Client(account_sid, auth_token)



def main_function():
    print("Running main functionality...")
    url = "https://www.affirmations.dev/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        #Output the data
        print(data['affirmation'])  
        message = client.messages.create(
        from_=os.getenv("from_"),
        to=os.getenv("to"),
        body=data['affirmation']
        )

        print(message.sid)
    
   
    else:
        print(f"Error: Unable to retrieve data from the API. Status code: {response.status_code}")

while True:
    # Get the current time in the 24-hour format
    current_time = time.localtime()
    
    if current_time.tm_hour == 22 and current_time.tm_min == 00:
        main_function()
        
        time.sleep(60)
    else:
        time.sleep(10)






   # coding: utf-8

from twilio.rest import TwilioRestClient
import json
import requests
from requests.auth import HTTPBasicAuth
import datetime
import pytz
import time
#'geocode' : '{:.4f},{:.4f}'.format(-37.940878, 145.028654),
username= "                              "
password= "                "
url5 = "https://twcservice.mybluemix.net/api/weather/v2"
#GET /api/weather/v2/forecast/daily/10day
def get_weather(in_lat, in_long):

    params = {
        'geocode' : '{:.4f},{:.4f}'.format( in_lat, in_long),
        'units': 'm',
        'language': 'en-US'
             }
    auth = HTTPBasicAuth(username,password)

    resp = requests.get(url5+'/forecast/daily/10day', params=params, auth=auth)

    JSON_output =resp.json()

    myforcast = JSON_output['forecasts'][0]["day"]   
    for key, value in myforcast.items() :
       print key, value
    uv_index = myforcast['uv_index']
    uv_desc  = myforcast['uv_desc']
    termperature = myforcast['hi']
    desc = myforcast['phrase_32char']
    hi = myforcast['hi']
    Sunscreen_reminder = 'The UV factor is ' + myforcast['uv_desc']   
    if hi > 30:
        general_weather_desc = 'Hot'
    elif hi > 24:
        general_weather_desc = 'Warm to Hot'
    elif hi > 18:
        general_weather_desc = 'Cool to Mild'
    elif hi > 10:
        general_weather_desc = 'Cool to cold'    
    elif hi < 10:
        general_weather_desc = 'Cold'  

    todays_weather = "Good Morning today will be " + general_weather_desc + ' and ' + desc + ' Top termperature will be ' + str(hi) + ' and ' + Sunscreen_reminder
    return(todays_weather)

def send_sms(phonenumber, message):
    account = "                         "
    token = "                           "
    client = TwilioRestClient(account, token)
    message = client.sms.messages.create(to=phonenumber,
                                     from_="+19999999999999999",
                                     body=message)

def job():
    my_time = datetime.datetime.now(pytz.timezone('Australia/Melbourne')).time()

if __name__ == "__main__":
    send_message = 'yes'
    while True:
        if datetime.datetime.now().hour == 6:
            my_time = datetime.datetime.now(pytz.timezone('Australia/Melbourne')).time()
            todays_weather = get_weather(-37.940878, 145.028654)
            if send_message == 'yes':
                send_sms("+9999999999999",todays_weather)
            else:
                print todays_weather    
            time.sleep(79200)
        else:
            print 'in else ' + str(datetime.datetime.now(pytz.timezone('Australia/Melbourne')).time())
            time.sleep(60)  # The else clause is not necessary but would prevent the program to keep the CPU busy.

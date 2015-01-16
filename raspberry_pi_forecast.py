#!/usr/bin/env python
 
import urllib
import forecastio
import datetime
import json
from xml.dom import minidom
from twython import Twython
from twilio.rest import TwilioRestClient

# Load a config file with our credentials
configFile = open(config.json, 'r')
config = json.loads(configFile)

# Twilio Information
account_sid = config['twilio_account_sid']
auth_token  = config['twilio_auth_token']
client      = TwilioRestClient(account_sid, auth_token)

# Forecast.io information
api_key     = config['forecast_api_key']

# Longitude and Latitude
# Huntersville: 35.4034,-80.8611
lat = 35.4034
lng = -80.8611

forecast = forecastio.load_forecast(api_key, lat, lng)
 
def weather_for_zip(zip_code):

 
forecast = forecastio.load_forecast(api_key, lat, lng)


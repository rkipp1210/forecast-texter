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
auth_token = config['twilio_auth_token']
client = TwilioRestClient(account_sid, auth_token)

# DarkSky API Key information
api_key = config['darksky_secret_key']

# Longitude and Latitude
BK = [40.6822, -73.9947]

forecast = forecastio.load_forecast(api_key, lat, lng)

def weatherForZip(zip_code):
    pass

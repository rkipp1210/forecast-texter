## Forecast Texter

Use python on a raspberry pi to text you every morning a forecast from darksky.net via twilio

### Up and running
- Create accounts for both Twilio and DarkSky and get your API credentials
- Using this info, create a file called `config.json` of the form:
```
{
    "twilio_account_sid": "Account SID",
    "twilio_auth_token": "Auth Token",
    "darksky_secret_key": "Secret Key",
}
```

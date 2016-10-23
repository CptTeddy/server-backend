
from twilio.rest import TwilioRestClient
from django.conf import settings

# Twilio Settings
ACCOUNT_SID = "AC25c13e8b6bb611ddac0740fa28456d83"
AUTH_TOKEN = "7113d3b111bb9d019694e46ade493789"
tclient = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)


def test_sms():
    # return send_sms("+15107016380", "this is a test")
    return send_sms("+8618917094945", "this is a test")

def send_sms(number, message):
    global twilio_client
    try:
        twilio_client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
        twilio_client.messages.create(
            to=number,
            # to="+15104993743",
            from_="+15107571223",
            body=message,
        )
        print('{} to {}'.format(message, number))
        return True
    except Exception as e:
        # client.captureException()
	    if settings.DEBUG:
	        raise e
	    return False


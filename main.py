import requests

api_key = "12345678910ABCD"
URL = "https://api.kavenegar.com/v1/%s/sms/send.json" % (api_key)
filename = "C:/Users/Kimia.ketabforoosh/Desktop/SMS"
text = """
Hi, 
This is Kimia.
Sorry for the delay in the shipment. YOur package will arrive tomorrow.

"""


def readPhones(filename):
    # TODO: read the phone numbers from the files
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content


def send_sms(number, text):
    url = URL
    data = {
        "receptor": number,
        "message": text,
    }
    response_ = requests.post(url, data=data)
    # TODO: send sms and return result
    return response_.ok


phoneNum = readPhones(filename)

for telenum in phoneNum:
    # if the phonenumber doesn't exist or doesn't work, it returns it
    if not send_sms(telenum, text):
        print(telenum)

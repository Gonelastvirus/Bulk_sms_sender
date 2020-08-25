import json
import requests
import time
import eel
eel.init("static")

@eel.expose
def send_sms(number,message):
    num=number.split(",")
    url="http://api.sparrowsms.com/v2/sms/?"
    for element in num:
        params={
        'token':'c6IdMv1UB0miVmGMOPgU',
        'from':'Demo',
        'to':element,
        'text':message,
        }
        r=requests.get(url,params=params)
        status_code = r.status_code
        response = r.text
        response_json = r.json()
        print(f"{status_code}, {response}, {response_json}")
        eel.sends(str(response_json))
    eel.back()
eel.start("index.html",size=(580,350))

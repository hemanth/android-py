""" Instanly upload to IMGUR, SMS, copies to clip and opens the img URL """
import android
from json import loads as json_decode
from urllib2 import Request, urlopen
from urllib import urlencode
import base64

__author__ = 'Hemanth H.M <hemanth.hm@gmail.com>'
__copyright__ = 'Copyright (c) 2010, h3manth.com.'
__license__ = 'GNU GPLv3'


""" The API_URL, API_KEY and IMG_APTH. """
URL = 'http://api.imgur.com/2/upload.json'
""" Please change the key to your key """
API_KEY = '6999d11def1e31418e8eaea7cae66761'
IMG_PATH = '/sdcard/imgur.jpg'

""" Number to which the link must be texted """
SMS_TO="YOUR_MOBILE_NUM"

droid = android.Android()
""" Invoke camrea to capture picture and save it to IMG_PATH """
droid.cameraInteractiveCapturePicture(IMG_PATH)

try:
    with file(IMG_PATH,'rb') as pic:
        droid.dialogCreateSpinnerProgress("Uploading","Please wait...")
        droid.dialogShow()
        image = pic.read()
        post = {
            'key': API_KEY,
            'image': base64.b64encode(image),
            'path': IMG_PATH
        }

        data = urlencode(post)
    
        try:
            img_url = urlopen(Request(URL, data))
   
        except Exception, e:
            droid.dialogDismiss()
            droid.dialogCreateAlert("Uploading..","FAILED!");
            exit;

        droid.dialogDismiss()
        response = json_decode(img_url.read())

        link = response['upload']['links']['original']
        droid.smsSend(SMS_TO,link);
        droid.setClipboard(link)
        droid.dialogCreateAlert("Uploaded,Sms'd, copied to clipboard, now view the link!");
        droid.view(link)
except IOError:
    droid.dialogCreateAlert("Sorry could not find the image!");


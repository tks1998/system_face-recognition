from PIL import Image
import os, os.path
import cv2
import base64
import urllib.parse
import requests
import json
import sys
import numpy as np
url = 'http://service.mmlab.uit.edu.vn/mmlab_api/face/feature_extract/post'
ROOT_DIR = './'
#get api token
url2 = 'http://service.mmlab.uit.edu.vn/mmlab_api/user_login/post/'
data ={'user_name': 'admin', 'password': 'admin'}
headers = {'Content-type': 'application/json'}
data_json = json.dumps(data)
response = requests.post(url2, data = data_json, headers=headers)

token = response.json()['token']
#------------------------------------
kt=None
IMAGE0_DIR = os.path.join(ROOT_DIR, "img70k")
snd_dir = next(os.walk(IMAGE0_DIR))[1]
snd_dir.sort()

for folder in snd_dir:
    IMAGE_DIR = os.path.join(IMAGE0_DIR, folder)
    file_names = next(os.walk(IMAGE_DIR))[2]
    file_names = sorted(file_names)
    for img in file_names:
        print(img)
        image = open(os.path.join(IMAGE_DIR, img), 'rb')
        image_read = image.read()
        encoded = base64.encodebytes(image_read)
        encoded_string = encoded.decode('utf-8')
        ######################
        data = {
            'api_version': '1.0',
            'token': token,
            # 'eyJhbGciOiJIUzUxMiIsImlhdCI6MTU3MzQ1NjcyNSwiZXhwIjoxNjA0OTkyNzI1fQ.eyJpZCI6ImFkbWluIn0.ca9XXBZS93W9bV8V-ws1z2PV3pX0OUCjvbZlxD_obGkF_4q5pDvN3XbRkLDKDqchaSG7deNmBnbAT5Xe-Karmg',
            'data': {
                'method': 'arcface',
                'model': '0',
                'image_encoded': encoded_string,
                'bboxes': [[0, 0, 128, 128]],
                'landmarks': [{
                    'have_landmark': 'False'
                }]
            }
        }
        headers = {'Content-type': 'application/json'}
        data_json = json.dumps(data)
        response = requests.post(url, data=data_json, headers=headers)
        kt = False
        while kt==False:
            try:
                decoded_string = base64.b64decode(response.json()['data']['features'][0])
                kt=True
            except:
                response = requests.post(url,data=data_json,headers=headers)
                kt=False
        with open(os.path.join('./feature',img.split('.')[0] + '.npy'),'wb') as image_file2:
            image_file2.write(decoded_string)

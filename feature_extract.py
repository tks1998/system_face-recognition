from PIL import Image
import os, os.path
import cv2
import base64
import urllib.parse
import requests
import json
import sys
url = 'http://service.mmlab.uit.edu.vn/mmlab_api/face/feature_extract/post'
ROOT_DIR = './'

IMAGE_DIR = os.path.join(ROOT_DIR, "images")
file_names = next(os.walk(IMAGE_DIR))[2]

for img in file_names:
   print(img)
   image = open(os.path.join(IMAGE_DIR,img), 'rb')
   image_read = image.read()
   encoded = base64.encodestring(image_read)
   encoded_string = encoded.decode('utf-8')
   ######################
   data ={'api_version': '1.0', 'token': 'eyJhbGciOiJIUzUxMiIsImlhdCI6MTU3MzQ1NjcyNSwiZXhwIjoxNjA0OTkyNzI1fQ.eyJpZCI6ImFkbWluIn0.ca9XXBZS93W9bV8V-ws1z2PV3pX0OUCjvbZlxD_obGkF_4q5pDvN3XbRkLDKDqchaSG7deNmBnbAT5Xe-Karmg', 'data': {'method': 'arcface', 'model': '0', 'image_encoded': encoded_string, 'bboxes': [[0, 0, 200, 300]], 'landmarks': [{'have_landmark': 'False'}]}}
   headers = {'Content-type': 'application/json'}
   data_json = json.dumps(data)
   response = requests.post(url, data = data_json, headers=headers)
   decoded_string = base64.b64decode(response.json()['data']['features'][0])
   
   with open(os.path.join('./feature', img.split('.')[0] + '.npy'), 'wb') as image_file2:
      image_file2.write(decoded_string);   

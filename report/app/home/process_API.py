import os
import base64
import urllib.parse
import requests
import json
from . import config 
from django.conf import settings
def get_token():
    """
        Function Get Token. 
        We prepare token for call API MMLAB
    """
    url_token = 'http://service.mmlab.uit.edu.vn/mmlab_api/user_login/post/'
    data ={'user_name': 'admin', 'password': 'admin'}
    headers = {'Content-type': 'application/json'}
    data_json = json.dumps(data)
    response = requests.post(url_token, data = data_json, headers=headers)
    config.new_Token = response.json()['token']
    return True 
def get_feature(x):
    """ 
        In this function, I use API "get feature" support by mmlab UIT. 
    """
    if config.new_Token is None:
        get_token()
    url_feature = 'http://service.mmlab.uit.edu.vn/mmlab_api/face/feature_extract/post'
    path_img = os.path.join(settings.MEDIA_ROOT,x)
    filename, file_extension = os.path.splitext(x)
    image = open(path_img, 'rb')
    image_read = image.read()
    encoded = base64.encodestring(image_read)
    encoded_string = encoded.decode('utf-8')
    ######################
    data ={'api_version': '1.0', 'token': config.new_Token, 'data': {'method': 'arcface', 'model': '0', 'image_encoded': encoded_string, 'bboxes': [[0, 0, 200, 300]], 'landmarks': [{'have_landmark': 'False'}]}}
    headers = {'Content-type': 'application/json'}
    data_json = json.dumps(data)
    response = requests.post(url_feature, data = data_json, headers=headers)
    decoded_string = base64.b64decode(response.json()['data']['features'][0])
    config.path_new_numpy = os.path.join(settings.MEDIA_ROOT_NPY,filename+".npy")
    with open(config.path_new_numpy, "wb") as image_file2:
      image_file2.write(decoded_string);   
  
    return
def VGG16(request_name):
    if config.new_Token is None:
        get_token()
    url = 'http://service.mmlab.uit.edu.vn/mmlab_api/vgg16_feature_extract'
    path_img = os.path.join(settings.MEDIA_ROOT,request_name)
    filename, file_extension = os.path.splitext(request_name)
    
    image = open(path_img, 'rb')
    image_read = image.read()
    encoded = base64.encodebytes(image_read)
    encoded_string = encoded.decode('utf-8')
    ######################
    data ={'api_version': '1.0', 'data': {'method': 'vgg16', 'model': '0', 'images': [encoded_string]}}
    headers = {'Content-type': 'application/json', 
                    'Authorization': "bearer "+ config.new_Token } 
    data_json = json.dumps(data)
    response = requests.post(url, data = data_json, headers=headers)
    for feature, index in zip(response.json()['data']['predicts'], range(len(response.json()['data']['predicts']))):
        decoded_string = base64.b64decode(feature)
        config.path_new_numpy = os.path.join(settings.MEDIA_ROOT_NPY,filename+".npy")
        with open( config.path_new_numpy , "wb") as image_file2:
            image_file2.write(decoded_string);
    return  


import os
import base64
import urllib.parse
import requests
import json
from . import config
from django.conf import settings
import cv2 as cv
import numpy as np
from skimage.feature import hog, blob_doh, peak_local_max
from PIL import Image
import shutil


def get_token():
    """
        Function Get Token. 
        We prepare token for call API MMLAB
    """
    url_token = 'http://service.mmlab.uit.edu.vn/mmlab_api/user_login/post/'
    data = {'user_name': 'admin', 'password': 'admin'}
    headers = {'Content-type': 'application/json'}
    data_json = json.dumps(data)
    response = requests.post(url_token, data=data_json, headers=headers)
    config.new_Token = response.json()['token']
    return True


def get_feature(x):
    """ 
        In this function, I use API "get feature" support by mmlab UIT. 
    """
    if config.new_Token is None:
        get_token()
    url_feature = 'http://service.mmlab.uit.edu.vn/mmlab_api/face/feature_extract/post'
    path_img = os.path.join(settings.MEDIA_ROOT, x)
    filename, file_extension = os.path.splitext(x)
    image = open(path_img, 'rb')
    image_read = image.read()
    encoded = base64.encodestring(image_read)
    encoded_string = encoded.decode('utf-8')
    ######################
    data = {'api_version': '1.0', 'token': config.new_Token, 'data': {'method': 'arcface', 'model': '0',
                                                                      'image_encoded': encoded_string, 'bboxes': [[0, 0, 200, 300]], 'landmarks': [{'have_landmark': 'False'}]}}
    headers = {'Content-type': 'application/json'}
    data_json = json.dumps(data)
    response = requests.post(url_feature, data=data_json, headers=headers)
    decoded_string = base64.b64decode(response.json()['data']['features'][0])
    config.path_new_numpy = os.path.join(
        settings.MEDIA_ROOT_NPY, filename+".npy")
    with open(config.path_new_numpy, "wb") as image_file2:
        image_file2.write(decoded_string)

    return


def VGG16(request_name):
    if config.new_Token is None:
        get_token()
    url = 'http://service.mmlab.uit.edu.vn/mmlab_api/vgg16_feature_extract'
    path_img = os.path.join(settings.MEDIA_ROOT, request_name)
    filename, file_extension = os.path.splitext(request_name)

    image = open(path_img, 'rb')
    image_read = image.read()
    encoded = base64.encodebytes(image_read)
    encoded_string = encoded.decode('utf-8')
    ######################
    data = {'api_version': '1.0', 'data': {
        'method': 'vgg16', 'model': '0', 'images': [encoded_string]}}
    headers = {'Content-type': 'application/json',
               'Authorization': "bearer " + config.new_Token}
    data_json = json.dumps(data)
    response = requests.post(url, data=data_json, headers=headers)
    for feature, index in zip(response.json()['data']['predicts'], range(len(response.json()['data']['predicts']))):
        decoded_string = base64.b64decode(feature)
        config.path_new_numpy = os.path.join(
            settings.MEDIA_ROOT_NPY, filename+".npy")
        with open(config.path_new_numpy, "wb") as image_file2:
            image_file2.write(decoded_string)
    return


def HOG(request_name):
    filename, file_extension = os.path.splitext(request_name)
    orient = 32
    pix_per_cell = 32
    cell_per_block = 2
    path_img = os.path.join(settings.MEDIA_ROOT, request_name)
    img = cv.imread(path_img)
    img = cv.resize(img, (182, 182))
    feature, hog_image = hog(img, orientations=orient,
                             pixels_per_cell=(pix_per_cell, pix_per_cell),
                             cells_per_block=(cell_per_block, cell_per_block),
                             transform_sqrt=True,
                             visualize=True, feature_vector=True)
    feature = feature.astype(np.float32)
    config.path_new_numpy = os.path.join(
        settings.MEDIA_ROOT_NPY, filename+".npy")

    np.save(config.path_new_numpy, feature)


def sift_feature(request_name):

    # Function detect sift feature
    # I call detectAndCompute of opencv.
    # function returns key_point,des
    # key_point  is position of keypoint
    # list des have all key point
    # Each key_point is a 128-dimensional numpy array
    filename, file_extension = os.path.splitext(request_name)
    path_img = os.path.join(settings.MEDIA_ROOT, request_name)

    img = cv.imread(path_img)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    sift = cv.xfeatures2d.SIFT_create()
    key_point, des = sift.detectAndCompute(gray, None)

    key_point_np = np.array(key_point)
    key_point_des = np.array(des)

    feature_sift = np.concatenate(key_point_des)
    len_max_sift = 13000
    if len(feature_sift) > len_max_sift:
        feature_sift = feature_sift[:len_max_sift]
    else:
        feature_sift = np.pad(
            feature_sift, (0, len_max_sift-len(feature_sift)), 'constant')

    config.path_new_numpy = os.path.join(
        settings.MEDIA_ROOT_NPY, filename+".npy")
    np.save(config.path_new_numpy, feature_sift)

    return True


def mix_feature_sift_hog(request_name):
    filename, file_extension = os.path.splitext(request_name)

    current_path = os.path.join(settings.MEDIA_ROOT, request_name)

    feature_hog = HOG(current_path)

    feature_sift = np.concatenate(sift_feature(current_path))
    feature_mix = np.concatenate((feature_hog, feature_sift))
    len_max = 13000  # maximum mix hog and sift
    if len(feature_mix) > len_max:
        feature_mix = feature_mix[:len_max]
    else:
        feature_mix = np.pad(
            feature_mix, (0, len_max-len(feature_mix)), 'constant')

    config.path_new_numpy = os.path.join(
        settings.MEDIA_ROOT_NPY, filename+".npy")

    np.save(config.path_new_numpy, feature_mix)

    return True


def extract_face(filename, required_size=(160, 160)):
    face = cv.imread(filename)
    image = Image.fromarray(face)
    image = image.resize(required_size)
    face_array = np.asarray(image)
    return face_array


def facenet(request_name, option=1):
    filename, file_extension = os.path.splitext(request_name)
    PATH_IMG = os.path.join(settings.MEDIA_ROOT, request_name)

    model_name = 'facenet_keras'

    image = open(PATH_IMG, 'rb')
    image_read = image.read()
    encoded = base64.encodebytes(image_read)
    encoded_string = encoded.decode('utf-8')

    url_feature = 'http://192.168.20.170:3000/facenet/image/'
    data = {'data': {
            'model': model_name,
            'image_encoded': encoded_string
            }}
    headers = {'Content-type': 'application/json'}
    data_json = json.dumps(data)
    response = requests.post(url_feature, data=data_json, headers=headers)

    config.path_new_numpy = os.path.join(
        settings.MEDIA_ROOT_NPY, filename+".npy")
    a = response.json()["data"]["features"][0]["feature"]
    if option == 2:
        return a
    np.save(config.path_new_numpy, a)


def resnet():
    pass


def mix_facenet_vgg16(request_name):
    VGG16(request_name)
    name_in_npy = request_name.split(".")[0]+".npy"
    path_vgg = os.path.join(settings.MEDIA_ROOT_NPY, name_in_npy)
    a = np.load(path_vgg)

    a = a.flatten()
    b = facenet(request_name, 2)
    feature_mix = np.concatenate((a, b), 0)
    config.path_new_numpy = os.path.join(settings.MEDIA_ROOT_NPY, name_in_npy)

    np.save(config.path_new_numpy, feature_mix)
    return


def insightface(encode_data):

    model_name = 'retinaface_r50_v1'

    url_feature = 'http://192.168.20.170:3000/insightface/image/'
    data = {'data': {
        'model': model_name,
        'image_encoded': encode_data,
        'parameter': {
            "nms_thresh": 0.7,
            "thresh": 0.7
        }
    }}
    headers = {'Content-type': 'application/json'}
    data_json = json.dumps(data)
    response = requests.post(url_feature, data=data_json, headers=headers)
    print(response.json()["data"]["predicts"][0]["bounding_box"])
    return

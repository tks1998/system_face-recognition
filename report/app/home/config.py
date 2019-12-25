import os 
from django.conf import settings
"""
    setting variable
"""
Start_system = True
VP_buid = False
VP_range = 50
Root = None
Tree = None
Range_find = 100000000.0
K_similarity = 10
name_upload = 0
new_Token = None
static_up_load = 0 
path_new_numpy = None
origin_data_npy =os.path.join(settings.BASE_DIR,'home/VGG_feature/')
origin_HOG_npy = os.path.join(settings.BASE_DIR,'home/HOG_feature/')
origin_data_img =settings.IMG_ROOT


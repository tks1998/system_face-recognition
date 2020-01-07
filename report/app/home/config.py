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

origin_HOG_npy = os.path.join(settings.BASE_DIR,'home/HOG_feature/')
origin_sift_npy = os.path.join(settings.BASE_DIR,'home/Sift_feature/')
origin_mix_hog_sift = os.path.join(settings.BASE_DIR,'home/mix_hog_sift/')
origin_data_img =settings.IMG_ROOT


"""
    MODEL DEEPLEARNING FROM KERAS 
"""
model_facenet = None
type_distance = 1


Root_running_HOG = None
Root_running_sift = None
Root_running_facenet = None
Root_running_vgg16 = None
Root_running_mix_facenet_vgg16 = None 

Tree_running_HOG = None
Tree_running_sift = None
Tree_running_facenet = None
Tree_running_vgg16 = None
Tree_running_mix_facenet_vgg16 = None 
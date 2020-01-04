import os
import shutil
from django.conf import settings
from . import config


def remove_file():
    up_img = settings.MEDIA_ROOT
    up_npy = settings.MEDIA_ROOT_NPY

    if os.path.exists(up_img) == True:
        shutil.rmtree(up_img)

    if os.path.exists(up_npy) == True:
        shutil.rmtree(up_npy)

    if os.path.exists(up_img) == False:
        os.mkdir(up_img)
    if os.path.exists(up_npy) == False:
        os.mkdir(up_npy)
    config.Start_system = False

from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from . import process_Tree
from . import process_request
from . import reset_system
import os
import numpy as np
from django.conf import settings
from . import config
from . import process_API
import shutil
# Create your views here.


def index(request):

    return render(request, 'pages/home.html')


def upload(request):
    if config.Start_system:
        print("system",config.Start_system)
        reset_system.remove_file()       
    result = {}
    uploaded_file = None
    if request.method == 'POST':
        k_number = request.POST.get("knumber")
        print(111111111111111111111, k_number)
        if (k_number is not None and k_number !='' ):
            config.K_similarity = int(k_number)
         
        uploaded_file = request.FILES['document']
        if uploaded_file:
            fs = FileSystemStorage()
            config.name_upload = config.name_upload+1
            new_name = str(config.name_upload)+ ".png"
            fs.save(new_name, uploaded_file) 
            process_API.HOG(new_name)
            result = process_request.process_img(new_name)
    return render(request, 'pages/upload.html', result)

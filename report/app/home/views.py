from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,StreamingHttpResponse, HttpResponseServerError
from . import process_Tree
from . import process_request
from . import reset_system
import os
import numpy as np
from django.conf import settings
from . import config
from . import process_API
import shutil
import cv2
from django.views.decorators import gzip
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
        uploaded_file = request.FILES['document']
        if uploaded_file:
            fs = FileSystemStorage()
            config.name_upload = config.name_upload+1
            new_name = str(config.name_upload)+ ".png"
            fs.save(new_name, uploaded_file) 
            process_API.HOG(new_name)
            result = process_request.process_img(new_name)
    return render(request, 'pages/upload.html', result)

def get_frame():
    camera =cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480)) 
    while True:
        _, img = camera.read()
        out.write(img)
        imgencode=cv2.imencode('.jpg',img)[1]
        stringData=imgencode.tostring()
        yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+stringData+b'\r\n')
    del(camera)
    
def indexscreen(request): 
    try:
        template = "screens.html"
        return render(request,template)
    except HttpResponseServerError:
        print("error")

@gzip.gzip_page
def dynamic_stream(request,stream_path="video"):
    try :
        return StreamingHttpResponse(get_frame(),content_type="multipart/x-mixed-replace;boundary=frame")
    except :
        return "error"

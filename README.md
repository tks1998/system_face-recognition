# Face Recognition System
___
This is the system finds similarity images using both deep learning methods and handcrafted methods. In the current version, we were able to find k-similar images in the 70000 image data set with a time of 0.5s / image. With 70k images, we use about 3MB of RAM and run on Intel Core i7-2620M CPU 2.70 GHz. Supported systems run on ubuntu, macOS, windows. In the future, We will develop it more effective.
___
## Overview
In this project, We use API MMLAB UIT get feature extraction VGG and algorithm VP-Tree.

Database: Because the GitHub limit only allows projects < 100MB, so we use a portion of data in the future, we will upload more data.
We put data in folder `report/app/home/data`, and We put features extractions in the `report/app/home/VGG_feature`.

Algorithm Vp-Tree:
```
process_Tree.py
```
Process request in file ( get request and call vp-tree):
```
process_request.py
```
## Getting Started
We are still developing it so if you want to run it yourself, please follow the instructions.

### Prerequisites
We assume that you already had python3.x.x. If not, please do as follows: install python3.7 follow [this tutorial](https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/) and [pip3](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/).

We recommend you using virtual environments.

### Installing
A step by step series of examples that tell you how to get a development env running.

Installing **Django**
```
pip install Django == 2.2.6
```
***!!!Note that** our project was compatible with Django 2.2.6.  If you want to change, you will likely encounter an error.*

Or simply 😀
```
pip install -r requirements.txt
```

Then install **Elasticsearch**

It depends on your system, here we use `elasticsearch 7.5.1`, `elasticsearch dsl 7.1` and `python3.x.x`.
>elasticsearch >= 7.x compatible with 7 <= elasticsearch dsl < 8 and more ...

In other words: Just install any version of elasticsearch that suits you the most. You can check it [here](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html).

After successfully installing Elaticsearch, you must find a compatible version **Elasticsearch DSL** for the elaticsearch version you have installed. You can [refer](https://elasticsearch-dsl.readthedocs.io/en/latest/) for more details about elasticsearch-dsl.

**Please remember that if your elasticsearch and elasticsearch DSL are incompatible, you will encounter serious errors.**

## Deployment
```
cd report/app
python manage.py runserver
```
After that, you visit the following link: http://127.0.0.1:8000/upload/

In Django, the default port is 8000 but you can change it and you can find more information on [django website](https://www.djangoproject.com/).

## Status
This project is in progress. In the future, we will develop features that make it easy for administrators to configure and you can continue to develop it.
___
Thank you for your interest in this project 💖💖💖

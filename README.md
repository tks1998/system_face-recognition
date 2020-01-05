# Face Recognition System
___
The facial recognition system is a computer application that automatically recognizes and recognizes someone's face in an image or video frame extracted from the video. Specifically, with the system we are building, we will use images taken from the camera through web services and then print out some information about that person.

The explosion of data and the development of advanced technologies worldwide has led to the problem of finding data in the huge data resources available. Especially the problem of identifying and identifying faces in images extracted from other data sources. Therefore, the level of research on facial recognition system is increasingly important and popular. The question is how do technology companies build a complete system with complex data? It was this that inspired us to choose the topic of the facial recognition system for this project.
___
## Overview
In this project, we use the API we have built to run facial recognition and extraction methods. You can check it in [this repo](https://github.com/quantran14/cs-api).

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

## How to use
### Create database
To create a database:
1. Put image-files in the directory `report/app/home/data/`. Each image should be named `<id>.<png/jpg/...>`
2. Create 2 `.txt` label-files in the directory `report/app/home/label/` one for training & one for testing (these files will be used in training classify model). For each image-files in the new line:
`<id> <image-class>`
3. Create a model in model.py, migrate model with command in terminal: python manage.py migrate [here](https://docs.djangoproject.com/en/3.0/topics/migrations/).
4. Indexing data with elastisearch. In file documents.py, import model you want to map with elasticsearch. In my project, I used to models IR2 then create struct in elasticsearch [refer](https://elasticsearch-dsl.readthedocs.io/en/latest/).
        IR2 have field [iddata,name,description,university] then I put it in elasticsearch model.
        Example:

            import IR2
            class IR2(Document):
            class Index:
                name = 'face_system'
                settings = {'number_of_shards': 1,
                            'number_of_replicas': 0}
                class Django:
                    model = IR2
                    fields = [
                        'iddata',
                        'name',
                        'description',
                        'university',
                    ]
5. After that, I create data in elasticsearach with 

        object_elasticsearch = IR2(
            iddata=x,
            name=x,
            description="famous human",
            university="UIT"
        )
        object_elasticsearch.save()
6. Finally:
    Run command index all data above:
    
        python manage.py runserver search_index --rebuild

Where:
- `id` - interger number start from `0`
- `image-class` - interger number from `0` to `(number_of_class-1)`

3. 

## Deployment
```
cd report/app
python manage.py runserver
```
After that, Please visit the following link: http://127.0.0.1:8000/ to forward to the homepage.

In Django, the default port is 8000 but you can change it and you can find more information on [django website](https://www.djangoproject.com/).

## Status
This project is in progress. In the future, we will develop features that make it easy for administrators to configure and you can continue to develop it.
___
Thank you for your interest in this project 💖💖💖

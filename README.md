# system_face-recognition
This is the system finds a similarity images. In the current version, we were able to find k-similar images in the 70000 image data set with a time of 0.5s / image. With 70k images, We use about 3MB of RAM and run on Intel Core i7-2620M CPU 2.70 GHz. Supported systems run on ubuntu, macOS, windows. In the future, We will develop it more effective. 

Easy install:

We assume you had python3.x.x

First step:
	Install Django with the command line in the terminal or similar tool
	
		pip install Django == 2.2.6
	note: My project was compatible with Django 2.2.6. If you want to change it you have probability error
		
Second:
	Install elasticsearch:

		It depends on your system, I use elasticsearch 7.5.1, elasticsearch dsl 7.1 and python3.x.x
		elasticsearch>=7.x compatible with 7 < = elasticsearch dsl < 8  
		and more ...
		In other words:
			
			Install elasticsearch any version you want. You can reference: https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html. 
			
			After that, you must find compatible version elasticsearch DSL for your version elasticsearch. 
		
			You can refer to for more details elasticsearch-dsl: https://elasticsearch-dsl.readthedocs.io/en/latest/ 
			
			Note: It is important, If elastic-search and elastic-search DSL not compatible you will get Serious Errors
	
Finally:	
	Running project:
	You must cd to folder report/app and run  command :
		
		python manage.py runserver 
			
After that, you visit the following link: http://127.0.0.1:8000/upload
	
NOTICE:
	In Django default port is 8000 but you can change it and You can reference in website: https://www.djangoproject.com/


In this project, We use API MMLAB UIT get feature extraction VGG and algorithm VP-Tree.
Database:
	
	Because the GitHub limit only allows projects <100MB, so we use a portion of data in the future, we will upload more data.
	We put data in folder report/app/home/data, and We put features extractions in the report/app/home/VGG_feature.

Algorithm Vp-Tree:
	
	process_Tree.py

Process request in file ( get request and call vp-tree):
	
	process_request.py

Front end:
	
	Boostrap


In the future, we will develop features that make admin easy to configure and you can continue to develop it.



Thank you for your interest in this project <3

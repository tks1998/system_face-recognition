from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Information_Face
from elasticsearch_dsl import connections
from datetime import datetime
connections.configure(
    default={'hosts': 'localhost'},
    dev={
        'hosts': ['http://localhost:9200'],
        'sniff_on_start': True
    }
)

@registry.register_document
class Information(Document):
    class Index:
        name = 'face_system'

        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Information_Face 
        fields = [
            'name',
            'description',
            'time',
        ]

name1 = Information_Face(
    name="2",
    description="No Nanme T_T",
    time =  datetime.now(),
)
name1.save()

name1 = Information_Face(
    name="5",
    description="No Nanme T_T",
    time= datetime.now(),
)
name1.save()

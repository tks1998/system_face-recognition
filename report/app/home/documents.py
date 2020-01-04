from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import IR2
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


for x in range(0, 100):
    name1 = IR2(
        iddata=x,
        name=x,
        description="famous human",
        university="UIT"
    )
    name1.save()
name1 = IR2(
    iddata=101,
    name="Dang Xuan Truong",
    description="UITer K12",
    university="UIT"
)
name1.save()

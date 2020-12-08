import django_tables2 as tables
from .models import Person

class PersonTable(tables.Table):
    name = tables.Column()
    age = tables.Column()
    # class Meta:
    #     model = Person
    #     template_name = "django_tables2/bootstrap.html"
    #     fields = ("name", )

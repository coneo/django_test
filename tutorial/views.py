from django.shortcuts import render

# Create your views here.
from django_tables2 import SingleTableView

from .models import Person
from .tables import PersonTable


class PersonListView(SingleTableView):
    model = Person
    table_class = PersonTable
    template_name = 'tutorial/people.html'

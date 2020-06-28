import django_filters
from .models import *
from django_filters import CharFilter

class UsersFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr = 'icontains')

    class Meta:
        model = Users
        fields = '__all__'
        exclude = ['email' , 'last_name' , 'address', 'date_created']

class LocationsFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr = 'icontains')

    class Meta:
        model = Locations
        fields = ('name',)

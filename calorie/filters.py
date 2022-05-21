import django_filters
from django_filters import DateFilter,CharFilter
from .models import*

class FoodcalFilter(django_filters.FilterSet):
	foodname=CharFilter(field_name='foodname',lookup_expr='icontains')
	class Meta:
		model=foodcal
		fields='__all__'
		
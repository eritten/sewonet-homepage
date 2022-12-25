from tastypie.resources import ModelResource, ALL
from .models import Project

class Search(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'fetch'
        filtering = {'name': ALL, 'description':ALL}

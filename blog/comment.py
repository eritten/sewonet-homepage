from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from .models import Comment, Blog

class BlogResource(ModelResource):
    class Meta:
        queryset = Blog.objects.all()
        resource_name = 'post'
        filtering = {'author': ALL, 'title': ALL}

class CommentResource(ModelResource):
    blog = fields.ForeignKey(CommentResource(), 'comment', full=True)
    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comment'
        allow_methods = ['GET', 'POST']
        authorization = Authorization()
        filtering = {'blog': ALL_WITH_RELATIONS, 'name': ALL, 'content':ALL}


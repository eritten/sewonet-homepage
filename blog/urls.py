from django.urls import path, include
from . import views, account
from . import feeds

urlpatterns = [
path('account/', include("django.contrib.auth.urls")),
path("signup/", account.signup, name="signup"),
path('', views.blog_home, name = 'blog_home'),
path('detail/<int:pk>/<slug:slug>/', views.detail, name='detail'),
path('tag/<slug:tag_slug>/', views.tags, name='post_list_by_tag'),
path('like/', views.like, name='like'),
path("comment/", views.comment, name="comment"),
path("search/", views.search, name="search"),
    path('feed/', feeds.LatestPostsFeed(), name='feed'),
path('subscribe/', views.subscribe, name='subscribe'),

]

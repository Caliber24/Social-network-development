from django.urls import path
from . import views
from rest_framework_nested import routers

post_router = routers.DefaultRouter()
post_router.register('posts', views.PostViewSet, basename='posts')

urlpatterns = post_router.urls

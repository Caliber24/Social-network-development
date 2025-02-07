from django.urls import path
from . import views
from rest_framework_nested import routers

post_router = routers.DefaultRouter()
post_router.register('posts', views.PostViewSet, basename='posts')


like_router = routers.NestedDefaultRouter(post_router, 'posts', lookup='post')
like_router.register('reacts', views.ReactViewSet, 'posts-reacts')

urlpatterns = post_router.urls + like_router.urls

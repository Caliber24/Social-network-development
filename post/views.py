from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Post, React
from .permissions import PostOwner
from .serializers import PostSerializer, ReactSerializer
# Create your views here.


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    
    def get_queryset(self):
      return Post.objects.prefetch_related('reacts').filter(status=1)
    def get_permissions(self):
      if self.action in ['update', 'partial_update', 'destroy']:
        return [IsAuthenticated(), PostOwner()]
      else:
        return [IsAuthenticated()]
  
    def perform_create(self, serializer):
      author = self.request.user
      serializer.save(author=author)


class ReactViewSet(ModelViewSet):
  permission_classes = [IsAuthenticated]
  serializer_class = ReactSerializer
  def get_queryset(self, *args, **kwargs):
      return React.objects.filter(post_id=self.kwargs.get('post_pk'))
  
  def perform_create(self, serializer, *args, **kwargs):
    post = get_object_or_404(Post, pk=self.kwargs.get('post_pk'))
    user = self.request.user
    is_like = self.request.data.get('is_like', 'false')
    is_like = is_like.lower() == 'true'
    existing_react = React.objects.filter(post=post, user=user).first()
    if existing_react:
      existing_react.is_like = is_like
      existing_react.save()
    else:
      serializer.save(post=post, user=user, is_like=is_like)


    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


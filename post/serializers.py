from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Post, React


class PostSerializer(ModelSerializer):
    react_count = serializers.IntegerField(
        source='get_react_count', read_only=True)
    like_count = serializers.IntegerField(
        source='get_like_count', read_only=True)
    dislike_count = serializers.IntegerField(
        source='get_dislike_count', read_only=True)
    author_email = serializers.CharField(source='author.email', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author']


class ReactSerializer(ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    post_title = serializers.CharField(source='post.title', read_only=True)

    class Meta:
        model = React
        fields = ('id', 'post_title', 'user', 'user_email',
                  'is_like', 'created_at', 'updated_at',)
        read_only_fields = ('user',)

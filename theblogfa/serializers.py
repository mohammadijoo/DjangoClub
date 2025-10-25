from rest_framework import serializers
from .models import Postfa

class PostfaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postfa
        fields = ['id', 'title', 'author', 'post_date', 'category', 'snippet', 'body']
    






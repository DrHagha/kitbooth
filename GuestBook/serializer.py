from rest_framework import serializers
from GuestBook.models import Comment

class CommentListGetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = [ 'id','comment','create_date']
        
class CommentCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ['comment']
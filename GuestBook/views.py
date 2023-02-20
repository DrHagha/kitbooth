from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializer import CommentListGetSerializer, CommentCreateSerializer
from .models import Comment

@api_view(['GET'])
def get_comment_list(request):
    if request.method == "GET":
        comment_list = Comment.objects.all()
        
        if comment_list == False:
            return Response(status=404)
        
        else:
            serializer = CommentListGetSerializer(comment_list, many = True)
            return Response(serializer.data, status=200)

@api_view(['POST'])
def create_comment(request):
    serializer = CommentCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
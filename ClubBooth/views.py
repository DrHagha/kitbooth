from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializer import BoothDetailSerializer, BoothShortSerializer
from .models import Booth

@api_view(['GET'])
def booth_list(request):
    if request.method == 'GET':
        booth_list = Booth.objects.all()
        serializer = BoothDetailSerializer(booth_list, many = True)
        return Response(serializer.data, status=200)
    
@api_view(['GET'])
def booth_detail(request, pk):
    if request.method == 'GET':
        booth = Booth.objects.get(pk = pk)
        
        if not booth:
            return Response(status=404)
        else:
            serializer = BoothDetailSerializer(booth)
            print(pk)
            return Response(serializer.data, status=200)
        
class boothcreater(viewsets.ModelViewSet):
    serializer_class = BoothDetailSerializer
    queryset= Booth.objects.all()
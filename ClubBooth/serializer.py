from rest_framework import serializers
from ClubBooth.models import Booth

class BoothSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booth
        fields = [ 'id','booth_name','club_category','booth_location']
        
        
class BoothShortSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booth
        fields = [ 'id','booth_name', 'booth_location']

        
class BoothDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booth
        fields = [ 'id','booth_name', 'club_picture','club_category','booth_location','introduction']
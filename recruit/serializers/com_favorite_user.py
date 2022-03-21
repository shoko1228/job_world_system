from rest_framework import serializers
from ..models import ComFavoriteUserModel


class ComFavoriteUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ComFavoriteUserModel
        fields = ('id', 'normal_user', 'com_user')
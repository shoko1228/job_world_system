from rest_framework import serializers
from ..models import MatchingrModel


class MatchingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MatchingrModel
        fields = ('id', 'normal_user', 'com_user')
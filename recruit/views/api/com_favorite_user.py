from rest_framework.views import APIView, set_rollback
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect

from recruit.models import ComFavoriteUserModel, ItemModel
from recruit.serializers.com_favorite_user import ComFavoriteUserSerializer 
from django.contrib.auth import get_user_model

from users.models import NormalUser


class ComFavoriteUserAPIView(APIView):
    
    def get(self, request):
        '''
        データ取得
        '''
        # ログインユーザーでフィルター
#要書き換え 済み？
        seliarizer = ComFavoriteUserSerializer(ComFavoriteUserModel.objects.filter(com_user=request.user.company_user), many=True)
        return Response(seliarizer.data)
    
    
    def post(self, request):


        '''
        データ登録
        '''

#要書き換え　済み？
        normal_user = NormalUser.objects.filter(id=request.data.get("normal_user")).first()
        if not normal_user:
            return Response({"detail": "Item not found"}, status=status.HTTP_400_BAD_REQUEST)
        results = ComFavoriteUserModel.objects.get_or_create(
                com_user = request.user.company_user, 
                normal_user = normal_user
            )
        seliarizer = ComFavoriteUserSerializer(results[0])
        return Response(seliarizer.data)
    

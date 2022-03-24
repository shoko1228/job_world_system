from rest_framework.views import APIView, set_rollback
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect

from recruit.models import ComFavoriteUserModel, ItemModel, UserFavoriteItemModel,MatchingrModel
from recruit.serializers.com_favorite_user import ComFavoriteUserSerializer 
from recruit.serializers.matching import MatchingSerializer
from django.contrib.auth import get_user_model

from users.models import NormalUser


class ComFavoriteUserAPIView(APIView):
    
    def get(self, request):
        '''
        データ取得
        '''
        # ログインユーザーでフィルター

        seliarizer = ComFavoriteUserSerializer(ComFavoriteUserModel.objects.filter(com_user=request.user.company_user), many=True)
        return Response(seliarizer.data)
    
    
    def post(self, request):


        '''
        データ登録
        '''

        normal_user = NormalUser.objects.filter(id=request.data.get("normal_user")).first()
        if not normal_user:
            return Response({"detail": "Item not found"}, status=status.HTTP_400_BAD_REQUEST)
        results = ComFavoriteUserModel.objects.get_or_create(
                com_user = request.user.company_user, 
                normal_user = normal_user
            )
        seliarizer = ComFavoriteUserSerializer(results[0])
        results_list = [seliarizer.data]

        user_favorite_item = UserFavoriteItemModel.objects.filter(normal_user=normal_user, item__company = request.user.company_user).first()
        if user_favorite_item:
            results_matching = MatchingrModel.objects.get_or_create(
                    com_user = request.user.company_user, 
                    normal_user = normal_user
                )
            seliarizer_matching = MatchingSerializer(results_matching[0])
            results_list.append(seliarizer_matching.data)

        return Response(results_list)
    

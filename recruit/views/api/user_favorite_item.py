from rest_framework.views import APIView, set_rollback
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect

from recruit.models import UserFavoriteItemModel, ItemModel, MatchingrModel, ComFavoriteUserModel
from recruit.serializers.user_favorite_item import UserFavoriteItemSerializer
from recruit.serializers.matching import MatchingSerializer
from django.contrib.auth import get_user_model


class UserFavoriteItemAPIView(APIView):
    
    def get(self, request):
        '''
        データ取得
        '''
        # ログインユーザーでフィルター
        seliarizer = UserFavoriteItemSerializer(UserFavoriteItemModel.objects.filter(user=request.user.normal_user), many=True)
        return Response(seliarizer.data)
    
    
    def post(self, request):

        '''
        データ登録
        '''
        item = ItemModel.objects.filter(id=request.data.get("item_id")).first()
        if not item:
            return Response({"detail": "Item not found"}, status=status.HTTP_400_BAD_REQUEST)
        results = UserFavoriteItemModel.objects.get_or_create(
                normal_user = request.user.normal_user, 
                item = item
            )
        seliarizer = UserFavoriteItemSerializer(results[0])
        results_list = [seliarizer.data]
        
        com_favorite_user = ComFavoriteUserModel.objects.filter(normal_user=request.user.normal_user, com_user=item.company).first()
        if com_favorite_user:
            results_matching = MatchingrModel.objects.get_or_create(
                    normal_user = request.user.normal_user, 
                    com_user = item.company
                )
            seliarizer_matching = MatchingSerializer(results_matching[0])
            results_list.append(seliarizer_matching.data)
        
        return Response(results_list)
    

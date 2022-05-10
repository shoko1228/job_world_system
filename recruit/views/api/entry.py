from rest_framework.views import APIView, set_rollback
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect

from recruit.models import UserFavoriteItemModel, ItemModel, MatchingrModel, ComFavoriteUserModel,ChatMessageModel
from recruit.serializers.user_favorite_item import UserFavoriteItemSerializer
from recruit.serializers.matching import MatchingSerializer
from django.contrib.auth import get_user_model


class EntryAPIView(APIView):
    
    # def get(self, request):
    #     '''
    #     データ取得
    #     '''
    #     # ログインユーザーでフィルター
    #     seliarizer = UserFavoriteItemSerializer(UserFavoriteItemModel.objects.filter(user=request.user.normal_user), many=True)
    #     return Response(seliarizer.data)
    
    
    def post(self, request):

        '''
        データ登録
        '''
        item = ItemModel.objects.filter(id=request.data.get("item_id")).first()

        if item:
            results_matching = MatchingrModel.objects.get_or_create(
                    normal_user = request.user.normal_user, 
                    com_user = item.company
                )
            seliarizer_matching = MatchingSerializer(results_matching[0])

            results_chat_message = ChatMessageModel.objects.create(
                from_user = 0,
                normal_user = request.user.normal_user, 
                com_user = item.company,
                message = "【自動送信】" + item.name + "にエントリーしました。"
            )
        
            return Response(seliarizer_matching.data)
    

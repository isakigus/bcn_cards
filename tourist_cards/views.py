import json
from django.http import HttpResponse
from django.views.generic import View
from .models import Card, Position


class JsonResponse(HttpResponse):
    pass


class Documentation(View):
    def get(self, requests):
        return HttpResponse('Documentation')


class AddCard(View):
    def post(self, request):
        # <view logic>
        return HttpResponse('result')


class RemoveCard(View):
    def get(self, request):
        return HttpResponse('RemoveCard')


class UpdateCardPosition(View):
    def post(self, requests):
        pass


class CardInfo(View):
    def get(self, requests):
        return HttpResponse('CardInfo')


class CardList(View):
    def get(self, requests):
        return HttpResponse('CardList')

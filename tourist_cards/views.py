import sys

import inspect

from django.views.generic import View
from .models import Card, Position
from  django.core.exceptions import ValidationError
from django.http import JsonResponse


class DocumentedView(View):
    pass


class Documentation(View):
    @staticmethod
    def parser_doc_string(doc_string):
        data = [item.strip() for item in doc_string.split('\n') if item.strip()]
        api_data = dict(item.split(':') for item in data)
        return api_data

    @staticmethod
    def is_documented_class(type_object):
        return inspect.isclass(type_object) and any(['DocumentedView' in base.__name__
                                                     for base in type_object.__bases__])

    @staticmethod
    def is_an_api_method(method_name):
        return method_name in View.http_method_names and method_name != 'options'

    @staticmethod
    def get_api_strings():
        out = []
        documented_objects = [member[1] for member in inspect.getmembers(sys.modules[__name__])]

        for obj in documented_objects:
            for method_tuple in inspect.getmembers(obj, predicate=inspect.ismethod):
                method_name, doc = method_tuple[0], method_tuple[1].__doc__
                if Documentation.is_an_api_method(method_name) and doc:
                    data = Documentation.parser_doc_string(doc)
                    data.update({'api': obj.__name__.lower(), 'method': method_name})
                    out.append(data)
        return out

    def get(self, requests):
        try:
            response = {'code': 'OK', 'info': Documentation.get_api_strings()}
        except Exception as ex:
            response = {'code': 'ERR07', 'info': str(ex)}

        return JsonResponse(response)


class Cards(DocumentedView):
    def get_cards_data(self, id):

        cards = Card.objects.all() if not id else Card.objects.filter(id=id)
        out = {'cards': []}
        for card in cards:
            data_dict = card.__dict__
            if data_dict:
                data_dict.pop('_state')
            out['cards'].append(data_dict)

        if len(out['cards']) == 1:
            out = out['cards'][0]

        return out

    def all_data(self):

        cards = Card.objects.all()
        out = {'cards': []}
        for card in cards:
            data_dict = card.__dict__
            if data_dict:
                data_dict.pop('_state')
                data_dict['points'] = []

                for pos in Position.objects.filter(card_id=card.id):
                    pos_dict = pos.__dict__
                    pos_dict.pop('_state')
                    data_dict['points'].append(pos_dict)

            out['cards'].append(data_dict)

        return out

    def get(self, request, id=None):
        """ url: /card/<id>/
            params: id (number)
            description: search a card by <id>, extra if all is used all the info is displayed
        """
        data = self.all_data() if id == 'all' in request.path else self.get_cards_data(id)
        return JsonResponse(data)

    def post(self, request, id=None):
        """ url: /card/<id>/
            params: [ optional ] id (number)
            description: create a new card with id, if not id provided it is automatically created.
        """
        try:
            card = Card()
            if id:
                card.id = id
            card.save()
            response = {'code': 'OK', 'info': 'new card created with id:{}'.format(card.id)}
        except Exception as ex:
            response = {'code': 'ERR01', 'info': str(ex)}

        return JsonResponse(response)

    def delete(self, request, id=None):
        """  url: /card/<id>/
             params: [ optional ] id (number)
             description: deletes a card by id
        """
        if not id:
            response = {'code': 'ERR03', 'info': 'no id provided /card/<id>/'}
        else:
            try:
                card = Card.objects.filter(id=id).first()
                if not card:
                    response = {'code': 'OK', 'info': 'no card found try /card/list'}
                else:
                    card_id = card.id
                    card.delete()
                    response = {'code': 'OK', 'info': 'card deleted with id:{}'.format(card_id)}
            except Exception as ex:
                response = {'code': 'ERR02', 'info': str(ex)}

        return JsonResponse(response)


class PositionApi(DocumentedView):
    def post(self, request):
        """  url: /card/position
             params: card_id (number), lat (string), lon(string)
             description: create a new card position by id
        """

        try:

            card_id = request.POST.get("card_id", "")
            card = Card.objects.get(id=card_id)

            pos = Position()
            pos.card_id = card
            pos.latitud = request.POST.get("lat", "")
            pos.longitud = request.POST.get("lon", "")

            pos.clean_fields()
            pos.save()
            response = {'code': 'OK', 'info': 'new card position created with id:{}'.format(pos.id)}

        except ValidationError as ex:
            response = {'code': 'ERR05', 'info': 'error validating position: {}'.format(ex)}

        except Exception as ex:
            response = {'code': 'ERR06', 'info': 'error inserting position: {}'.format(ex)}

        return JsonResponse(response)

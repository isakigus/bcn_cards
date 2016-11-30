from django.conf.urls import url
from tourist_cards import views

urlpatterns = [
    url(r'api/info', views.Documentation.as_view()),
    url(r'position/(?P<card_id>[0-9]*)', views.PositionApi.as_view()),
    url(r'all/$', views.Cards.as_view()),
    url(r'(?P<id>[0-9]+)/$', views.Cards.as_view()),
    url(r'', views.Cards.as_view()),
]

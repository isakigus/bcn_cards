from django.conf.urls import url
from tourist_cards import views

urlpatterns = [
    url(r'api/info', views.Documentation.as_view()),
    url(r'(?P<id>\w+)/$', views.Cards.as_view()),
    url(r'position', views.PositionApi.as_view()),
    url(r'', views.Cards.as_view()),
]

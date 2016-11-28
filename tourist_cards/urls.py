from django.conf.urls import url
from tourist_cards import views

urlpatterns = [
    url(r'^list', views.CardList.as_view()),
    url(r'^info', views.CardInfo.as_view()),
    url(r'^add', views.AddCard.as_view()),
    url(r'^remove', views.RemoveCard.as_view()),
    url(r'^update_position', views.UpdateCardPosition.as_view())
]

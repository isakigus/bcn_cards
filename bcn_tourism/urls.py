from django.conf.urls import url, include
from django.contrib import admin

from tourist_cards.views import Documentation

urlpatterns = [
    url(r'^', Documentation.as_view()),
    url(r'^card/', include('tourist_cards.urls')),
    url(r'^admin/', admin.site.urls),
]

from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [

    url(r'^card/', include('tourist_cards.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'', RedirectView.as_view(url='/frontend/index.html')),
]

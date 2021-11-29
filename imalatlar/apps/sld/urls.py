from django.urls import path
from .views import detail_view, create_view, list_view, make_pdf

app_name = 'sld'
urlpatterns = [
    path('goruntule/<id>', detail_view, name='detail'),
    path('olustur', create_view, name='create'),
    path('liste', list_view, name='list'),
    path('gonder/<id>', make_pdf, name='make_pdf')
]
from django.urls import path

from .views import *

app_name = "home"

urlpatterns = [
    path('', home_view, name='home'),
    path('kapilar/',kapilar_view,name='kapilar'),
    path('about_sld/', aboutsld_view, name='aboutsld'),
    path('about_mr30/', aboutmr30_view, name='aboutmr30'),
    path('401/', view_401,name='401'),
]
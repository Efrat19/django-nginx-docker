from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('get-emojis', views.get_list, name='get-emojis')
]

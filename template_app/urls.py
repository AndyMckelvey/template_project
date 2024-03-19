from django.urls import path
from template_app import views
# /|\ change this

app_name = 'template_app'
# /|\ change this

urlpatterns = [
    path('', views.index, name='index'),
]

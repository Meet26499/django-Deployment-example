from basic_app import views
from django.urls import path

app_name = 'basic_app'


urlpatterns = [
    path('others/',views.others,name='others'),
    path('relative/',views.relative,name='relative')
]
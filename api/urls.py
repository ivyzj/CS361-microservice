from django.urls import path
from .views import ImageAPIView
#from . import views

urlpatterns = [
    path('', ImageAPIView.as_view()),
    path('title/<title>', ImageAPIView.as_view()),
    #path('', views.ImageAPI, name='post_single'),
]

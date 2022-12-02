from django.urls import path
from .views import FirstView, SecondView

urlpatterns = [
    path('1', FirstView.as_view(), name='first'),
    path('2', SecondView.as_view(), name='second')
]
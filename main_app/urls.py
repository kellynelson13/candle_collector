from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('candles/', views.candles_index, name="index"),
    path('candles/<int:candle_id>/', views.candles_detail, name='detail'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('candles/', views.candles_index, name="index"),
    path('candles/<int:candle_id>/', views.candles_detail, name='detail'),
    path('candle/create/', views.CandleCreate.as_view(), name='candle_create'),
    path('candle/<int:pk>/update/', views.CandleUpdate.as_view(), name='candles_update'),
    path('candle/<int:pk>/delete/', views.CandleDelete.as_view(), name='candles_delete'),
]

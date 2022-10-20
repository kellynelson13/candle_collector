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
    path('candles/<int:candle_id>/add_burning/', views.add_burning, name='add_burning'),
    path('enjoyers/', views.EnjoyerList.as_view(), name='enjoyers_index'),
    path('enjoyers/<int:pk>/', views.EnjoyerDetail.as_view(), name='enjoyers_detail'),
    path('enjoyers/create/', views.EnjoyerCreate.as_view(), name='enjoyers_create'),
    path('enjoyers/<int:pk>/update/', views.EnjoyerUpdate.as_view(), name='enjoyers_update'),
    path('enjoyers/<int:pk>/delete/', views.EnjoyerDelete.as_view(), name='enjoyers_delete'),
    path('candles/<int:candle_id>/assoc_enjoyer/<int:enjoyer_id>/', views.assoc_enjoyer, name='assoc_enjoyer'),
]

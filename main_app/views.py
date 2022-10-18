from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Candle

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# class Candle:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, scent, color, ounces, burn_time):
#     self.scent = scent
#     self.color = color
#     self.ounces = ounces
#     self.burn_time = burn_time
  
    

# candles = [
#   Candle('Tea Tree and Spearmint', 'cream', '5oz', '5 hours'),
#   Candle('Bridesmaid', 'white', '3oz', '4 hours'),
#   Candle('Honeycrisp Apple', 'green', '5.7oz', '6 hours')
# ]


def candles_index(request):
    candles = Candle.objects.all()
    return render(request, 'candles/index.html', { 'candles': candles})

def candles_detail(request, candle_id):
    candle = Candle.objects.get(id=candle_id)
    return render(request, 'candles/detail.html', { 'candle': candle })

class CandleCreate(CreateView):
    model = Candle
    fields = '__all__'

class CandleUpdate(UpdateView):
    model = Candle
    fields = ['scent', 'color', 'ounces', 'burn_time']

class CandleDelete(DeleteView):
    model = Candle
    success_url = '/candles/'

    
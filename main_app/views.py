from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Candle, Enjoyer
from .forms import BurningForm

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
    enjoyers_candle_doesnt_have = Enjoyer.objects.exclude(id__in = candle.enjoyers.all().values_list('id'))
    burning_form = BurningForm()
    return render(request, 'candles/detail.html', { 
        'candle': candle, 'burning_form': burning_form, 
        'enjoyers': enjoyers_candle_doesnt_have 
        })

def add_burning(request, candle_id):
  # create the ModelForm using the data in request.POST
  form = BurningForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the candle_id assigned
    new_burning = form.save(commit=False)
    new_burning.candle_id = candle_id
    new_burning.save()
    return redirect('detail', candle_id=candle_id)

def assoc_enjoyer(request, candle_id, enjoyer_id):
  # Note that you can pass a enjoyer's id instead of the whole object
  Candle.objects.get(id=candle_id).enjoyers.add(enjoyer_id)
  return redirect('detail', candle_id=candle_id)

class CandleCreate(CreateView):
    model = Candle
    fields = ['scent', 'color', 'ounces', 'burn_time']

class CandleUpdate(UpdateView):
    model = Candle
    fields = ['scent', 'color', 'ounces', 'burn_time']

class CandleDelete(DeleteView):
    model = Candle
    success_url = '/candles/'

    
class EnjoyerCreate(CreateView):
    model = Enjoyer
    fields = ('name', 'mood')

class EnjoyerUpdate(UpdateView):
    model = Enjoyer
    fields = ('name', 'mood')

class EnjoyerDelete(DeleteView):
    model = Enjoyer
    success_url = '/enjoyers/'

class EnjoyerDetail(DetailView):
    model = Enjoyer
    template_name = 'enjoyers/detail.html'

class EnjoyerList(ListView):
    model = Enjoyer
    template_name = 'enjoyers/index.html'
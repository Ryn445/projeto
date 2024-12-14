# views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Renderiza a página inicial (home)

# advogacia/views.py
from rest_framework import viewsets

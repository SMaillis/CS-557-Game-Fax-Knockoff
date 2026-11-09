from django.views import View
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'home.html')
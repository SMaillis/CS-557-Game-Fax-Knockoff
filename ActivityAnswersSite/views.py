from django.views import View
from django.shortcuts import render
from .models import Game, Question, Guide


class Home(View):
    def get(self, request):
        context = {
            'games': Game.objects.order_by('title'),
            'recent_questions': Question.objects.order_by('-created_at')[:5],
            'recent_guides': Guide.objects.order_by('-created_at')[:5],
        }
        return render(request, 'home.html', context)


# Placeholders so every route works; real logic comes with each card
class Games(View):
    def get(self, request):
        return render(request, 'games.html')


class Questions(View):
    def get(self, request):
        return render(request, 'questions.html')


class Guides(View):
    def get(self, request):
        return render(request, 'guides.html')


class Login(View):
    def get(self, request):
        return render(request, 'login.html')
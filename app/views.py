from django.shortcuts import render, redirect, get_list_or_404
from django.views import View

class HomeView(View):

    def get(self, request):
        return render(request, 'home.html')
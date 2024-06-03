from django.shortcuts import render, HttpResponse, redirect
from . import models
# Create your views here.
variables = {}
def home(request):
    variables['articles'] = models.Article.objects.all()
    # for art in models.Article.objects.all():
    #     subart = list(art.subarts.get())

    
    return render(request, 'Main/home.html', variables)
    # return HttpResponse(f'variables: {variables}')

from django.shortcuts import render
from django.http import HttpResponse
from template_app.models import Category


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    return render(request, 'template_app/index.html', context=context_dict)
    # /|\ Fix this


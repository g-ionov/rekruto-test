import code

from django.shortcuts import render
from django.views import View

from .services import get_code


class FirstView(View):
    """ View для первого задания """

    def get(self, request, *args, **kwargs):
        return render(request, 'app/first.html', {"code": get_code()})


class SecondView(View):
    """ View для второго задания"""

    def get(self, request, *args, **kwargs):
        return render(request, 'app/second.html', {"code": get_code()})



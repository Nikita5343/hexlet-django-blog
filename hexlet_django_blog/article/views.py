from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

def index(request):
    return render(
        request,
        "articles/index.html",
        context={
            "app_name": "Статьи",
        },
    )

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('article')
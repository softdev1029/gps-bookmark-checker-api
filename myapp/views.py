from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hello(request):
    #return render(request, "myapp/template/hello.html", {})
    text = "<h1>welcome to my app number %s!</h1>"
    return HttpResponse(text)



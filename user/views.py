from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template.response import TemplateResponse
from user.models import User

import datetime



def blog_index(request):
    return render(request, "index.html")



# Create your views here.
def current_datetime(request:HttpRequest):
    now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # print(html)
    # return HttpResponse(html)
    return render(request, "base2.html",{'time': "It is now %s" % now})
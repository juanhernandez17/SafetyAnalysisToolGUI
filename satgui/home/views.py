from django.shortcuts import render
from django.views.generic import TemplateView
from DoS.models import System
# Create your views here.

Homepage = {
    'DoS':{
        "name": 'Details Of System',
        "description":"",
        "icon":"home/clipboard.svg"
        
    },
    "SAT":{
        "name":"Safety Analysis",
        "description":"",
        "icon":"home/check.svg"
    },
    "SRD":{
        "name":"Safety Related Data",
        "description":"",
        "icon":"home/list1.svg"
    }

 }

class Home(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        return render(request, self.template_name,{"Homepage":Homepage})


class Index(TemplateView):
    template_name = 'home/index.html'

class Systems(TemplateView):
    template_name = 'home/Systems.html'
    def get(self, request):
        ls = System.objects.all().filter(User=request.user).values()
        return render(request, self.template_name, {"systemlist": ls})

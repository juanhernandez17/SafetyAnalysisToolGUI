from .forms import FormStepOne, UploadFileForm
from formtools.wizard.views import CookieWizardView
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.generic import TemplateView, View
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import System
from .forms import SystemCreationForm
from django.views.generic import TemplateView
from .get_file import get_file
from django.contrib import messages
from systemAPI.serializers import SystemDetailedSerializer
from .generate_file import generate_file

class DoS(TemplateView):
    template_name = 'DoS/DoS.html'
     
    def get(self,request):
        return render(request, self.template_name)
    def post(self,request):
        return render(request, self.template_name)
       


class File(TemplateView):
    template_name = 'DoS/DoS.html'
    fileform = UploadFileForm

    def get(self, request, id):
        try:
            onj = System.objects.get(pk=id)
            onjinfo = SystemDetailedSerializer(onj, context={'request': request})
            filename = onjinfo.data['name'].strip().replace(" ", "_")+".txt"
            response = HttpResponse(generate_file(onjinfo.data), content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
            return response
        except:
            messages.error(request,'Couldn\'t download that file')
        return redirect('home')

    def post(self, request):
        try:
            uploaded_file = request.FILES['file']
            get_file(uploaded_file.readlines(), uploaded_file.name, request)
            messages.success(
                request, f'Succesfully created System {uploaded_file.name} from file')
            return redirect('DoS')

        except:
            messages.error(
                request, f'Error while parsing file')
            return redirect('DoS')



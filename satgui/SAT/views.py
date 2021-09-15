from django.shortcuts import render, redirect
from django.views import View
from DoS.forms import SystemCreationForm
from DoS.models import System as Sysdb
from DoS.models import Component
from django.contrib import messages

# Create your views here.


class Sat(View):
    template_name = 'SAT/sat.html'
    form = SystemCreationForm
    

    def get(self, request, id=0):
        form = SystemCreationForm()
        syslist = Sysdb.objects.filter(User=request.user)
        return render(request, self.template_name, {"data": syslist, "form": form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            if request.POST['system_id']:
                try:
                    sys = Sysdb.objects.get(pk=request.POST['system_id'])
                    messages.success(
                        request, f'System Updated Successfully')
                except:
                    name = request.POST['name']
                    messages.error(request, f'Couldn\'t find {name} in the database')
                    return render(request, self.template_name, {'form': form})
                system = self.form(request.POST, instance=sys)
            else:
                system = form.save(commit=False)
                system.User = request.user
                messages.success(
                    request, f'System {system.name} Created Successfully')
            system.save()


            return redirect('SAT')

        return render(request, self.template_name, {'form': form})

from django import forms
from .models import *#System,Component
from .validators import validate_file_extension
class FormStepOne(forms.Form):
    system_name = forms.CharField(max_length=100, required=False)
    system_description = forms.CharField(widget=forms.Textarea, required=False)


class SystemCreationForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea, required=False)
    system_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = System
        fields = ['name', 'description','system_id']
        # widgets = {'description': forms.Textarea(attrs={'cols': 80, 'rows': 20})}
        exclude = ('user',)
        # widgets = {'id': forms.HiddenInput()}

    def clean(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        description = self.cleaned_data.get('description')
#------------------------------------------------

class ComponentCreationForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea, required=False)
    component_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Component
        fields = ['name', 'description','component_id']
        # widgets = {'description': forms.Textarea(attrs={'cols': 80, 'rows': 20})}
        exclude = ('user',)
        # widgets = {'id': forms.HiddenInput()}

    def clean(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        description = self.cleaned_data.get('description')
#------------------------------------------------

class UploadFileForm(forms.Form):
    file = forms.FileField(validators=[validate_file_extension])

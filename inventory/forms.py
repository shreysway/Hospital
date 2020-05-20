from django import forms
from .models import *

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptops
        fields = ('Specialization', 'DoctorName', 'Patient', 'issues')


class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktops
        fields = ('Specialization', 'DoctorName', 'Patient', 'issues')
        

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobiles
        fields = ('Specialization', 'DoctorName', 'Patient', 'issues')

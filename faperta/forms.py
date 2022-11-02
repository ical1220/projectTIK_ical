from dataclasses import fields
from django.forms import ModelForm
from faperta.models import dosen
from faperta.models import mahasiswa
from faperta.models import staff

class FormDosen(ModelForm):
    class Meta:
        model = dosen
        fields = '__all__'

class FormMahasiswa(ModelForm):
    class Meta:
        model = mahasiswa
        fields = '__all__'

class FormStaff(ModelForm):
    class Meta:
        model = staff
        fields = '__all__'
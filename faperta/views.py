from django.shortcuts import render, redirect
from faperta.models import dosen
from faperta.models import mahasiswa
from faperta.models import staff
from faperta.forms import FormDosen
from faperta.forms import FormMahasiswa
from faperta.forms import FormStaff

# Create your views here.
def faperta(request):
    return render(request, 'indexfaperta.html')

def tambah_dosen(request):
    if request.POST:
        form = FormDosen(request.POST)
        if form.is_valid():
            form.save()
            form = FormDosen()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-dosen.html', konteks)
    else:
    
        form = FormDosen()

        konteks = {
            'form': form,
        }

    return render(request, 'tambah-dosen.html', konteks)

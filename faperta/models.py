from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class dosen(models.Model):
    nama = models.CharField(max_length=50)
    NIP = models.CharField(max_length=40)
    tanggal_lahir = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    fakultas = models.CharField(max_length=40)
    prodi = models.CharField(max_length=40)
    alamat = models.CharField(max_length=40)
    
    def __str__(self):
        return self.nama

class mahasiswa(models.Model):
    nama = models.CharField(max_length=50)
    NIM = models.CharField(max_length=40)
    tanggal_lahir = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    fakultas = models.CharField(max_length=40)
    prodi = models.CharField(max_length=40)
    
    def __str__(self):
        return self.nama

class staff(models.Model):
    nama = models.CharField(max_length=50)
    NIP = models.CharField(max_length=40)
    tanggal_lahir = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    unit = models.CharField(max_length=40)
    alamat = models.CharField(max_length=40)
    
    def __str__(self):
        return self.nama
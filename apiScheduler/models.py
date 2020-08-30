from django.db import models
from users.models import User

class Etablissement(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name 
        
class Specialite(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self): 
        return self.name

class LieuConsul(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    region = models.CharField(max_length=50)
    deps = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    name1 = models.CharField(max_length=50, blank=True, null=True)
    name2 = models.CharField(max_length=50)

    def __str__(self): 
        return self.name2
    
class Contacts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    fax = models.CharField(max_length=50, blank=True, null=True)

class Horaire(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jour = models.CharField(max_length=50)
    debut = models.TimeField()
    fin = models.TimeField()


class BasePatient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self): 
        return self.name

class FichePatient(models.Model):
    base = models.ForeignKey(BasePatient, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone1 = models.CharField(max_length=50)
    phone2 = models.CharField(max_length=50)
    birthday = models.DateField()
    adresse = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)
    remarques = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)


class Ressources(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

class Agenda(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ressource = models.ForeignKey(Ressources, on_delete=models.CASCADE)
    lieu = models.ForeignKey(LieuConsul, on_delete=models.CASCADE)
    base = models.ForeignKey(BasePatient, on_delete=models.CASCADE)
    specialite = models.CharField(max_length=50)

class MotifConsult(models.Model):
    pass
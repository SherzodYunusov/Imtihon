from django.db import models
from django.contrib.auth.models import User

class Muallif(models.Model):
    ism = models.CharField(max_length=50)
    yosh = models.PositiveSmallIntegerField()
    kasb = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.ism

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=100)
    sana = models.DateField()
    mavzu = models.CharField(max_length=100)
    matn = models.TextField()
    muallif1 = models.ForeignKey(Muallif, on_delete=models.CASCADE)
    def __str__(self):
        return self.sarlavha

# Create your models here.

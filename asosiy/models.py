from django.db import models
from django.contrib.auth.models import User


class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.PositiveSmallIntegerField(blank=True)
    kasbi = models.CharField(max_length=50, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ism}"


class Maqola(models.Model):
    sarlavha = models.CharField(max_length=50)
    sana = models.DateField(blank=True, null=True)
    mavzu = models.CharField(max_length=50, blank=True)
    matn = models.TextField()
    muallif = models.ForeignKey(Muallif, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.sarlavha}"

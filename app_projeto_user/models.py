from django.db import models

class User_aula1(models.Model):
    id_user = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255)
    age = models.IntegerField()
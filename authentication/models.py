from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
   created_at = models.DateTimeField(auto_now_add=True, null=True)
   updated_at = models.DateTimeField(auto_now=True)

   class Meta:
      abstract = True

class Departement(BaseModel):
    name = models.CharField(max_length=100 , unique= True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class Service(BaseModel):
    name = models.CharField(max_length=100 , unique= True)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, related_name='departement')
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class Unite(BaseModel):
    name = models.CharField(max_length=100 , unique= True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service')
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class User(AbstractUser):
    unite = models.ForeignKey(Unite,on_delete=models.SET_NULL,related_name='unite', null=True, blank=True)
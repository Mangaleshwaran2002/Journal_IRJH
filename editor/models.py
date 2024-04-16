from django.db import models
from django.db.models.query import QuerySet
from app_auth.models import User,Role
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class EditiorManager(BaseUserManager):

    def get_queryset(self,*args,**kwargs) -> QuerySet:
        result=super().get_queryset(*args,**kwargs)
        return result.filter(role=Role.EDITOR).all()

class Editior(User):
    base_role=Role.EDITOR
    author=EditiorManager()
    class Meta:
        proxy = True
        verbose_name_plural = "Editior"


class Editors(models.Model):
    title=models.CharField(verbose_name="editor title",max_length=150,null=True,blank=True)
    name=models.CharField(verbose_name="editor name",max_length=150,null=False,blank=False)
    bio=models.TextField(verbose_name="editor bio")
    location=models.CharField(verbose_name="editor location",max_length=250,null=True,blank=True)
    email=models.EmailField(verbose_name="editor email")

    def __str__(self) -> str:
        return str(self.name)
    
    class Meta:
        verbose_name_plural = "Editors"
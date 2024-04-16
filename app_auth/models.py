from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Role(models.TextChoices):
    ADMIN="ADMIN","Admin"
    AUTHOR="AUTHOR","Author"
    EDITOR="EDITOR","Editor"

class User(AbstractUser):
    role=models.CharField(_("role"),max_length=80,blank=False,choices=Role.choices)
    orcid=models.SlugField(_("orcid"),blank=True)
    base_role=Role.ADMIN
    def save(self,*args,**kwargs):

        if not self.pk:
            self.role=self.base_role
            if len(self.password) < 30:
                # self.passwd=f.encrypt(self.password.encode()).decode()
                self.set_password(self.password)
        return super().save(*args,**kwargs)
        
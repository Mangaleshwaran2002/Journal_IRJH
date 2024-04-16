from django.db import models
from app_auth.models import User
# Create your models here.
class Volume(models.Model):
    name=models.CharField(max_length=150,verbose_name="volume",null=False)

    def __str__(self) -> str:
        return str(self.name)
    

    

class Manuscript(models.Model):
    m_id=models.CharField(max_length=300,verbose_name="Manuscript id",null=True,blank=True)
    Title=models.CharField(max_length=300,verbose_name="Manuscript title",null=True,blank=True)
    Type=models.CharField(max_length=50,verbose_name="Manuscript type",null=True,blank=True)
    abstract=models.TextField(verbose_name="Manuscript abstract",null=True,blank=True)
    pub_date=models.DateField(auto_now=True,verbose_name="Manuscript publish date")
    volume=models.ForeignKey(to=Volume,on_delete=models.DO_NOTHING,verbose_name="Manuscript volume",related_name="Volume",null=True,blank=True)
    pdf_file=models.FileField(verbose_name="Manuscript pdf",upload_to="Manuscripts")
    verified=models.BooleanField(verbose_name="Manuscript verified",default=False)
    under_review=models.BooleanField(verbose_name="Manuscript under review",default=True)
    author=models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name="Manuscript author",related_name="Author",null=True,blank=True)
    co_authors=models.CharField(max_length=300,verbose_name="Manuscript co-authors",null=True,blank=True)

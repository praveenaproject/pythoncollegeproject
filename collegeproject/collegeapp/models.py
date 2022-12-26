from django.db import models

# Create your models here.
class Department(models.Model):
    dname=models.CharField(max_length=250,blank=True,null=True)


    def __str__(self):
        return self.dname


class Branch(models.Model) :
    department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)
    bname=models.CharField(max_length=250,blank=True,null=True)


    def __str__(self):
        return self.bname



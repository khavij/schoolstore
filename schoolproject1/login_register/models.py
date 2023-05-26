from django.db import models

class Datas(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    phoneno = models.IntegerField()
    mailid = models.EmailField()
    address= models.CharField(max_length=250)
    department = models.CharField(max_length=250)
    course = models.CharField(max_length=250)
    purpose = models.CharField(max_length=250)
    notebook = models.CharField(max_length=250,null=True)
    pen = models.CharField(max_length=250 ,null=True)
    record = models.CharField(max_length=250,null=True)
    uniform = models.CharField(max_length=250,null=True)
    exampaper = models.CharField(max_length=250,null=True)
    def __str__(self):
        return self.name
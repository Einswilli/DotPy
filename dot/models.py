from email.policy import default
from django.db import models

# Create your models here.

class User(models.Model):
    UserID=models.AutoField(primary_key=True)
    UserFName=models.CharField(max_length=50)
    UserLName=models.CharField(max_length=50)
    UserEmail=models.EmailField(max_length=150)
    UserNumber=models.IntegerField()
    UserJob=models.CharField(max_length=150)
    UserPass=models.CharField(max_length=25)
    UserPhoto=models.ImageField()
    JoinedAt=models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.UserFName} {self.UserLName[1]}.'


class Designer(models.Model):
    DesignerID=models.AutoField(primary_key=True)
    DesignerFName=models.CharField(max_length=50)
    DesignerLName=models.CharField(max_length=50)
    DesignerEmail=models.EmailField(max_length=150)
    DesignerNumber=models.IntegerField()
    DesignerJob=models.CharField(max_length=150)
    DesignerPass=models.CharField(max_length=25)
    DesignerPhoto=models.ImageField(default='static/assets/img/py.png')
    JoinedAt=models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.DesignerFName} {self.DesignerLName[1]}.' 


class Oeuvre(models.Model):

    OID=models.AutoField(primary_key=True)
    Title=models.CharField(max_length=50)
    Description=models.CharField(max_length=500)
    OType=models.CharField(max_length=15)
    OImage=models.ImageField()
    AddedAt=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Title


class Email(models.Model):

    MailID=models.AutoField(primary_key=True)
    Subject=models.CharField(max_length=70)
    Message=models.CharField(max_length=2000)
    Author=models.ForeignKey("Suscriber",on_delete=models.CASCADE)
    SentAt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Subject

class Suscriber(models.Model):

    SID=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50)
    Email=models.CharField(max_length=200)
    JoinedAt=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Name


class Template(models.Model):

    TempID=models.AutoField(primary_key=True)
    TempName=models.CharField(max_length=70)
    TempDesc=models.CharField(max_length=500)
    Tempfile=models.FileField()
    TempImg=models.ImageField()
    TempPrice=models.FloatField()
    tempAthor=models.ForeignKey("Suscriber",on_delete=models.CASCADE)
    AddedAt=models.DateField(auto_now_add=True)

    def __str__(self) :
        return self.TempName


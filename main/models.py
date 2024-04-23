from django.db import models

# Create your models here.

class AppInfo(models.Model):
    appname = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logo')
    copyright = models.IntegerField()

    def  __str__(self):
        return self.appname

class AboutMe(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    pix = models.ImageField(upload_to='pix')

    def __str__(self):
        return self.name
    
class Sevices(models.Model):
    name = models.CharField(max_length=50)
    title= models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=104)
    date = models.DateField()
    service_type = models.ForeignKey(Sevices, on_delete=models.CASCADE)
    additional_info = models.TextField()
    upload_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class MyWorks(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='jobsd')
    review = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.name
    


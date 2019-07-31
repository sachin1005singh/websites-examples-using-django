from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Collagelist(models.Model):

    name = models.CharField(max_length= 100)
    url = models.URLField(max_length= 100)
    emailid = models.EmailField()
    about = models.TextField(max_length= 1000,default=True)
    

    def __str__(self):
        return self.name +" ------- "+ self.emailid

class Collagedetail(models.Model):
    collage = models.ForeignKey(Collagelist,on_delete= models.CASCADE)
    course = models.CharField(max_length= 100)
    upload = models.FileField()

    def __str__(self):
        return self.course +" ----- " +str(self.upload)

class Contact(models.Model):
    std_name = models.CharField(max_length= 100)
    email_id = models.EmailField()
    contact = models.TextField(max_length= 1000)

    def __str__(self):
        return self.name + "---------------" + self.email_id






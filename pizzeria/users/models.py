from django.db import models

# Create your models here.
'''
class User(models.Model):
    username = models.CharField(max_length=15,blank=False)
    first_name = models.CharField(max_length=15, blank=False)
    last_name = models.CharField(max_length=15, blank=False)
    phone_number = models.CharField(max_length=15, blank=False)
    address = models.CharField(max_length=50, blank=False)
    address2 = models.CharField(max_length=50, blank=True,null=True)
    town = models.CharField(max_length=20, blank=False)
    state = models.CharField(max_length=15, blank=False)
    zip_code = models.CharField(max_length=5, blank=False )
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','last_name','phone_number','address','town','state','zip_code'] 

    def __str__(self):
        return str(self.id) + self.name
'''

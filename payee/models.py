from django.db import models
from accounts.models import User
import random
# Create your models here.
    # print(random.randint(123123123123,947258369125))

class Payee(models.Model):
    id=models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    ifsc = models.CharField(max_length=100)
    account_number = models.IntegerField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  

     
                                                         
                                                 
 
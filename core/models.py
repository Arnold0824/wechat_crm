from django.db import models

class users(models.Model):
    clientid=models.CharField('微信用户openid',max_length=50,null=False,blank=True)

# Create your models here.

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.



class MusicModel(models.Model):
    name = models.CharField(max_length=300,default='')
    creator_name = models.CharField(max_length=200,default='')
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.now)
    desc = models.TextField(default='Do you like music?')
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)


    class Meta:
        db_table = 'MusicModel'
    def __str__(self) -> str:
        return self.name
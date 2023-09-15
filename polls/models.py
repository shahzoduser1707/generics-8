from django.db import models
from datetime import datetime
# Create your models here.



class MusicModel(models.Model):
    name = models.CharField(max_length=300,default='')
    creator_name = models.CharField(max_length=200,default='')
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.now)
    desc = models.TextField(default='Do you like music?')


    class Meta:
        db_table = 'MusicModel'
    def __str__(self) -> str:
        return self.name
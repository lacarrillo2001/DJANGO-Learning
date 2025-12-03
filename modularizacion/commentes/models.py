from django.db import models

# Create your models here.
class Comment(models.Model):
     name = models.CharField(max_length=255,null=False)
     score = models.IntegerField(default=3)
     Comment_text = models.TextField(max_length=10000,null=True)
     date_created = models.DateTimeField(null=True)
     signature = models.CharField(max_length=255,default='Anonimo')

     def __str__(self):
          return self.name
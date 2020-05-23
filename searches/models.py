from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class SearchQuery(models.Model):
   user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
   query = models.CharField(max_length=100)
   timestamp = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return self.query


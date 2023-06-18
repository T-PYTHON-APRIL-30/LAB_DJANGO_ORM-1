from django.db import models

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    models.BooleanField(default=False)
    publish_date=models.DateTimeField(auto_now_add=True)
    


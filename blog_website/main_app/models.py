from django.db import models

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    models.BooleanField(default=False)
    publish_date=models.Date.Time.Field(auto_now_add=True)

def __str__(self):
    return self.title

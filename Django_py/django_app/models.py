from django.db import models

# Create your models here.
class ArticalModel(models.Model):
    title = models.CharField(max_length=150, verbose_name= 'Title')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.title
    
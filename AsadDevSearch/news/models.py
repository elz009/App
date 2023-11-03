from django.db import models

# Create your models here.


class Articles(models.Model):
    title = models.CharField('Name', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('text')
    date = models.DateTimeField('Publish Time')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Novost"
        verbose_name_plural = "Novosti"
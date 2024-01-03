from django.db import models

# Create your models here.

class Movies(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    year = models.DateField(null=True, blank=True)   #null=If True, Django will store empty values as NULL in the database. Default is False.
#blank- If True, the field is allowed to be blank. Default is False.
    image = models.ImageField(upload_to='pics')

    class Meta:
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.name



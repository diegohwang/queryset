from django.db import models

# Create your models here.


class site(models.Model):
    site_name = models.CharField(max_length=128)
    site_code = models.CharField(max_length=128)
    site_id = models.IntegerField()
    
    def __str__(self):
        return self.site_name
    
class media(models.Model):
    title = models.CharField(max_length=128)
    url = models.URLField(max_length=128)
    belong_site = models.ForeignKey(site)
    
    def __str__(self):
        return self.title
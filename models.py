from django.db import models 
from django.template.defaultfilters import slugify

class Project(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    main_image = models.ImageField(upload_to='projects/photos', blank=True, help_text='Try for 1800x1200. Darker, non-busy images work best as a background.')
    start_date = models.DateField(blank=True)
    slug = models.CharField(max_length=100, blank=True)
    viewable = models.BooleanField(help_text='Should this page show at dataomaha.com/projects?')

    def __unicode__(self):
        return self.title
		
class Installment(models.Model):
    series = models.ForeignKey(Project)
    date = models.DateField(blank=True)
    headline = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/photos/', blank=True)
    link = models.CharField(max_length=200)

    def __unicode__(self):
        return self.headline

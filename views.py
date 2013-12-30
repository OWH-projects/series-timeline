from myproject.projects.models import *
from django.shortcuts import *
from django.db.models import *


def Main(request):
    list = Project.objects.filter(viewable=True).order_by('-start_date')

    dictionaries = { 'list': list, }
    return render_to_response('projects/main.html', dictionaries)

def Detail(request, slug):
    series = Project.objects.get(slug=slug)
    stories = series.installment_set.all().order_by('date')
    
    dictionaries = { 'series': series, 'stories': stories, }
    return render_to_response('projects/detail.html', dictionaries)

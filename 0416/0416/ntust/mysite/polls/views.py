from django.shortcuts import render_to_response
from django.http import HttpResponse

from .models import Person

# creat ypur views here
def index(request):
	people = Person.objects.all()
	return render_to_response('polls/menu.html',locals())


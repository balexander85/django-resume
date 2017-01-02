from django.shortcuts import render_to_response
from main.models import resume_experience
from main.models import resume_objective
from main.models import resume_education
from main.models import resume_skills
from main.models import resume_interest
from main.models import resume_projects


def index(request):
    return render_to_response('main/index.html',
	{
	'objectives': resume_objective.objects.all(),
	'jobs': resume_experience.objects.all().order_by('id').reverse(),
	'education': resume_education.objects.all(),
	'skills': resume_skills.objects.all(),
	'special_interest': resume_interest.objects.all(),
	'projects': resume_projects.objects.all(),
    })

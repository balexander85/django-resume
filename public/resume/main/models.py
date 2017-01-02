from __future__ import unicode_literals

from django.db import models

class resume_experience(models.Model):
	job_id = models.FloatField()
	company_name = models.TextField()
	job_location = models.CharField(max_length=100, unique=False)
	position_title = models.CharField(max_length=100, unique=False)
	dates_of_employment = models.CharField(max_length=100, unique=False)
	job_description = models.TextField()

class resume_objective(models.Model):
	objective = models.TextField()

class resume_education(models.Model):
	education = models.TextField()

class resume_skills(models.Model):
	skills = models.TextField()

class resume_interest(models.Model):
	interest = models.TextField()

class resume_projects(models.Model):
	projects = models.TextField()

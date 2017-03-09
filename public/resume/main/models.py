from __future__ import unicode_literals

from django.db import models

class resume_experience(models.Model):
    job_id = models.FloatField()
    company_name = models.TextField()
    job_location = models.CharField(max_length=100, unique=False)
    position_title = models.CharField(max_length=100, unique=False)
    dates_of_employment = models.CharField(max_length=100, unique=False)
    job_description = models.TextField()

    class Meta:
        verbose_name = u'Jobs'
        verbose_name_plural = u'Jobs'


class resume_objective(models.Model):
    objective = models.TextField()

    class Meta:
        verbose_name = u'Objective'
        verbose_name_plural = u'Objectives'


class resume_education(models.Model):
    education = models.TextField()

    class Meta:
        verbose_name = u'Education'
        verbose_name_plural = u'Education'


class resume_skills(models.Model):
    skills = models.TextField()

    # Boilerplate code to make a prettier display in the admin interface.
    class Meta:
        verbose_name = u'Skills'
        verbose_name_plural = u'Skills'


class resume_interest(models.Model):
    interest = models.TextField()

    class Meta:
        verbose_name = u'Interest'
        verbose_name_plural = u'Interests'


class resume_projects(models.Model):
    projects = models.TextField()

    class Meta:
        verbose_name = u'Projects'
        verbose_name_plural = u'Projects'


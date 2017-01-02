from django.contrib import admin
from .models import resume_experience
from .models import resume_objective
from .models import resume_education
from .models import resume_skills
from .models import resume_interest
from .models import resume_projects

# class resume_experience(admin.ModelAdmin):
#     list_display = ('company_name', 'position_title', 'dates_of_employment')


admin.site.register(resume_experience)
admin.site.register(resume_objective)
admin.site.register(resume_education)
admin.site.register(resume_skills)
admin.site.register(resume_interest)
admin.site.register(resume_projects)

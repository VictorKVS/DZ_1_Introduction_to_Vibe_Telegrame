from django.contrib import admin

from .models import Evidence, Goal, Problem, Project, Source

admin.site.register(Project)
admin.site.register(Goal)
admin.site.register(Problem)
admin.site.register(Source)
admin.site.register(Evidence)

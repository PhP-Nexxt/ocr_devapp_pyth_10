from django.contrib import admin
from api_softdesk.models import Project, Contributor, Issue, Comment

# Register your models here.

# In admin
admin.site.register(Project)
admin.site.register(Contributor)
admin.site.register(Issue)
admin.site.register(Comment)


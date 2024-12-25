from django.contrib import admin
from .models import Type,Animal,Medical,Staff,Task,Event
# Register your models here.
admin.site.register(Type)
admin.site.register(Animal)
admin.site.register(Medical)
admin.site.register(Staff)
admin.site.register(Task)
admin.site.register(Event)
# Compare this snippet from animal/views.py:


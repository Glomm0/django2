from django.contrib import admin
from .models import TakenTask,Task
# Register your models here.

admin.site.register(Task)
admin.site.register(TakenTask)
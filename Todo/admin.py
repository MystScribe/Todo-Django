from django.contrib import admin
from . models import TodoModel

@admin.register(TodoModel)
class ModelNameAdmin(admin.ModelAdmin):
    pass

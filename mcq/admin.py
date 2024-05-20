from django.contrib import admin
from .models import CustomUser, Result, AllQuestions

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Result)
admin.site.register(AllQuestions)

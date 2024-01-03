from django.contrib import admin

# Register your models here.
from . models import Student,Items,Movies
admin.site.register(Student)
admin.site.register(Items)
admin.site.register(Movies)
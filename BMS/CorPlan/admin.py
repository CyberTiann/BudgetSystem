from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import annual, quarter
# Register your models here.
admin.site.register(annual)
admin.site.register(quarter)
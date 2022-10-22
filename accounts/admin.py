from django.contrib import admin
from .models import User, Profile

# Register your models here.
admin.site.site_header = "My Administration"


admin.site.register(User)
admin.site.register(Profile)

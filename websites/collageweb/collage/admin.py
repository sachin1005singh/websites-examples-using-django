from django.contrib import admin
from .models import Collagelist, Collagedetail,Contact
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Collagelist)
admin.site.register(Collagedetail)
admin.site.register(Contact)
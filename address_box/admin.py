from django.contrib import admin
from .models import Person, Email, Group


admin.site.register(Person)
admin.site.register(Email)
admin.site.register(Group)

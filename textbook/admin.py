from django.contrib import admin
from .models import Syllabus
from .models import Module
from .models import Unit
from .models import UserProgress

# Register your models here.
admin.site.register(Syllabus)
admin.site.register(Module)
admin.site.register(Unit)
admin.site.register(UserProgress)
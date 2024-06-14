from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

# Unsure about how I should name related_name
class Syllabus(models.Model):
    syllabus_title = models.CharField(max_length=200, unique=True)
    syllabus_slug = models.SlugField(max_length=200, unique=True)  #PK
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="syllabus_instance")  # FK
    created_on = models.DateTimeField(auto_now_add=True)
    deadline_official = models.DateTimeField(auto_now_add=True)
    status_syllabus = models.IntegerField(choices=STATUS, default=0)

class Module(models.Model):
    syllabus_slug = models.ForeignKey(Syllabus, on_delete=models.CASCADE, related_name="module_instance")  # FK
    module_title = models.CharField(max_length=200, unique=True)
    module_slug = models.SlugField(max_length=200, unique=True)  #PK
    author = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status_syllabus = models.IntegerField(choices=STATUS, default=0)

class Unit(models.Model):
    module_slug = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="unit_instance")  #FK
    unit_title = models.CharField(max_length=200, unique=True)
    unit_slug = models.SlugField(max_length=200, unique=True)  # PK
    category = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=200, unique=True)
    status_syllabus = models.IntegerField(choices=STATUS, default=0)

class UserProgress (models.Model):  # CamelCase!?
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_progress_instance")  # PK, FK
    unit_slug = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="user_progress_instance")  # FK
    deadline_set = models.DateTimeField(auto_now_add=True)
    pace_set = models.DateTimeField(auto_now_add=True)
    pace_you = models.DateTimeField(auto_now_add=True)
    last_visited = models.DateTimeField(auto_now_add=True)
    been_here = models.BooleanField(max_length=200, unique=True)
    read = models.BooleanField(max_length=200, unique=True)
    understood = models.BooleanField(max_length=200, unique=True)
    bookmark = models.BooleanField(max_length=200, unique=True)
    user_notes = models.CharField(max_length=200, unique=True)
    highlights = models.CharField(max_length=200, unique=True)
    unit_feedback = models.CharField(max_length=200, unique=True)

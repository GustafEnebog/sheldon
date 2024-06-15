from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
# Info on autoslug used below: https://django-autoslug.readthedocs.io/en/latest/

class Syllabus(models.Model):
    # syllabus_id = models.IntegerField(unique=True)  #PK    id = models.IntegerField(primary_key=True, blank=False, null=False, unique=True)
    syllabus_title = models.CharField(max_length=200, unique=True)
    # slug = AutoSlugField(populate_from='syllabus_title')
    syllabus_slug = models.SlugField(max_length=200, unique=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="syllabus_user")  # FK
    created_on = models.DateTimeField(auto_now_add=True)
    deadline_official = models.DateTimeField(auto_now_add=True)
    status_syllabus = models.IntegerField(choices=STATUS, default=0)


class Module(models.Model):
    # module_id = models.IntegerField(unique=True)  #PK
    syllabus_id = models.ForeignKey(Syllabus, on_delete=models.CASCADE, related_name="syllabus_module")  # FK
    module_title = models.CharField(max_length=200, unique=True)
    module_slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    status_syllabus = models.IntegerField(choices=STATUS, default=0)


class Unit(models.Model):
    # unit_id = models.IntegerField(unique=True)  #PK
    module_id = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="module_unit")  #FK
    unit_title = models.CharField(max_length=200, unique=True)
    unit_slug = models.SlugField(max_length=200, unique=True)
    category = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=200)
    status_syllabus = models.IntegerField(choices=STATUS, default=0)


class UserProgress (models.Model):  # CamelCase!?
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_user_progress")  # PK, FK
    unit_id = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="unit_user_progress")  # FK
    deadline_set = models.DateTimeField(auto_now_add=True)
    pace_set = models.DateTimeField(auto_now_add=True)
    pace_you = models.DateTimeField(auto_now_add=True)
    last_visited = models.DateTimeField(auto_now_add=True)
    been_here = models.BooleanField(max_length=200)
    read = models.BooleanField(max_length=200)
    understood = models.BooleanField(max_length=200)
    bookmark = models.BooleanField(max_length=200)
    user_notes = models.CharField(max_length=200)
    highlights = models.CharField(max_length=200)
    unit_feedback = models.CharField(max_length=200)

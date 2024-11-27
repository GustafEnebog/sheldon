from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Syllabus(models.Model):
    syllabus_title = models.CharField(max_length=200, unique=True)
    syllabus_slug = models.SlugField(max_length=200, unique=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="syllabus_user")  # FK
    created_on = models.DateTimeField(auto_now_add=True)
    deadline_official = models.DateTimeField(auto_now_add=True)
    status_syllabus = models.IntegerField(choices=STATUS, default=0)


class Module(models.Model):
    module_id = models.IntegerField(unique=True, null=True)  # PK
    syllabus_id = models.ForeignKey(Syllabus, on_delete=models.CASCADE, related_name="syllabus_module")  # FK
    module_title = models.CharField(max_length=200, unique=True)
    module_slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    status_module = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"{self.module_title} | written by {self.author}"


class Unit(models.Model):
    unit_id = models.IntegerField(unique=True, null=True)  # PK
    module_id = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="module_unit")  # FK
    unit_title = models.CharField(max_length=200, unique=True)
    unit_slug = models.SlugField(max_length=200, unique=True)
    category = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField(max_length=1000)
    status_unit = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"{self.unit_title} | written by {self.author}"


class UserProgress (models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_user_progress", null=True)  # PK, FK
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


class Note(models.Model):
    unit_id = models.ForeignKey(Unit, on_delete=models.CASCADE,
                                related_name="unit_note")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name="user_note")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

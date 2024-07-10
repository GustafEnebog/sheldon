from django.contrib import admin
from .models import Syllabus
from .models import Module
from .models import Unit
from .models import UserProgress
from .models import Note
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Syllabus)
class SyllabusAdmin(SummernoteModelAdmin):

    list_display = ('syllabus_title', 'syllabus_slug', 'status_syllabus')
    search_fields = ['syllabus_title']
    list_filter = ('status_syllabus',)
    prepopulated_fields = {'syllabus_slug': ('syllabus_title',)}
    #summernote_fields = ('content',)

    #syllabus_title = models.CharField(max_length=200, unique=True)
    #syllabus_slug = models.SlugField(max_length=200, unique=True)
    #user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="syllabus_user")  # FK
    #created_on = models.DateTimeField(auto_now_add=True)
    #deadline_official = models.DateTimeField(auto_now_add=True)
    #status_syllabus = models.IntegerField(choices=STATUS, default=0)


@admin.register(Module)
class ModuleAdmin(SummernoteModelAdmin):

    list_display = ('module_title', 'module_slug', 'status_module')
    search_fields = ['module_title']
    list_filter = ('status_module',)
    prepopulated_fields = {'module_slug': ('module_title',)}
    #summernote_fields = ('content',)

    #syllabus_id = models.ForeignKey(Syllabus, on_delete=models.CASCADE, related_name="syllabus_module")  # FK
    #module_title = models.CharField(max_length=200, unique=True)
    #module_slug = models.SlugField(max_length=200, unique=True)
    #author = models.CharField(max_length=200)
    #created_on = models.DateTimeField(auto_now_add=True)
    #status_module = models.IntegerField(choices=STATUS, default=0)


@admin.register(Unit)
class UnitAdmin(SummernoteModelAdmin):

    list_display = ('unit_title', 'unit_slug', 'status_unit')
    search_fields = ['unit_title']
    list_filter = ('status_unit',)
    prepopulated_fields = {'unit_slug': ('unit_title',)}
    #sssummernote_fields = ('content',)

    #module_id = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="module_unit")  #FK
    #unit_title = models.CharField(max_length=200, unique=True)
    #unit_slug = models.SlugField(max_length=200, unique=True)
    #category = models.CharField(max_length=200)
    #author = models.CharField(max_length=200)
    #created_on = models.DateTimeField(auto_now_add=True)
    #content = models.TextField(max_lengh=200)
    #status_unit = models.IntegerField(choices=STATUS, default=0)


@admin.register(UserProgress)
class UserProgressAdmin(SummernoteModelAdmin):

    list_display = ('user_notes', 'user_notes')
    search_fields = ['user_notes']
    #list_filter = ('user_notes')
    prepopulated_fields = {'user_notes': ('user_notes',)}


@admin.register(Note)
class NoteAdmin(SummernoteModelAdmin):

    pass

# Register your models here.
# admin.site.register(Syllabus)
# admin.site.register(Module)
# admin.site.register(Unit)
# admin.site.register(UserProgress)

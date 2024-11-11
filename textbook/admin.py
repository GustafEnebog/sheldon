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


@admin.register(Module)
class ModuleAdmin(SummernoteModelAdmin):

    list_display = ('module_title', 'module_slug', 'status_module')
    search_fields = ['module_title']
    list_filter = ('status_module',)
    prepopulated_fields = {'module_slug': ('module_title',)}


@admin.register(Unit)
class UnitAdmin(SummernoteModelAdmin):

    list_display = ('unit_title', 'unit_slug', 'status_unit')
    search_fields = ['unit_title']
    list_filter = ('status_unit',)
    prepopulated_fields = {'unit_slug': ('unit_title',)}


@admin.register(UserProgress)
class UserProgressAdmin(SummernoteModelAdmin):

    list_display = ('user_notes', 'user_notes')
    search_fields = ['user_notes']
    prepopulated_fields = {'user_notes': ('user_notes',)}


@admin.register(Note)
class NoteAdmin(SummernoteModelAdmin):

    list_display = ('created_on', 'body')

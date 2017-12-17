from django.contrib import admin

from .models import *


class InstituteAdmin(admin.ModelAdmin):
    list_display = ['name']


class TeacherInline(admin.TabularInline):
    model = Group.teachers.through

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'middle_name']
    inlines = [TeacherInline]


class GroupAdmin(admin.ModelAdmin):
    fields = ['name', 'department']
    list_display = ['name', 'department']
    inlines = [TeacherInline]


admin.site.register(Institute, InstituteAdmin)
admin.site.register(Department)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Vote)
admin.site.register(ResponseStudent)

"""
Definition of models.
"""

from django.db import models


class Institute(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    institute = models.ForeignKey(Institute)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, blank=True)
    middle_name = models.CharField(max_length=100, blank=True)
    department = models.ForeignKey(Department, null=True)

    def __str__(self):
        return self.last_name

    def full_name(self):
        return self.last_name


class Group(models.Model):
    name = models.CharField(max_length=15, unique=True)
    department = models.ForeignKey(Department)
    teachers = models.ManyToManyField(Teacher, null=True)

    def __str__(self):
        return self.name


class ResponseStudent(models.Model):
    badge_number = models.CharField(max_length=100)
    student_name = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group)

    def __str__(self):
        return self.badge_number


class Vote(models.Model):
    MARKS = (
    ('0','Выберите'),
    ('1','1 балл'),
    ('2','2 балла'),
    ('3','3 балла'),
    ('4','4 балла'),
    ('5','5 баллов'),
    )
    teacher = models.ForeignKey(Teacher, related_name='votes')
    mark1 = models.CharField(max_length=1, choices=MARKS, default='0')
    mark2 = models.CharField(max_length=1, choices=MARKS, default='0')
    mark3 = models.CharField(max_length=1, choices=MARKS, default='0')
    mark4 = models.CharField(max_length=1, choices=MARKS, default='0')
    mark5 = models.CharField(max_length=1, choices=MARKS, default='0')
    mark6 = models.CharField(max_length=1, choices=MARKS, default='0')
    mark7 = models.CharField(max_length=1, choices=MARKS, default='0')
    mark8 = models.CharField(max_length=1, choices=MARKS, default='0')
    response_student = models.ForeignKey(ResponseStudent, related_name='votes')

    def get_teacher_fullname(self):
        return 'XXXXXXXX'







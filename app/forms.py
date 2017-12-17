"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, Select
from django.utils.translation import ugettext_lazy as _

from app.models import Vote


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class BadgeForm(forms.Form):
    badge_number = forms.CharField(label='Номер бейджа', max_length=100)
    student_name = forms.CharField(max_length=200, label='ФИО')


class GroupForm(forms.Form):
    name = forms.CharField(label='Группа', max_length=100)


class VoteForm(ModelForm):
    t_full_name = forms.CharField(label='Учитель', max_length=100)

    class Meta:
        model = Vote
        exclude = ['response_student',]
        widgets = {
            'mark1': forms.Select(attrs={'class': 'form-control input-sm'}),
            'mark2': forms.Select(attrs={'class': 'form-control input-sm'}),
            'mark3': forms.Select(attrs={'class': 'form-control input-sm'}),
            'mark4': forms.Select(attrs={'class': 'form-control input-sm'}),
            'mark5': forms.Select(attrs={'class': 'form-control input-sm'}),
            'mark6': forms.Select(attrs={'class': 'form-control input-sm'}),
            'mark7': forms.Select(attrs={'class': 'form-control input-sm'}),
            'mark8': forms.Select(attrs={'class': 'form-control input-sm'}),
        }

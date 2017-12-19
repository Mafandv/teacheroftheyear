"""
Definition of urls for StudentsOpinion.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    #url(r'^$', app.views.home, name='home'),
    url(r'^$', app.views.poll, name='poll'),
    # url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^poll', app.views.poll, name='poll'),
    url(r'^badge', app.views.badge, name='badge'),
    url(r'^group_list', app.views.group_list, name='group_list'),
    url(r'^group', app.views.group, name='group'),
    url(r'^vote', app.views.vote, name='vote'),
    url(r'^import_data', app.views.import_data, name='import_data'),
    url(r'^export_xls', app.views.export_xls, name='export_xls'),

    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]

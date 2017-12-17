"""
Definition of views.
"""
from django.forms import formset_factory, modelformset_factory
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from datetime import datetime
import json
import xlrd

from django.template.loader import render_to_string

from app.forms import BadgeForm, GroupForm, VoteForm
from app.models import Group, Vote, ResponseStudent, Department, Teacher, Institute


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def poll(request):


    form = BadgeForm()
    return render(request, 'app/poll.html', { 'badge_form': form })


def badge(request):
    if request.method == 'POST':
        form = BadgeForm(request.POST)
        if form.is_valid():
            request.session['badge_number'] = form .cleaned_data['badge_number']
            request.session['student_name'] = form.cleaned_data['student_name']
            context = {
                'group_form': GroupForm()
            }
            data = {
                'success': True,
                'html': render_to_string('app/group.html', context, request)
            }
            return JsonResponse(data)

    data = {
        'success': False,
    }
    return JsonResponse(data)


def group_list(request):
    search = request.GET['search']
    data = []
    gr = Group.objects.all()
    for x in gr:
        if x.name.lower().find(search.lower()) != -1:
            data.append(x.name)

    # gr = Group.objects.filter(name__icontains=search)
    # data = [x.name for x in gr]
    s = json.dumps(data)
    print(s)

    return JsonResponse(s, safe=False)


def group(request):
    #VoteFormSet = modelformset_factory(Vote, exclude=('response',))
    VoteFormSet = formset_factory(VoteForm, extra=0)
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            gname = form.cleaned_data['name']
            tmp = Group.objects.filter(name=gname)
            if (tmp.count() > 0):
                g = tmp[0]
                request.session['group'] = g.pk
                l = []
                for t in g.teachers.all():
                    l.append({'teacher': t, 't_full_name': t.full_name()})
                context = {
                    'teacher_form': VoteFormSet(initial=l),
                }
                data = {
                    'success': True,
                    'html': render_to_string('app/teacher.html', context, request)
                }
                return JsonResponse(data)
    data = {
        'success': False,
    }
    return JsonResponse(data)


def vote(request):
    VoteFormSet = formset_factory(VoteForm, extra=0)
    if request.method == 'POST':
        formset = VoteFormSet(request.POST, request.FILES)
        if formset.is_valid():
            g = request.session.get('group')
            b = request.session.get('badge_number')
            n = request.session.get('student_name')

            if (g == None or b == None or n == None):
                return HttpResponseRedirect('/')

            print('valid')

            resp = ResponseStudent()
            resp.badge_number = b
            resp.student_name = n
            resp.group = Group.objects.filter(pk=g)[0]
            resp.save()
            for form in formset.cleaned_data:
                v = Vote()
                v.response_student = resp
                v.teacher = form['teacher']
                v.mark1 = form['mark1']
                v.mark2 = form['mark2']
                v.mark3 = form['mark3']
                v.mark4 = form['mark4']
                v.mark5 = form['mark5']
                v.mark6 = form['mark6']
                v.mark7 = form['mark7']
                v.mark8 = form['mark8']
                v.save()
        else:
            print('No valid')
    return render(
        request,
        'app/thank_you.html'
    )


def import_data(request):
    rb = xlrd.open_workbook('D:\pydata\prepod_goda.xlsx')
    sheet = rb.sheet_by_index(0)
    ins = Institute.objects.all()[0]
    n = sheet.nrows
    s = 'sdads'
    for rownum in range(sheet.nrows):
        row = sheet.row_values(rownum)
        d = row[0].strip()
        t = row[1].strip()
        g = row[2].strip()
        dep = Department()
        tech = Teacher()
        group = Group()

        db_d = Department.objects.filter(name=d)
        if (db_d.count() == 0):
            dep.name = d
            dep.institute = ins
            dep.save()
        else:
            dep = db_d[0]

        db_t = Teacher.objects.filter(last_name=t)
        if (db_t.count() == 0):
            tech.last_name = t
            tech.department = dep
            tech.save()
        else:
            tech = db_t[0]

        db_g = Group.objects.filter(name=g)
        if (db_g.count() == 0):
            group.name = g
            group.department = dep
            group.save()
        else:
            group = db_g[0]

        group.teachers.add(tech)
        group.save()

    return HttpResponse("OK " + s)

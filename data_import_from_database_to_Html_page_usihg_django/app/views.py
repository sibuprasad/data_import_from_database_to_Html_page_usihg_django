from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def Insert_Topic(request):
    tn = input('Enter topic_name: ')
    to = Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    return HttpResponse('Data is Inserted to Topic')

def Insert_Webpage(request):
    tn = input('Enter topic_name: ')
    to = Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input('Enter name: ')
    u=input('Enter Url: ')
    wo = Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    return HttpResponse('Data is Inserted to Webpage')

def Insert_AccessRecord(request):
    tn = input('Enter topic_name: ')
    to = Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input('Enter name: ')
    u=input('Enter Url: ')
    wo = Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    d = input('Enter date: ')
    a = input('Enter author: ')
    e = input('Enter email: ')
    ao = AccessRecord.objects.get_or_create(name=wo,date=d,author=a,email=e)[0]
    ao.save()
    return HttpResponse('Data is Inserted to AccessRecord')


def display_topics(request):
    qsto = Topic.objects.all()
    d = {'qsto':qsto}
    return render(request,'display_topics.html', d)

def display_webpage(request):
    qswo = Webpage.objects.all()
    d = {'qswo':qswo}
    return render(request,'display_webpage.html', d)

def display_acessrecords(request):
    qsao = AccessRecord.objects.all()
    d = {'qsao':qsao}
    return render(request,'display_acessrecords.html', d)
from django.shortcuts import render, redirect
from polls.models import Subject, Teacher, User
from django.http import JsonResponse, HttpRequest, HttpResponse
from polls.mappers import SubjectMapper

def subjects( request ):
    queryset = Subject.objects.all()
    subjects = []
    for x in queryset:
        subjects.append( SubjectMapper(x).as_dict() )
    
    return JsonResponse( subjects, safe=False )
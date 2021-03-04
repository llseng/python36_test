from django.shortcuts import render, redirect
from polls.models import Subject, Teacher, User
from django.http import JsonResponse, HttpRequest, HttpResponse, Http404
from polls.mappers import SubjectMapper
from polls.serializers import SubjectSerializer, SubjectSimpleSerializer, TeacherSerializer

import json, time
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django_redis import get_redis_connection

def subjects( request ):
    redis_cli = get_redis_connection()
    cache_key = 'vote:polls:subjects'
    data = redis_cli.get( cache_key )
    
    while not data: 
        if redis_cli.setnx( 'mutex', 'x', ex=10 ):

            queryset = Subject.objects.all()
            subjects = []
            for x in queryset:
                subjects.append( SubjectMapper(x).as_dict() )
            data = json.dumps( subjects )
            redis_cli.set( cache_key,  data, ex=60 )

            redis_cli.delete( 'mutex' )
        else:
            time.sleep( 0.1 )
            data = redis_cli.get( cache_key )

    res = json.loads( data )
    
    return JsonResponse( res, safe=False )

@api_view( ('GET',) )
@cache_page( timeout= 60, cache= 'default' )
def show_subjects( request: HttpRequest ) -> HttpResponse:
    subjects = Subject.objects.all().order_by( 'no' )
    # 创建序列化器对象并指定要序列化的模型
    serializer = SubjectSerializer( subjects, many=True )
    # 通过序列化器的data 属性获得模型对应的字典并通过创建Response对象返回JSON格式的数据
    return Response( serializer.data )

@api_view( ('GET', ) )
@cache_page( timeout= 60, cache= 'default' )
def show_teachers( request: HttpRequest ) -> HttpResponse:
    try:
        sno = int( request.GET.get( 'sno' ) )
        subject = Subject.objects.only( 'name' ).get( no=sno )
        teachers = Teacher.objects.filter( sno=subject ).defer( 'sno' ).order_by( 'no' )
        subject_seri = SubjectSimpleSerializer( subject )
        teacher_seri = TeacherSerializer( teachers, many=True )
        return Response( {'subject':subject_seri.data, 'teachers': teacher_seri.data} )
    except (TypeError, ValueError, Subject.DoesNotExist ):
        return Response( status=404 )

@method_decorator(decorator=cache_page(timeout=60, cache='default'), name='get' )
class SubjectView( ListAPIView ):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectViewSet( ModelViewSet ):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

@method_decorator(decorator=cache_page(timeout=60, cache='default'), name='get' )
class TeacherView( ListAPIView ):
    serializer_class = TeacherSerializer

    def get_queryset(self):
        queryset = Teacher.objects.defer( 'sno' )
        try:
            sno = self.request.GET.get( 'sno', '' )
            queryset = queryset.filter( sno__no=sno )
            return queryset
        except ValueError:
            raise Http404( "No teachers found." )

from django.shortcuts import render, redirect
from polls.models import Subject, Teacher, User
from django.http import JsonResponse, HttpRequest, HttpResponse
from polls.mappers import SubjectMapper
from polls.serializers import SubjectSerializer, SubjectSimpleSerializer, TeacherSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

def subjects( request ):
    queryset = Subject.objects.all()
    subjects = []
    for x in queryset:
        subjects.append( SubjectMapper(x).as_dict() )
    
    return JsonResponse( subjects, safe=False )

@api_view( ('GET',) )
def show_subjects( request: HttpRequest ) -> HttpResponse:
    subjects = Subject.objects.all().order_by( 'no' )
    # 创建序列化器对象并指定要序列化的模型
    serializer = SubjectSerializer( subjects, many=True )
    # 通过序列化器的data 属性获得模型对应的字典并通过创建Response对象返回JSON格式的数据
    return Response( serializer.data )

@api_view( ('GET', ) )
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
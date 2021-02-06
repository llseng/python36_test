from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpRequest, HttpResponse

# Create your views here.
from polls.models import Subject, Teacher, User
from polls.utils import gen_random_code, Captcha, gen_md5_digest

def show_subjects( request ):
    subjects = Subject.objects.all().order_by('no')
    return render( request, 'subjects.html', {'subjects': subjects} )

def show_teachers( request ):
    try:
        # if not request.session.get('userid', None):
        #     return redirect( '/' )

        sno = int( request.GET.get( 'sno' ) )
        teachers = []
        if sno:
            subject = Subject.objects.only( 'name' ).get( no=sno )
            teachers = Teacher.objects.filter( sno=subject ).order_by( 'no' )
        
        return render( request, 'teachers.html', {
            'subject': subject,
            'teachers': teachers
        } )
    except (ValueError, Subject.DoesNotExist):
        return redirect( '/' )

def praise_or_criticize( request ):
    try:
        if request.session.get('userid', None):
            tno = int( request.GET.get( 'tno' ) )
            teacher = Teacher.objects.get( no=tno )
            if request.path.startswith( '/praise' ):
                teacher.good_count += 1
                count = teacher.good_count
            else:
                teacher.bad_count += 1
                count = teacher.bad_count
                
            teacher.save()
            data = {'code': 20000, 'mesg': '操作成功', 'count': count}
        else:
            data = {'code': 20002, 'mesg': '请登录'}
    except (ValueError, Teacher.DoesNotExist ):
        data = {'code': 20001, 'mesg': '操作失败'}
    
    return JsonResponse( data )

def login( request: HttpRequest ) -> HttpResponse:
    hint = ''
    if request.method == 'POST':

        for x in range(1):

            req_captcha = request.POST.get( 'captcha' )
            captcha = request.session.get('captcha', None)
            if not req_captcha or not captcha or req_captcha.lower() != captcha.lower():
                hint = '验证码错误'
                continue

            username = request.POST.get( 'username' )
            password = request.POST.get( 'password' )
            
            if not username or not password:
                hint = '用户或密码错误'
                continue
                
            password = gen_md5_digest( password )
            user = User.objects.filter( username = username, password = password).first()

            if not user:
                hint = '请输入有效的用户名和密码'
                continue
            
            request.session['userid'] = user.no
            request.session['username'] = user.username
            return redirect( '/' )

    return render( request, 'login.html', {'hint': hint} )

def get_captcha(request: HttpRequest) -> HttpResponse:
    """验证码"""
    captcha_text = gen_random_code()
    request.session['captcha'] = captcha_text
    image_data = Captcha.instance().generate(captcha_text)
    return HttpResponse(image_data, content_type='image/png')

def logout( request ):
    '''注销'''
    request.session.flush()
    return redirect( '/' )

def test( request ):
    if request.session.test_cookie_worked():
        return JsonResponse( {} )
    else:
        print(request.COOKIES, request.session, request.session.keys(), request.session.values() )
        return HttpResponse( "Please enable cookies and try again." )
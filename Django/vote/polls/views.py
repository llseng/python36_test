from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpRequest, HttpResponse

# Create your views here.
from polls.models import Subject, Teacher, User
from polls.utils import gen_random_code, Captcha, gen_md5_digest

import xlwt, io
from urllib.parse import quote

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
        # if request.session.get('userid', None):
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
        # else:
        #     data = {'code': 20002, 'mesg': '请登录'}
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

def export_teachers_excel( request ):
    # 创建工作簿
    wb = xlwt.Workbook()
    # 添加工作表
    sheet = wb.add_sheet( '老师信息表' )
    # 查询所有老师的信息
    queryset = Teacher.objects.all().select_related( 'sno' )
    # 向excel表单中写入表头
    colnames = ('姓名', '介绍', '好评数', '差评数', '学科')
    for index, name in enumerate( colnames ):
        sheet.write( 0, index, name )
    # 向单元格中写入老师的数据
    props = ('name', 'intro', 'good_count', 'bad_count', 'sno' )
    for row, teacher in enumerate( queryset ):
        for col, prop in enumerate( props ):
            value = getattr( teacher, prop, '' )
            if isinstance( value, Subject ):
                value = value.name
            sheet.write( row + 1, col, value )
    
    # 保存Excel
    buffer = io.BytesIO()
    wb.save( buffer )
    # 将二进制数据写入响应的消息体中并设置MIME类型
    resp = HttpResponse( buffer.getvalue(), content_type='application/vnd.ms-excel' )
    # 中文文件名需要处理成百分号编码
    filename = quote( '老师.xls' )
    # 通过响应头告知浏览器下载该文件的文件名
    resp['content-disposition'] = f'attachment: filename*=utf-8''{filename}'
    return resp


def test( request ):
    if request.session.test_cookie_worked():
        return JsonResponse( {} )
    else:
        print(request.COOKIES, request.session, request.session.keys(), request.session.values() )
        return HttpResponse( "Please enable cookies and try again." )
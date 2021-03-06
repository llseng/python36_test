"""vote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from polls.views import show_subjects, show_teachers, praise_or_criticize, login, logout, get_captcha, test, export_teachers_excel
import polls.apis as polls_apis

from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('admin/', admin.site.urls),

    path( '', show_subjects ),
    path( 'teachers/', show_teachers ),
    path( 'praise/', praise_or_criticize ),
    path( 'criticize/', praise_or_criticize ),
    path( 'login/', login ),
    path( 'logout/', logout ),
    path( 'captcha/', get_captcha ),

    path( 'test/', test ),

    path('excel/', export_teachers_excel),

    path( 'api/subjects/', polls_apis.subjects ),
    path( 'api/show_subjects/', polls_apis.show_subjects ),
    path( 'api/show_teachers/', polls_apis.show_teachers ),
    path( 'api/show_subjects2/', polls_apis.SubjectView.as_view() ),
    path( 'api/show_teachers2/', polls_apis.TeacherView.as_view() ),
]

router = DefaultRouter()
router.register( 'api/show_subjects3', polls_apis.SubjectViewSet )

urlpatterns += router.urls
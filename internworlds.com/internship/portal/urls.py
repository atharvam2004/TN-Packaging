"""internship URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('', views.homepage, name='index'),
                  path('our_team/', views.teampage, name='our_team'),
                  path('faq/', views.faqpage, name='faq'),

                  path('makeresume/', views.resumedata, name='makeresume'),

                  path('resumetemp/', views.resumetemp, name='resumetemp'),

                  path('index/', views.homepage, name='index'),
                  path('about/', views.aboutpage, name='about'),
                  path('usersignup/', views.signup, name='usersignup'),
                  path('companysignup/', views.companysignup, name='companysignup'),
                  path('signup/', views.signup, name='usersignup'),
                  path('login/', views.loginpage, name='login'),
                  path('userdashboard/', views.userdashboardpage, name='userdashboard'),
                  path('getint_tit/',views.getint_tit,name="getint_tit"),
                  path('getint_type/',views.getint_type,name="getint_type"),
                  path('getloc/',views.getloc,name="getloc"),
                  path('company_main_registration/', views.company_registration_mainpage,name='company_main_registration'),
                  path('companylogout/', views.companylogout, name='companylogout'),
                  path('contact/', views.contactinfo, name='contact'),
                  path('company/', views.companypage, name='company'),
                  path('company_profile/', views.companyprofile_save, name='company_profile'),
                  path('companylogin/', views.companyloginpage, name='companylogin'),
                  path('add_job/', views.addjobform, name='add_job'),
                  path('add_internship/', views.addineternshipform, name='add_internship'),
                  path('company_profile/', views.companyprofile_save, name='company_profile'),
                  path('company_profile_view/', views.company_profile_view, name='company_profile_view'),
path('view_internship/', views.viewInternship, name='view_internship'),
path('view_internship_detail/<int:id>', views.view_internship_detail, name='view_internship_detail'),
path('show_internship_detail/<int:id>', views.show_internship_detail, name='show_internship_detail'),
path('show_job_detail/<int:id>', views.show_job_detail, name='show_job_detail'),
                  path('job/', views.show_job, name='job'),

                  path('delete/<int:id>/',views.delete_internship,name='delete_internship'),
path('update_internship<int:id>/',views.update_internship,name='update_internship'),
path('view_job_details/<int:id>', views.view_job_detail, name='view_job_details'),
path('view_job/',views.viewJob,name='view_job'),
path('delete_job/<int:id>/',views.delete_job,name='delete_job'),
path('update/<int:id>/',views.update_job,name='update_job'),

                  path('logout/', views.userlogout, name='logout'),
                  path('profile/', views.profile, name='profile'),
path('show_internship/', views.show_internship, name='show_internship'),

path('view_internship/', views.viewInternship, name='view_internship'),
path('view_internship_detail/<int:id>', views.view_internship_detail, name='view_internship_detail'),
path('show_internship_detail/<int:id>', views.show_internship_detail, name='show_internship_detail'),
path('show_job_detail/<int:id>', views.show_job_detail, name='show_job_detail'),
                  path('job/', views.show_job, name='job'),
                  path('job/search',views.search,name='job_search'),
                  path('job/search_location', views.search_location, name='job_search_location'),

                  path('internship/search', views.search_internship, name='internship_search'),
                  path('internship/search_internship_location', views.searchinternshiplocation, name='internship_search_location'),
                  path('applicationform/', views.internship, name='Application_Form'),
path('userdashboardprofile',views.userdashboardprofile,name='userdashboardprofile'),
                  path('userresumes', views.userresume, name='userresume'),
                  path('user_job/', views.userjob, name='user_job'),
                  path('user_internship/', views.userinternship, name='user_internship'),
path('userjobdetail/<int:id>', views.user_show_job_detail, name='userjobdetail'),
                  path('userinternshipdetail/<int:id>', views.user_show_internship_detail, name='userinternshipdetail'),
path('job/design', views.show_job_design, name='job_design'),
path('job/graphics', views.show_job_graphics, name='job_graphics'),
path('job/market', views.show_job_market, name='job_market'),
path('job/software', views.show_job_software, name='job_software'),
path('job/java', views.show_job_java, name='job_java'),
path('job/python', views.show_job_python, name='job_python'),
path('job/web', views.show_job_web, name='job_web'),
path('job/cother', views.show_job_cother, name='job_cother'),
path('job/delhi', views.show_job_delhi, name='job_delhi'),
path('job/mumbai', views.show_job_mumbai, name='job_mumbai'),
path('job/pune', views.show_job_pune, name='job_pune'),

path('job/hyderbad', views.show_job_hyderbad, name='job_hyderbad'),
path('job/bangalore', views.show_job_bangalore, name='job_bangalore'),
path('job/chennai', views.show_job_chennai, name='job_chennai'),
path('job/kolkata', views.show_job_kolkata, name='job_kolkata'),
path('job/agra', views.show_job_agra, name='job_agra'),
path('job/pune', views.show_job_pune, name='job_pune'),
path('job/other', views.show_job_other, name='job_other'),

path('internship/design', views.show_internship_design, name='internship_design'),
path('internship/graphics', views.show_internship_graphics, name='internship_graphics'),
path('internship/market', views.show_internship_market, name='internship_market'),
path('internship/software', views.show_internship_software, name='internship_software'),
path('internship/java', views.show_internship_java, name='internship_java'),
path('internship/python', views.show_internship_python, name='internship_python'),
path('internship/web', views.show_internship_web, name='internship_web'),
path('internship/cother', views.show_internship_cother, name='internship_cother'),
path('internship/delhi', views.show_internship_delhi, name='internship_delhi'),
path('internship/mumbai', views.show_internship_mumbai, name='internship_mumbai'),
path('internship/pune', views.show_internship_pune, name='internship_pune'),

path('internship/hyderbad', views.show_internship_hyderbad, name='internship_hyderbad'),
path('internship/bangalore', views.show_internship_bangalore, name='internship_bangalore'),
path('internship/chennai', views.show_internship_chennai, name='internship_chennai'),
path('internship/kolkata', views.show_internship_kolkata, name='internship_kolkata'),
path('internship/agra', views.show_internship_agra, name='internship_agra'),
path('internship/pune', views.show_internship_pune, name='internship_pune'),
path('internship/other', views.show_internship_other, name='internship_other'),
path('add_blogs/', views.addblogpage, name='add_blogs'),
path('view_add_blogs/', views.viewaddblog, name='view_add_blogs'),
path('view_add_blog_detail/<int:id>', views.view_add_blog_detail, name='view_add_blog_detail'),
path('delete_blog/<int:id>/',views.delete_blog,name='delete_blog'),
path('update_blog/<int:id>/',views.update_blog,name='update_blog'),
path('blog_page/',views.userblog,name='blog_page'),
path('job/full_time_job', views.show_job_full_time_job, name='full_time_job'),
path('job/part_time_job', views.show_job_part_time_job, name='part_time_job'),
path('internship/full_time_internship', views.show_internship_full_time_internship, name='full_time_internship'),
path('internship/part_time_internship', views.show_internship_part_time_internship, name='part_time_internship'),
path('internship/part_time_internship', views.show_internship_part_time_internship, name='part_time_internship'),
path('blog_page_info/<int:id>', views.userblogdetail, name='blog_page_info'),
                  path('applydata/<int:id>', views.applyformdata, name='applydata'),
                  path('form_apply', views.form_apply, name='form_apply'),
                  path('internshipapplydata/<int:id>', views.applyinternshipformdata, name='internshipapplydata'),
                  path('internship_form_apply', views.internship_form_apply, name='internship_form_apply'),
                  path('internship_resumes', views.internship_resumes, name='internship_resume'),
                  path('internship_resume_detail/<int:id>', views.internship_resumesdetails,
                       name='internship_resume_detail'),
                  path('internship_delete_resume/<int:id>', views.internship_delete_resume,
                       name='internship_delete_resume'),
path('resumedetails/<int:id>', views.resumesdetails, name='resumedetails'),
path('resumes', views.resumes, name='resumes'),
path('userresumes', views.userresume, name='userresume'),
path('delete_resume/<int:id>', views.delete_resume, name='delete_resume'),
                  # profile update
                  path('user_profile_update', views.user_profile_update, name='user_profile_update'),
                  path('company_profile_update/', views.company_profile_update, name='company_profile_update'),
                  # change password
                  path('user_change_password', views.user_change_password, name='user_change_password'),
                  path('company_change_password', views.company_change_password, name='company_change_password'),
                  path('job/searches', views.search1, name='job_searches'),
                  path('job/search_locations', views.search_location1, name='job_search_locations'),
                  path('internship/searches', views.search_internship1, name='internship_searches'),
                  path('internship/search_internship_locations', views.searchinternshiplocation1,
                       name='internship_search_locations'),
                  path('associate', views.associatepage, name='associate'),
                  path('associate_form', views.associateformpage, name='associate_form'),
                  path('testimonial_form', views.testimonialinfo, name='testimonial_form'),
                  path('forgot_password', views.forgot, name='forgot_password'),
                  path('companyforgetpassword', views.company_forgot, name='companyforgetpassword'),
                  path('new_password',views.new_password,name='new_password'),
                  path('company_new_password', views.company_new_password, name='company_new_password'),
   
              ]\
              +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
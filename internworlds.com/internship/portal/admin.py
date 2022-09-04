from profile import Profile

from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import  our_team,Blog, resume,Associate,Testimonial,Company_Registration, job_application_form,internship_application_form,\
    company_profile,add_internship,add_job,Customer,internform
class testimonialadmin(admin.ModelAdmin):
    list_filter=('id','user_name')
    search_fields = ['user_name']
    list_display = ['id','user_name','location',
                    'review','uploads']

#blog
class blogadmin(admin.ModelAdmin):
    list_filter=('id','title')
    search_fields = ['title']
    list_display = ['id','company_name',
                    'email_address','title',
                    'sub_title','description','location','uploads']
#add courses
# Register your models here.
class associateadmin(admin.ModelAdmin):
    list_filter=('id','company_name')
    search_fields = ['company_name']

    list_display = ['fname','lname','email',
                   'company_name',
                    'address','state','country','website_url','about_company','company_size']

class companyprofileadmin(admin.ModelAdmin):
    list_filter=('id','organization_name')
    search_fields = ['organization_name']
    exclude = ['password']
    list_display = ['username','email','organization_name',
                   'organization_description','organization_logo','phone','address','organization_website']
#add courses
class customeradmin(admin.ModelAdmin):
    list_display =('id','first_name','email','phone',
                   'city')
    exclude = ['password']
    search_fields = ['first_name']
    list_filter = ['first_name']











class add_jobs_admin(admin.ModelAdmin):
    search_fields = ['job_type']
    list_filter = ['job_type','job_title']
    list_display = ('id','company_name','email_address','job_type',
                    'job_title','required_skill','experience_requirements',
                    'job_description'
                    ,'responsibilities','required_qualification',
                    'about_company','stipend','no_of_positions',
                    'application_deadline','work_mode','location')
class add_internships_admin(admin.ModelAdmin):
    search_fields = ['internship_type']
    list_filter = ['internship_type','internship_title']
    list_display = ('id','company_name','email_address',
                    'internship_type','internship_title','required_skill',
                    'experience_requirements','internship_description'
                    ,'responsibilities','required_qualification',
                    'about_company','stipend','no_of_positions',
                    'application_deadline','work_mode','location')

class applicationform_admin(admin.ModelAdmin):
    list_display = ("company_name","company_email","field",
                    "fname",
                    "lname", "email", "phone", "city",
                    "hometown", "secondary_class", "secondary_year",
                    "secondary_percentage", "seniorsecondary", "seniorsecondary_year",
                    "seniorecondary_percentage", "Diploma_field",
                    "Diploma_college", "Diploma_year", "Diploma_percentage",

                    "graduation_field", "graduation_college", "graduation_year",
                    "grad_percentage",

                    "post_graduation_field", "post_graduation_college", "post_graduation_year",
                    "post_graduation_percentage", "Phd_field", "Phd_college",
                    "Phd_year", "Phd_percentage",

                    "Job_company_name", "Job_location",
                    "Job_designation", "Job_joining_date", "Job_relieving_date",

                    "Internships_company_name", "Internships_location",
                    "Internship_designation", "Internships_joining_date", "Internships_relieving_date",

                    "Positions_Responsibility", "trainings_field",
                    "trainings_location", "trainings_joining_date", "trainings_relieving_date",

                    "personal_projects_topic", "personal_projects_description",

                    "skills", "blog_link", "gitHub_profile",
                    "play_store_link",
                    "behance_portfolio",
                    "other_work_sample"
                    )

    search_fields = ['fname']
    list_filter = ['fname']

class internship_applicationform_admin(admin.ModelAdmin):
    list_display = ("company_name", "company_email", "field",
                    "fname",
                    "lname", "email", "phone", "city",
                    "hometown", "secondary_class", "secondary_year",
                    "secondary_percentage", "seniorsecondary", "seniorsecondary_year",
                    "seniorecondary_percentage", "Diploma_field",
                    "Diploma_college", "Diploma_year", "Diploma_percentage",

                    "graduation_field", "graduation_college", "graduation_year",
                    "grad_percentage",

                    "post_graduation_field", "post_graduation_college", "post_graduation_year",
                    "post_graduation_percentage", "Phd_field", "Phd_college",
                    "Phd_year", "Phd_percentage",

                    "Job_company_name", "Job_location",
                    "Job_designation", "Job_joining_date", "Job_relieving_date",

                    "Internships_company_name", "Internships_location",
                    "Internship_designation", "Internships_joining_date", "Internships_relieving_date",

                    "Positions_Responsibility", "trainings_field",
                    "trainings_location", "trainings_joining_date", "trainings_relieving_date",

                    "personal_projects_topic", "personal_projects_description",

                    "skills", "blog_link", "gitHub_profile",
                    "play_store_link",
                    "behance_portfolio",
                    "other_work_sample"
                    )

    search_fields = ['fname']
    list_filter = ['fname']
class add_team_admin(admin.ModelAdmin):
    search_fields = ['user_name']
    list_filter = ['user_name']
    list_display = ('id','user_name','designation',
                    'review','linkedin_account','uploads')

admin.site.register(job_application_form,applicationform_admin)
admin.site.register(internship_application_form,internship_applicationform_admin)

admin.site.register(Customer,customeradmin)
admin.site.register(company_profile,companyprofileadmin)
admin.site.register(add_job,add_jobs_admin)
admin.site.register(add_internship,add_internships_admin)
admin.site.register(Blog,blogadmin)
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Testimonial,testimonialadmin)
admin.site.register(Associate,associateadmin)
admin.site.register(our_team,add_team_admin)

admin.site.register(resume)
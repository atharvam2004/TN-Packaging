


from django.forms import forms, ModelForm

from .models import Customer
from .models.customers import contact, add_job, add_internship, company_profile, Company_Query_Form, \
    Company_Registration, internform, Blog, job_application_form, internship_application_form, \
    job_application_form


class registerforms(ModelForm):
    class Meta:
        model=Customer
        fields=["first_name","email","password","phone","city"]
    def clean(self):
        email = self.cleaned_data.get('email')
        if Customer.objects.filter(email=email).exists():
            raise forms.ValidationError("Email exists")
        return self.cleaned_data

class companyregisterforms(ModelForm):
    class Meta:
        model=Company_Registration
        fields=["username","email","password","phone","city"]


class internshipformdetail(ModelForm):
    class Meta:
        model=internform
        fields=[
                    "fname",
                    "lname","email","phone","city",
                       "hometown","secondary_class" ,"secondary_year",
        "secondary_percentage" , "seniorsecondary" ,"seniorsecondary_year" ,
        "seniorecondary_percentage" ,"Diploma_field" ,
        "Diploma_college","Diploma_year" ,"Diploma_percentage" ,

        "graduation_field" ,"graduation_college" ,"graduation_year",
                   "gradpercentage" ,

        "post_graduation_field", "post_graduation_college","post_graduation_year" ,
        "post_graduation_percentage" ,"Phd_field","Phd_college",
        "Phd_year","Phd_percentage",

        "Job_company_name", "Job_location" ,
        "Job_designation" ,"Job_joining_date" ,"Job_relieving_date" ,

        "Internships_company_name","Internships_location" ,
        "Internship_designation" ,"Internships_joining_date" ,"Internships_relieving_date" ,

       "Positions_Responsibility" ,"trainings_field",
        "trainings_location","trainings_joining_date","trainings_relieving_date",

        "personal_projects_topic", "personal_projects_description",

        "skills","blog_link","gitHub_profile",
        "play_store_link" ,
        "behance_portfolio" ,
        "other_work_sample"],


class conatctforms(ModelForm):
    class Meta:
        model=contact
        fields=["user_name",
                "email","subject","message"]

class add_job_forms(ModelForm):
    class Meta:
        model=add_job
        fields=['company_name','email_address','job_type','job_title','required_skill','experience_requirements','job_description'
                    ,'responsibilities','required_qualification']


class add_internship_forms(ModelForm):
    class Meta:
        model=add_internship
        fields=['company_name','email_address','job_type','job_title','required_skill','experience_requirements','job_description'
                    ,'responsibilities','required_qualification']
class organization_profile_forms(ModelForm):
    class Meta:
        model=company_profile
        fields=[ 'username','email','password',
                 'organization_name','organization_description',
                 'organization_logo','phone','address','organization_website']



class internshipformdetail(ModelForm):
    class Meta:
        model=internform
        fields=['job_type','job_title','required_skill','experience_requirements','job_description'
                    ,'responsibilities','required_qualification','about_company','stipend','no_of_positions',
                    'application_deadline','work_mode','location']

class conatctforms(ModelForm):
    class Meta:
        model=Company_Query_Form
        fields=["comapny_name","comapny_email","user_name",
                "email","subject","message"]

class add_jobs_forms(ModelForm):
    class Meta:
        model=add_job
        fields=['company_name','email_address','job_type','job_title','required_skill','experience_requirements','job_description'
                    ,'responsibilities','required_qualification','about_company','stipend','no_of_positions',
                    'application_deadline','work_mode','location']


class add_internships_forms(ModelForm):
    class Meta:
        model=add_internship
        fields=['company_name','email_address','internship_type',
                'internship_title','required_skill',
                'experience_requirements','internship_description'
                    ,'responsibilities','required_qualification','about_company','stipend','no_of_positions',
                    'application_deadline','work_mode','location']



class add_blogs(ModelForm):
    class Meta:
        model=Blog
        fields=['company_name','email_address',
                'title','sub_title',
                'description'
                    ,'uploads']


class application_formdetail(ModelForm):
    class Meta:
        model=job_application_form
        fields=["company_name","company_email","field",
                    "fname",
                    "lname", "email", "phone", "city",
                    "hometown", "secondary_class", "secondary_year",
                    "secondary_percentage", "seniorsecondary", "seniorsecondary_year",
                    "seniorecondary_percentage", "Diploma_field",
                    "Diploma_college", "Diploma_year", "Diploma_percentage",

                    "graduation_field", "graduation_college", "graduation_year",
                    "gradpercentage",

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
                    "other_work_sample"]
class internship_application_formdetail(ModelForm):
    class Meta:
        model=internship_application_form

    fields = ["company_name", "company_email", "field",
              "fname",
              "lname", "email", "phone", "city",
              "hometown", "secondary_class", "secondary_year",
              "secondary_percentage", "seniorsecondary", "seniorsecondary_year",
              "seniorecondary_percentage", "Diploma_field",
              "Diploma_college", "Diploma_year", "Diploma_percentage",

              "graduation_field", "graduation_college", "graduation_year",
              "gradpercentage",

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
              "other_work_sample"]
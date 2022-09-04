from django.db import models



class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    password =models.CharField(max_length=8)
    phone=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
  

    def __str__(self):
        return self.first_name


class contact(models.Model):
    user_name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField(max_length=500)



class company_profile(models.Model):
    username=models.CharField(max_length=500)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    organization_name=models.CharField(max_length=255)
    organization_description=models.TextField(max_length=1000)
    organization_logo=models.ImageField(upload_to='media/')
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    organization_website=models.URLField()
    






class Company_Registration(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=8)
    phone=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

class add_job(models.Model):
    company_name=models.CharField(max_length=100)
    email_address=models.EmailField()
    job_type=models.CharField(max_length=100)
    job_title=models.CharField(max_length=100)
    required_skill=models.CharField(max_length=1000)
    experience_requirements=models.CharField(max_length=1000)
    job_description=models.CharField(max_length=1000)
    responsibilities=models.CharField(max_length=700)
    required_qualification=models.CharField(max_length=500)
    about_company=models.CharField(max_length=1000)
    stipend=models.CharField(max_length=200)
    no_of_positions=models.CharField(max_length=100)
    application_deadline=models.CharField(max_length=50)
    work_mode=models.CharField(max_length=50)
    location=models.CharField(max_length=50)


class add_internship(models.Model):
    company_name=models.CharField(max_length=100)
    email_address=models.EmailField()
    internship_type=models.CharField(max_length=100)
    internship_title=models.CharField(max_length=100)
    required_skill=models.CharField(max_length=1000)
    experience_requirements=models.CharField(max_length=500)
    internship_description=models.CharField(max_length=1000)
    responsibilities=models.CharField(max_length=700)
    required_qualification=models.CharField(max_length=500)
    about_company=models.CharField(max_length=1000)
    stipend=models.CharField(max_length=100)
    no_of_positions=models.CharField(max_length=50)
    application_deadline=models.CharField(max_length=50)
    work_mode=models.CharField(max_length=50)
    location=models.CharField(max_length=100)

class Blog(models.Model):
    company_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    location = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    sub_title = models.CharField(max_length=200)
    description = models.CharField(max_length=3000)
    uploads = models.ImageField(upload_to='blog_media/',
                                          max_length=100)

class internform(models.Model):


    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    email=models.EmailField(max_length=50)

    phone=models.CharField(max_length=10)

    city=models.CharField(max_length=20)
    hometown=models.CharField(max_length=60)


    secondary_class=models.CharField(max_length=10)
    secondary_year=models.CharField(max_length=10)
    secondary_percentage=models.CharField(max_length=10)
    seniorsecondary = models.CharField(max_length=50)
    seniorsecondary_year=models.CharField(max_length=10)
    seniorecondary_percentage=models.CharField(max_length=10)

    Diploma_field=models.CharField(max_length=20)
    Diploma_college=models.CharField(max_length=50)
    Diploma_year=models.CharField(max_length=20)
    Diploma_percentage=models.CharField(max_length=20)

    graduation_field=models.CharField(max_length=20)
    graduation_college = models.CharField(max_length=50)
    graduation_year = models.CharField(max_length=20)
    grad_percentage = models.CharField(max_length=20)


    post_graduation_field=models.CharField(max_length=20)
    post_graduation_college = models.CharField(max_length=50)
    post_graduation_year = models.CharField(max_length=20)
    post_graduation_percentage = models.CharField(max_length=20)

    Phd_field=models.CharField(max_length=20)
    Phd_college = models.CharField(max_length=50)
    Phd_year = models.CharField(max_length=20)
    Phd_percentage = models.CharField(max_length=20)


    Job_company_name = models.CharField(max_length=50)

    Job_location = models.CharField(max_length=20)
    Job_designation = models.CharField(max_length=50)
    Job_joining_date = models.CharField(max_length=10)
    Job_relieving_date = models.CharField(max_length=10)



    Internships_company_name = models.CharField(max_length=50)

    Internships_location = models.CharField(max_length=20)
    Internship_designation = models.CharField(max_length=50)
    Internships_joining_date = models.CharField(max_length=10)
    Internships_relieving_date = models.CharField(max_length=10)

    Positions_Responsibility = models.CharField(max_length=50)

    trainings_field = models.CharField(max_length=50)
    trainings_location = models.CharField(max_length=20)
    trainings_joining_date = models.CharField(max_length=10)
    trainings_relieving_date = models.CharField(max_length=10)

    personal_projects_topic= models.CharField(max_length=50)
    personal_projects_description= models.CharField(max_length=100)

    skills = models.CharField(max_length=100)

    blog_link = models.CharField(max_length=20)
    gitHub_profile = models.CharField(max_length=20)
    play_store_link = models.CharField(max_length=20)
    behance_portfolio = models.CharField(max_length=20)
    other_work_sample = models.CharField(max_length=20)

class job_application_form(models.Model):
    company_name = models.CharField(max_length=100)
    company_email = models.EmailField()
    field = models.CharField(max_length=100)

    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)

    phone=models.CharField(max_length=10)

    city=models.CharField(max_length=100)
    hometown=models.CharField(max_length=100)


    secondary_class=models.CharField(max_length=100)
    secondary_year=models.CharField(max_length=100)
    secondary_percentage=models.CharField(max_length=100)
    seniorsecondary = models.CharField(max_length=100)
    seniorsecondary_year=models.CharField(max_length=100)
    seniorecondary_percentage=models.CharField(max_length=100)

    Diploma_field=models.CharField(max_length=100)
    Diploma_college=models.CharField(max_length=100)
    Diploma_year=models.CharField(max_length=100)
    Diploma_percentage=models.CharField(max_length=100)

    graduation_field=models.CharField(max_length=100)
    graduation_college = models.CharField(max_length=100)
    graduation_year = models.CharField(max_length=100)
    grad_percentage = models.CharField(max_length=100)


    post_graduation_field=models.CharField(max_length=100)
    post_graduation_college = models.CharField(max_length=100)
    post_graduation_year = models.CharField(max_length=100)
    post_graduation_percentage = models.CharField(max_length=100)

    Phd_field=models.CharField(max_length=100)
    Phd_college = models.CharField(max_length=100)
    Phd_year = models.CharField(max_length=100)
    Phd_percentage = models.CharField(max_length=100)


    Job_company_name = models.CharField(max_length=100)

    Job_location = models.CharField(max_length=100)
    Job_designation = models.CharField(max_length=100)
    Job_joining_date = models.CharField(max_length=100)
    Job_relieving_date = models.CharField(max_length=100)



    Internships_company_name = models.CharField(max_length=100)

    Internships_location = models.CharField(max_length=100)
    Internship_designation = models.CharField(max_length=100)
    Internships_joining_date = models.CharField(max_length=100)
    Internships_relieving_date = models.CharField(max_length=100)

    Positions_Responsibility = models.CharField(max_length=100)

    trainings_field = models.CharField(max_length=100)
    trainings_location = models.CharField(max_length=100)
    trainings_joining_date = models.CharField(max_length=100)
    trainings_relieving_date = models.CharField(max_length=100)

    personal_projects_topic= models.CharField(max_length=100)
    personal_projects_description= models.CharField(max_length=100)

    skills = models.CharField(max_length=100)
    blog_link = models.CharField(max_length=100)

    gitHub_profile = models.CharField(max_length=100)
    play_store_link = models.CharField(max_length=100)
    behance_portfolio = models.CharField(max_length=100)
    other_work_sample = models.CharField(max_length=100)
class internship_application_form(models.Model):
    company_name = models.CharField(max_length=100)
    company_email = models.EmailField()
    field = models.CharField(max_length=100)

    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)

    phone=models.CharField(max_length=10)

    city=models.CharField(max_length=100)
    hometown=models.CharField(max_length=100)


    secondary_class=models.CharField(max_length=100)
    secondary_year=models.CharField(max_length=100)
    secondary_percentage=models.CharField(max_length=100)
    seniorsecondary = models.CharField(max_length=100)
    seniorsecondary_year=models.CharField(max_length=100)
    seniorecondary_percentage=models.CharField(max_length=100)

    Diploma_field=models.CharField(max_length=100)
    Diploma_college=models.CharField(max_length=100)
    Diploma_year=models.CharField(max_length=100)
    Diploma_percentage=models.CharField(max_length=100)

    graduation_field=models.CharField(max_length=100)
    graduation_college = models.CharField(max_length=100)
    graduation_year = models.CharField(max_length=100)
    grad_percentage = models.CharField(max_length=100)


    post_graduation_field=models.CharField(max_length=100)
    post_graduation_college = models.CharField(max_length=100)
    post_graduation_year = models.CharField(max_length=100)
    post_graduation_percentage = models.CharField(max_length=100)

    Phd_field=models.CharField(max_length=100)
    Phd_college = models.CharField(max_length=100)
    Phd_year = models.CharField(max_length=100)
    Phd_percentage = models.CharField(max_length=100)


    Job_company_name = models.CharField(max_length=100)

    Job_location = models.CharField(max_length=100)
    Job_designation = models.CharField(max_length=100)
    Job_joining_date = models.CharField(max_length=100)
    Job_relieving_date = models.CharField(max_length=100)



    Internships_company_name = models.CharField(max_length=100)

    Internships_location = models.CharField(max_length=100)
    Internship_designation = models.CharField(max_length=100)
    Internships_joining_date = models.CharField(max_length=100)
    Internships_relieving_date = models.CharField(max_length=100)

    Positions_Responsibility = models.CharField(max_length=100)

    trainings_field = models.CharField(max_length=100)
    trainings_location = models.CharField(max_length=100)
    trainings_joining_date = models.CharField(max_length=100)
    trainings_relieving_date = models.CharField(max_length=100)

    personal_projects_topic= models.CharField(max_length=100)
    personal_projects_description= models.CharField(max_length=100)

    skills = models.CharField(max_length=100)
    blog_link = models.CharField(max_length=100)

    gitHub_profile = models.CharField(max_length=100)
    play_store_link = models.CharField(max_length=100)
    behance_portfolio = models.CharField(max_length=100)
    other_work_sample = models.CharField(max_length=100)
class Testimonial(models.Model):
    user_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    review = models.CharField(max_length=500)

    uploads = models.ImageField(upload_to='media/',
                                          max_length=100)

class Associate(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)

    email = models.EmailField()
    company_name = models.CharField(max_length=100)

    address=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)

    website_url=models.CharField(max_length=10)

    company_size=models.CharField(max_length=100)
    about_company=models.TextField(max_length=100)


class our_team(models.Model):
    user_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    review = models.CharField(max_length=500)
    linkedin_account=models.URLField()

    uploads = models.ImageField(upload_to='media/', max_length=100)
    
    
    
    
class resume(models.Model):
    name = models.CharField(max_length=50, blank=True )   
    title = models.CharField(max_length=30, blank=True )   
    email = models.EmailField(max_length=50, blank=True )
    address = models.CharField(max_length=150, blank=True )
    city = models.CharField(max_length=25, blank=True )
    country = models.CharField(max_length=25, blank=True )
    pnumber = models.CharField(max_length=12, blank=True )
    summary = models.TextField(max_length=200, blank=True )
    jobtitle = models.CharField(max_length=20, blank=True )   
    company = models.CharField(max_length=50, blank=True )
    workmode = models.CharField(max_length=50, blank=True )
    workcountry = models.CharField(max_length=25, blank=True )
    startdate = models.DateField(auto_now=False, auto_now_add=False, blank=True )
    enddate = models.DateField(auto_now=False, auto_now_add=False, blank=True )
    jobdesc = models.TextField(max_length=150,blank=True )
    workhere = models.CharField(max_length=10,blank=True )
    degree = models.CharField(max_length=30, blank=True )
    institudename = models.CharField(max_length=50,blank=True )   
    graduationdate = models.DateField(auto_now=False, auto_now_add=False, blank=True )
    edesc = models.TextField(max_length=150, blank=True )
    skill1 = models.CharField(max_length=32, blank=True )   
    skill2 = models.CharField(max_length=32, blank=True )   
    skill3 = models.CharField(max_length=32, blank=True )   
    skill4 = models.CharField(max_length=32, blank=True )   
    skill5 = models.CharField(max_length=32, blank=True )   
    skill6 = models.CharField(max_length=32, blank=True )   
    def __str__(self):
        returnself.name
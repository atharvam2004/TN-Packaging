import re
import random

from django.contrib import messages
from django.core.mail import send_mail

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import company_profile, Customer,  contact
from .models.customers import Blog, Company_Registration, add_job, \
    add_internship, internform, job_application_form, internship_application_form, Testimonial, Associate,  our_team


def signup(request):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if request.method=="POST":
        first_name=request.POST['first_name']
        email=str(request.POST['email'])
        password=request.POST['password']
        phone=request.POST['phone']
        phone = phone[-10:]
        city=request.POST['city']
        if '@' and '.' not in email :
            messages.warning(request,"Enter a Valid Email ID")
        elif len(password) < 8:
            messages.warning(request, "Minimum 8 characters required for Password")
        elif len(password) > 8:
            messages.warning(request, "Only 8 digit are required For Password")
    
        else:
            try:
                curEmail = Customer.objects.get(email=email)
                messages.warning(request,"Email already registered")
            except Customer.DoesNotExist:
                Customer(first_name=first_name,
                         email=email, password=password,
                         phone=phone, city=city).save()
                messages.success(request, 'The User '
                                 + request.POST['first_name'] +
                                 " is registered Succesfully.")
                return HttpResponseRedirect('/login/')
        return  render(request,"signup.html")

    else:
        #return HttpResponseRedirect('/login/')
        return  render(request,"signup.html")




def companyprofile_save(request):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if request.method=="POST":

        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        organization_name=request.POST.get("organization_name")
        organization_description=request.POST.get("organization_description")
        organization_logo=request.POST.get("organization_logo")
        phone=request.POST.get("phone")
        address = request.POST.get("address")
        organization_website=request.POST.get("organization_website")
        try:
                Details = company_profile.objects.get(organization_name=organization_name,email=email)
                messages.warning(request,"Email or owner name or company name already registered")
        except company_profile.DoesNotExist:
                company_profile(username=username,email=email,password=password,organization_name=organization_name,organization_description=organization_description,organization_logo=organization_logo,
                phone=phone,address=address,organization_website=organization_website).save()
                messages.success(request,"Data Save Successfully..You Can Login Now..")
                return HttpResponseRedirect('/companylogin/')

        return  render(request,"company_profile_form.html")
    else:
        return  render(request,"company_profile_form.html")

def associateformpage(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']

        email = request.POST['email']
        company_name = request.POST['company_name']
        address = request.POST['address']
        state = request.POST['state']
        country = request.POST['country']
        website_url = request.POST['website_url']
        company_size = request.POST['company_size']
        about_company = request.POST['about_company']

        Associate(fname=fname,lname=lname,
        email=email, company_name=company_name,
                            address=address,country=country,state=state,
                             website_url=website_url,company_size=company_size,about_company=about_company).save()
        messages.success(request, 'The company '
                                     + request.POST['company_name'] +
                                     " is registered Succesfully.")

        return render(request, "associate_forms.html")
    else:
        return render(request, "associate_forms.html")

def faqpage(request):
    return render(request, "faq.html")
def teampage(request):
    data=our_team.objects.all()
    return render(request, "team.html",{'show':data})
def associatepage(request):
    return render(request, "associate.html")
def viewresumepage(request):
    return render(request, "viewresume.html")
def applicationformpage(request):
    return render(request, "applicationform.html")

def getloc(request):
    if request.method == 'POST':
        if request.POST['location']:
            query = request.POST['location']
            loc = add_internship.objects.filter(location=query)
        else:
          query = ""
          loc = None
          messages.success(request,"No match found")
    return render(request, 'internship.html', {'locs': loc})

def getint_tit(request):
    if request.method == 'POST':
        if request.POST['browers']:
            query = request.POST['browers']
            results = add_internship.objects.filter(internship_title=query)
        else:
          query = ""
          results = None
          messages.success(request,"No match found")
    return render(request,'internship.html', {'results':results})

def getint_type(request):
    if request.POST['internship_type']:
            it = request.POST['internship_type']
            it = it.str.lower();
            if "full" in it:
                return HttpResponseRedirect('/internship/full_time_internship')
            else:
                return HttpResponseRedirect('/internship/part_time_internship')
    return render(request,"index.html")

def homepage(request):
    # uper functions create kar diya hai bas aapko redirect karvana hai .....
    # if request.method == 'POST':
    #     if request.POST['location']:
    #         query = request.POST['location']
    #         loc = add_internship.objects.filter(location=query)
    #     else:
    #       query = ""
    #       loc = None
    #       messages.success(request,"No match found")
    #     return render(request, 'internship.html', {'locs': loc})

    # elif request.method == 'POST':
    #     if request.POST['browers']:
    #         query = request.POST['browers']
    #         results = add_internship.objects.filter(internship_title=query)
    #     else:
    #       query = ""
    #       results = None
    #       messages.success(request,"No match found")
    #     return render(request,'internship.html', {'results':results})
    # elif request.method == "POST":
    #     if request.POST['internship_type']:
    #         it = request.POST['internship_type']
    #         it = it.str.lower();
    #         if "full" in it:
    #             return HttpResponseRedirect('/internship/full_time_internship')
    #         else:
    #             return HttpResponseRedirect('/internship/part_time_internship')
            # return render(request,"index.html")
    loc = add_internship.objects.all()
    review = Testimonial.objects.all()
    return render(request,"index.html",{'loc':loc,'review':review})

def aboutpage(request):
    return render(request, "about.html")




def loginpage(request):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if request.method == "POST":
        try:
            email = request.POST['email']
            password = request.POST['password']
            if not (re.search(regex, email)):
                messages.warning(request, "Email should contain @gmail.com at the end")
            elif len(password) < 8:
                messages.warning(request, "Minimum 8 characters required for Password")
            Userdetails=Customer.objects.get(email=request.POST['email'],password = request.POST['password'])
            print("Username=",Userdetails)
            request.session['email']=Userdetails.email
            request.session['first_name'] = Userdetails.first_name
            messages.success(request,"Login Successfull")
            count=add_job.objects.all().count()
            ints=add_internship.objects.all().count()
            return render(request, "userdashboard.html",{'count':count,'interns':ints})
        except Customer.DoesNotExist:
            messages.success(request,"Email and Password Invalid..")

    return  render(request,"login.html")


def userdashboardpage(request):
    count=add_job.objects.all().count()
    ints=add_internship.objects.all().count()
    return render(request,"userdashboard.html",{'count':count,'interns':ints})


def companyloginpage(request):
    if request.method == "POST":
        try:
            email = request.POST['email']
            password = request.POST['password']
            Userdetails=company_profile.objects.get(email=request.POST['email'],password=request.POST['password'])
            print("Username=",Userdetails)
            request.session['email']=Userdetails.email
            messages.success(request,"Login Successfull")
            return HttpResponseRedirect("/company")
        except company_profile.DoesNotExist:
            messages.success(request,"Email and Password Invalid..")
    return  render(request,"companylogin.html")

def userlogout(request):
    try:
        del request.session['email']
    except:
        return render(request,"login.html")
    return render(request,"index.html")

def companylogout(request):
    try:
        del request.session['email']
    except:
        return render(request,"login.html")
    return render(request,"index.html")



def company_registration_mainpage(request):
    return render(request, "company_main_registration.html")


def addjobform(request):
    if request.method=="POST":
        try:
            company_name=request.POST['company_name']

            email_address=request.POST['email_address']

            job_type=request.POST['job_type']
            job_title=request.POST['job_title']
            required_skill=request.POST['required_skill']
            experience_requirements = request.POST['experience_requirements']
            job_description = request.POST['job_description']
            responsibilities = request.POST['responsibilities']
            required_qualification = request.POST['required_qualification']
            work_mode = request.POST['work_mode']
            application_deadline = request.POST['application_deadline']
            stipend = request.POST['stipend']
            no_of_positions = request.POST['no_of_positions']
            location = request.POST['location']
            about_company = request.POST['about_company']

            add_job(company_name=company_name,email_address=email_address,job_type=job_type,
                       job_title=job_title,required_skill=required_skill,
                       experience_requirements=experience_requirements,
                job_description=job_description,
                responsibilities=responsibilities,
                required_qualification=required_qualification,
                       work_mode=work_mode,
                 no_of_positions=no_of_positions,
                 application_deadline=application_deadline,
                 stipend=stipend,about_company=about_company,
                 location=location).save()
            messages.success(request,"Data added Succesfully.")
            #return  render(request,"view_job.html")
            return HttpResponseRedirect('/view_job/')

        except Customer.DoesNotExist:
            messages.success(request,"Enter correct details")
    else:
        return  render(request,"add-job.html")


def addineternshipform(request):
    if request.method=="POST":
        company_name=request.POST['company_name']

        email_address=request.POST['email_address']

        internship_type=request.POST['internship_type']
        internship_title=request.POST['internship_title']
        required_skill=request.POST['required_skill']
        experience_requirements = request.POST['experience_requirements']
        internship_description = request.POST['internship_description']
        responsibilities = request.POST['responsibilities']
        required_qualification = request.POST['required_qualification']
        work_mode = request.POST['work_mode']
        application_deadline = request.POST['application_deadline']
        stipend = request.POST['stipend']
        no_of_positions = request.POST['no_of_positions']
        location = request.POST['location']
        about_company = request.POST['about_company']
        add_internship(company_name=company_name,email_address=
        email_address,internship_type=internship_type,
                       internship_title=internship_title,required_skill=required_skill,
                       experience_requirements=experience_requirements,
                internship_description=internship_description,
                responsibilities=responsibilities,
                required_qualification=required_qualification,
         no_of_positions =no_of_positions, application_deadline =
        application_deadline,work_mode=work_mode, stipend = stipend,
                                        about_company = about_company,
                        location = location
        ).save()
        messages.success(request,"Data added Succesfully.")
        return HttpResponseRedirect('/view_internship/')
        return  render(request,"view_internship.html")
    else:
        return  render(request,"add_internship.html")




def profile(request):
    query=Customer.objects.filter(email=request.session['email'])
    print(query)
    return render(request, 'userprofile.html', {'Query': query})




def company_profile_view(request):
    query = company_profile.objects.filter(email=request.session['email'])
    print(query)
    return render(request, "company_profile_view.html", {'Query': query})

# view job

def viewJob(request):

    job_details = add_job.objects.filter(email_address=request.session['email'])
    return render(request, "view_job.html",{'job_detail':job_details})


def update_job(request,id):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')

        email_address = request.POST.get('email_address')

        job_type = request.POST.get('job_type')
        job_title = request.POST.get('job_title')
        required_skill = request.POST.get('required_skill')
        experience_requirements = request.POST.get('experience_requirements')
        job_description = request.POST.get('job_description')
        responsibilities = request.POST.get('responsibilities')
        work_mode = request.POST['work_mode']
        application_deadline = request.POST['application_deadline']
        stipend = request.POST['stipend']
        no_of_positions = request.POST['no_of_positions']
        location = request.POST['location']
        about_company = request.POST['about_company']
        required_qualification = request.POST.get('required_qualification')
        add_job.objects.filter(id=id).update(company_name=company_name,email_address=email_address,job_type=job_type,
                       job_title=job_title,required_skill=required_skill,
                       experience_requirements=experience_requirements,
                job_description=job_description,
                responsibilities=responsibilities,
                required_qualification=required_qualification,
                       work_mode=work_mode,
                 no_of_positions=no_of_positions,
                 application_deadline=application_deadline,
                 stipend=stipend,about_company=about_company,
                 location=location)
        job_details = add_job.objects.filter(id=id)
        messages.success(request,"Data Updated Successfully")
        #return render(request, "view_job.html")
        return HttpResponseRedirect('/view_job/')


    else:
        job_details = add_job.objects.filter(id = id)
    return render(request, "update_view_job.html", {'job_detail': job_details})

#deletes add_job
def delete_job(request,id):
        p = add_job.objects.get(id=id)
        p.delete()
        messages.success(request,"Data Deleted Successfully")

        return HttpResponseRedirect('/view_job/')

# view add_internship

def viewInternship(request):
    email = request.session["email"]
    if email =="":
        messages.success(request, "Login again!!")
    print(email)
    #     handle it
    intern_details = add_internship.objects.filter(email_address=email)
    return render(request, "view_internship.html",{'all_detail':intern_details})



def update_internship(request,id):
    if request.method == 'POST':
        company_name = request.POST['company_name']

        email_address = request.POST['email_address']

        internship_type = request.POST['internship_type']
        internship_title = request.POST['internship_title']
        required_skill = request.POST['required_skill']
        experience_requirements = request.POST['experience_requirements']
        internship_description = request.POST['internship_description']
        responsibilities = request.POST['responsibilities']
        required_qualification = request.POST['required_qualification']
        work_mode = request.POST['work_mode']
        application_deadline = request.POST['application_deadline']
        stipend = request.POST['stipend']
        no_of_positions = request.POST['no_of_positions']
        location = request.POST['location']
        about_company = request.POST['about_company']
        add_internship.objects.filter(id=id).update(company_name=company_name,email_address=
        email_address,internship_type=internship_type,
                       internship_title=internship_title,required_skill=required_skill,
                       experience_requirements=experience_requirements,
                internship_description=internship_description,
                responsibilities=responsibilities,
                required_qualification=required_qualification,
         no_of_positions =no_of_positions, application_deadline =
        application_deadline,work_mode=work_mode, stipend = stipend,
                                        about_company = about_company,
                        location = location)
        intern_details = add_internship.objects.filter(id=id)
        messages.success(request,"Data Updated Successfully")
        #return render(request, "view_internship.html")
        return HttpResponseRedirect('/view_internship/')

    else:
        pi = add_internship.objects.filter(id=id)
        intern_details = add_internship.objects.filter(id=id)
    return render(request, "update_add_internship.html", {'all_detail': intern_details})

#deletes add_internship
def delete_internship(request,id):

        pi = add_internship.objects.get(id = id)
        pi.delete()
        messages.success(request,"Data Deleted Successfully")
        return HttpResponseRedirect('/view_internship/')

def view_job_detail(request,id):
    job_details = add_job.objects.filter(id=id)#this works?
    return render(request, "view_job_detail.html", {'job_detail': job_details})

def view_internship_detail(request,id):

        intern_details = add_internship.objects.filter(id=id)
        return render(request, "view_internship_detail.html", {'all_detail': intern_details})

def show_internship(request):
    show=add_internship.objects.all()
    return render(request, "internship.html", {'Show': show})
def show_job(request):
    show=add_job.objects.all()
    return render(request, "job.html", {'Show': show})
def show_internship_detail(request, id):
    intern_details = add_internship.objects.filter(id=id)
    return render(request, "show_internship detail.html", {'all_detail': intern_details})
def show_job_detail(request, id):
    intern_details = add_job.objects.filter(id=id)
    return render(request, "show_job_detail.html", {'all_detail': intern_details})
def companypage(request):
    count = add_job.objects.filter(email_address=request.session['email']).count()
    ints = add_internship.objects.filter(email_address=request.session['email']).count()
    applicationform = job_application_form.objects.filter(company_email=request.session['email']).count()
    internform = internship_application_form.objects.filter(company_email=request.session['email']).count()
    blog = Blog.objects.filter(email_address=request.session['email']).count()

    return render(request, "company.html", {'Blogs':blog, 'count': count, 'interns': ints,'app':applicationform,'internresume':internform})




def contactinfo(request):
    if request.method=="POST":
        user_name=request.POST['user_name']
        email=request.POST['email']
        subject=request.POST['subject']
        message = request.POST['message']



        contact(user_name=user_name,
                       email=email,subject=subject,
                       message=message,
                       ).save()
        messages.success(request,"Message Sent Succesfully.")
        return  render(request,"contact.html")
    else:
        return  render(request,"contact.html")

#searchjobs
def search(request):
    if request.method == 'POST':
      query = request.POST['q']
      results = add_job.objects.filter(job_title=query)
    else:
      query = ""
      results = None
      messages.success(request,"No match found")

    return render(request,'job.html', {'results':results})
def search_location(request):
    if request.method == 'POST':
      query = request.POST['p']
      loc = add_job.objects.filter(location=query)
    else:
      query = ""
      loc = None
      messages.success(request,"No match found")

    return render(request,'job.html', {'locs':loc})
def search_internship(request):
    if request.method == 'POST':
      query = request.POST['q']
      results = add_internship.objects.filter(internship_title=query)
    else:
      query = ""
      results = None
      messages.success(request,"No match found")

    return render(request,'internship.html', {'results':results})
def searchinternshiplocation(request):
    if request.method == 'POST':
      query = request.POST['p']
      loc = add_internship.objects.filter(location=query)
    else:
      query = ""
      loc = None
      messages.success(request,"No match found")
    return render(request, 'internship.html', {'locs': loc})


def companysignup(request):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if request.method=="POST":
        username=request.POST['username']

        email=request.POST['email']
        password=request.POST['password']
        phone=request.POST['phone'][-10:]
        city=request.POST['city']
        if not username.isalpha() :
            messages.warning(request,"Name should be alphabet only")
        elif not (re.search(regex,email)):
            messages.warning(request,"Email should contain @gmail.com at the end")
        elif len(password) < 8:
            messages.warning(request, "Minimum 8 characters required for Password")
        elif not len(phone) == 10:
            messages.warning(request,"Phone number should be 10 digits only.")
        elif not city.replace(' ','').isalpha():
            messages.warning(request, "City should contain only alphabets")
        else:
            try:
                Details = Company_Registration.objects.get(username=username,email=email)
                messages.warning(request,"Email or Username  already registered")
            except Company_Registration.DoesNotExist:
                Company_Registration(username=username,email=email,password=password,phone=phone,city=city).save()
                messages.success(request,"The User is registered Succesfully.")
                return render(request, "companylogin.html")

        return  render(request,"companysignup.html")

    else:
        return  render(request,"companysignup.html")







def userdashboardprofile(request):
    que=Customer.objects.filter(email=request.session['email'])
    return render(request, 'userdashboard.html', {'Query': que})


def countjob(request):
    count = add_job.objects.all().count()


    return render(request, 'userdashboard.html',{'count':count})

def userjob(request):
    show=add_job.objects.all()
    return render(request, "userjob.html", {'Show': show})


def userinternship(request):
    show=add_internship.objects.all()
    return render(request, "userinternship.html", {'Show': show})

def user_show_internship_detail(request, id):

        if internship_application_form.objects.filter(email=request.session["email"], id=id):
            messages.success(request, "You already applied for that Internship")
            return HttpResponseRedirect("/user_internship")
        else:
           intern_details = add_internship.objects.filter(id=id)
           return render(request, "userinternshipdetail.html", {'all_detail': intern_details})

def user_show_job_detail(request, id):
    try:
        job_application_form.objects.get(email=request.session["email"], id=id)
        messages.success(request, "You already applied for that job")
        return HttpResponseRedirect("/user_job")
    except Exception:
        intern_details = add_job.objects.filter(id=id)
        return render(request, "userjobdetail.html", {'all_detail': intern_details})


#searchjobs




# By jobcategories

def show_internship_design(request):

       showInternship = add_internship.objects.filter(internship_title="Web Designer")
       return render(request,"internship.html",{"showIntern":showInternship})



def show_internship_graphics(request):
    showInternship = add_internship.objects.filter(internship_title="Graphics Designer")
    return render(request,"internship.html",{"showIntern":showInternship})

def show_internship_market(request):
    showInternship = add_internship.objects.filter(internship_title=" Digital Marketing")
    return render(request,"internship.html",{"showIntern":showInternship})

def show_internship_software(request):
    showInternship = add_internship.objects.filter(internship_title="Software Development")
    return render(request,"internship.html",{"showIntern":showInternship})

def show_internship_java(request):
    showInternship = add_internship.objects.filter(internship_title="Java")
    return render(request,"internship.html",{"showIntern":showInternship})

def show_internship_python(request):
    showInternship = add_internship.objects.filter(internship_title="Python")
    return render(request,"internship.html",{"showIntern":showInternship})

def show_internship_web(request):
    showInternship = add_internship.objects.filter(internship_title="Web Developer")
    return render(request,"internship.html",{"showIntern":showInternship})

def show_internship_cother(request):
    showInternship = add_internship.objects.exclude(internship_title="Web Designer")\
                     &add_internship.objects.\
                         exclude(internship_title="Graphics Designer")&\
                     add_internship.objects.exclude(internship_title=" Digital Marketing")\
                     &add_internship.objects.exclude(internship_title="Software Development")\
                     &add_internship.objects.exclude(internship_title="Java")\
                     &add_internship.objects.exclude(internship_title="Python")
    return render(request,"internship.html",{"showIntern":showInternship})



def show_internship_delhi(request):

    showInternship = add_internship.objects.filter(location="Delhi")
    return render(request,"internship.html",{"showIntern":showInternship})

def show_internship_mumbai(request):

    showInternship = add_internship.objects.filter(location="Mumbai")
    return render(request,"internship.html",{"showIntern":showInternship})

def show_internship_hyderbad(request):

    showInternship = add_internship.objects.filter(location="Hyderbad")
    return render(request,"internship.html",{"showIntern":showInternship})

def show_internship_bangalore(request):


    showInternship = add_internship.objects.filter(location="Bangalore")
    return render(request,"internship.html",{"showIntern":showInternship})

def show_internship_chennai(request):

    showInternship = add_internship.objects.filter(location="Chennai")
    return render(request,"internship.html",{"showIntern":showInternship})

def show_internship_kolkata(request):

    showInternship = add_internship.objects.filter(location="Kolkata")
    return render(request,"internship.html",{"showIntern":showInternship})

def show_internship_agra(request):

    showInternship = add_internship.objects.filter(location="Agra")
    return render(request,"internship.html",{"showIntern":showInternship})

def show_internship_pune(request):


      showInternship = add_internship.objects.filter(location="Pune")
      return render(request,"internship.html",{"showIntern":showInternship})

def show_internship_other(request):
    showInternship = (add_internship.objects.
                      exclude(location="Delhi") &
                      add_internship.objects.exclude(location="Mumbai")&
                      add_internship.objects.exclude(location="Hyderbad")&
                      add_internship.objects.exclude(location="Bangalore")&
                      add_internship.objects.exclude(location="Chennai")&
                      add_internship.objects.exclude(location="Kolkata")&
                      add_internship.objects.exclude(location="Agra"))

    return render(request,"internship.html",{"showIntern":showInternship})
# By jobcategories

def show_job_design(request):
       showInternship = add_job.objects.filter(job_title="Webd designer")
       return render(request,"job.html",{"showIntern":showInternship})



def show_job_graphics(request):
    showInternship = add_job.objects.filter(job_title="Graphic Designer")
    return render(request,"job.html",{"showIntern":showInternship})

def show_job_market(request):
    showInternship = add_job.objects.filter(job_title="Digital Marketing")
    return render(request,"job.html",{"showIntern":showInternship})

def show_job_software(request):
    showInternship = add_job.objects.filter(job_title="Software Development")
    return render(request,"job.html",{"showIntern":showInternship})

def show_job_java(request):
    showInternship = add_job.objects.filter(job_title="Java")
    return render(request,"job.html",{"showIntern":showInternship})

def show_job_python(request):
    showInternship = add_job.objects.filter(job_title="Python")
    return render(request,"job.html",{"showIntern":showInternship})

def show_job_web(request):
    showInternship = add_job.objects.filter(job_title="Web Developer")
    return render(request,"job.html",{"showIntern":showInternship})

def show_job_cother(request):
    showInternship = add_job.objects.exclude(job_title="Web Designer")\
                     &add_job.objects.exclude(job_title="Graphics Designer")\
                     &add_job.objects.exclude(job_title=" Digital Marketing")\
                     &add_job.objects.exclude(job_title="Software Development")\
                     &add_job.objects.exclude(job_title="Java")&\
                     add_job.objects.exclude(job_title="Python")
    return render(request,"job.html",{"showIntern":showInternship})



def show_job_delhi(request):

    showInternship = add_job.objects.filter(location="Delhi")
    return render(request,"job.html",{"showIntern":showInternship})

def show_job_mumbai(request):

    showInternship = add_job.objects.filter(location="Mumbai")
    return render(request,"job.html",{"showIntern":showInternship})

def show_job_hyderbad(request):

    showInternship = add_job.objects.filter(location="Hyderbad")
    return render(request,"job.html",{"showIntern":showInternship})

def show_job_bangalore(request):


    showInternship = add_job.objects.filter(location="Bangalore")
    return render(request,"job.html",{"showIntern":showInternship})

def show_job_chennai(request):

    showInternship = add_job.objects.filter(location="Chennai")
    return render(request,"job.html",{"showIntern":showInternship})

def show_job_kolkata(request):

    showInternship = add_job.objects.filter(location="Kolkata")
    return render(request,"job.html",{"showIntern":showInternship})

def show_job_agra(request):

    showInternship = add_job.objects.filter(location="Agra")
    return render(request,"job.html",{"showIntern":showInternship})

def show_job_pune(request):


      showInternship = add_job.objects.filter(location="Pune")
      return render(request,"job.html",{"showIntern":showInternship})

def show_job_other(request):
    showInternship = (add_job.objects.
                      exclude(location="Delhi") &
                      add_job.objects.exclude(location="Mumbai")&
                      add_job.objects.exclude(location="Hyderbad")&
                      add_job.objects.exclude(location="Bangalore")&
                      add_job.objects.exclude(location="Chennai")&
                      add_job.objects.exclude(location="Kolkata")&
                      add_job.objects.exclude(location="Agra"))

    return render(request,"job.html",{"showIntern":showInternship})



def addblogpage(request):
    if request.method == "POST":
        company_name = request.POST['company_name']

        email_address = request.POST['email_address']
        location = request.POST['location']

        title = request.POST['title']
        sub_title = request.POST['sub_title']
        description = request.POST['description']
        uploads = request.FILES['uploads']

        Blog(company_name=company_name, email_address=email_address,
                 title=title, sub_title=sub_title,
                 description=description,
                 uploads=uploads
                 ,location=location).save()
        messages.success(request, "Data added Succesfully.")
        return HttpResponseRedirect('/view_add_blogs/')

    else:
        return render(request, "add_blog.html")
def viewaddblog(request):
        email = request.session["email"]
        if email == "":
            messages.success(request, "Login again!!")
        print(email)
        #     handle it
        intern_details = Blog.objects.filter(email_address=email)
        return render(request, "view_blog.html", {'all_detail': intern_details})

def view_add_blog_detail(request,id):
    allblogs = Blog.objects.filter(id=id)
    return render(request, "add_view_blog_detail.html", {'all_blog':allblogs})
def update_blog(request,id):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')

        email_address = request.POST.get('email_address')
        location = request.POST['location']

        title = request.POST['title']
        sub_title = request.POST['sub_title']
        description = request.POST['description']
        uploads = request.POST['uploads']

        Blog.objects.filter(id=id).update(company_name=company_name, email_address=email_address,
                 title=title, sub_title=sub_title,
                 description=description,
                 uploads=uploads,location=location
                 )
        blog_details = Blog.objects.filter(id=id)
        messages.success(request,"Data Updated Successfully")
        return HttpResponseRedirect('/view_add_blogs/')
        #return render(request, "view_blog.html")



    else:
        blog_details = Blog.objects.filter(id=id)
    return render(request, "update_add_blog.html", {'blog_detail': blog_details})

#deletes add_job
def delete_blog(request,id):
        p = Blog.objects.get(id=id)
        p.delete()
        messages.success(request,"Data Deleted Successfully")
        return HttpResponseRedirect('/view_add_blogs/')

        #return render(request, "add_view_blog_detail.html")
def userblog(request):
    blogshow=Blog.objects.all()
    return  render(request,"blogs.html",{'Blogshow':blogshow})

def show_job_full_time_job(request):

    showInternship = add_job.objects.filter(job_type="Full Time Job")
    return render(request,"job.html",{"showIntern":showInternship})

def show_job_part_time_job(request):

    showInternship = add_job.objects.filter(job_type="Part Time Job")
    return render(request,"job.html",{"showIntern":showInternship})
def show_internship_full_time_internship(request):

    showInternship = add_internship.objects.filter(internship_type="Full Time Internship")
    return render(request,"internship.html",{"showIntern":showInternship})

def show_internship_part_time_internship(request):

    showInternship = add_internship.objects.filter(internship_type="Part Time Internship")
    return render(request,"internship.html",{"showIntern":showInternship})
def userblogdetail(request,id):
    blogshows=Blog.objects.filter(id=id)
    return  render(request,"blogdetails.html",{'Blogshows':blogshows})



def internship(request):
    try:
        user = internform.objects.get(email=request.session["email"])

        resumes = internform.objects.filter(email=request.session["email"])
        return render(request, "viewresume.html", {'Resume': resumes,'user':user})
    except internform.DoesNotExist:

        if request.method=="POST":

            fname=request.POST['fname']
            lname=request.POST['lname']
            email=request.POST['email']
            phone=request.POST['phone']
            city=request.POST['city']
            hometown=request.POST['hometown']

            secondary_class=request.POST['secondary_class']
            secondary_year=request.POST['secondary_year']
            secondary_percentage=request.POST['secondary_percentage']
            seniorsecondary=request.POST['seniorsecondary']
            seniorsecondary_year=request.POST['seniorsecondary_year']
            seniorecondary_percentage=request.POST['seniorsecondary_percentage']
            Diploma_field=request.POST['Diploma_field']
            Diploma_college=request.POST['Diploma_college']
            Diploma_year=request.POST['Diploma_year']
            Diploma_percentage=request.POST['Diploma_percentage']
            graduation_field=request.POST['graduation_field']
            graduation_college=request.POST['graduation_college']
            graduation_year=request.POST['graduation_year']
            grad_percentage=request.POST['grad_percentage']
            post_graduation_field=request.POST['post_graduation_field']
            post_graduation_college=request.POST['post_graduation_college']
            post_graduation_year=request.POST['post_graduation_year']
            post_graduation_percentage=request.POST['post_graduation_percentage']
            Phd_field=request.POST['Phd_field']
            Phd_college=request.POST['Phd_college']
            Phd_year=request.POST['Phd_year']
            Phd_percentage=request.POST['Phd_percentage']

            Job_company_name=request.POST['Job_company_name']
            Job_location=request.POST['Job_location']
            Job_designation=request.POST['Job_designation']
            Job_joining_date=request.POST['Job_joining_date']
            Job_relieving_date=request.POST['Job_relieving_date']
            Internships_company_name=request.POST['Internships_company_name']
            Internships_location=request.POST['Internships_location']
            Internship_designation=request.POST['Internship_designation']
            Internships_joining_date=request.POST['Internships_joining_date']
            Internships_relieving_date=request.POST['Internships_relieving_date']

            Positions_Responsibility=request.POST['Positions_Responsibility']
            trainings_field=request.POST['trainings_field']
            trainings_location=request.POST['trainings_location']
            trainings_joining_date=request.POST['trainings_joining_date']
            trainings_relieving_date=request.POST['trainings_relieving_date']

            personal_projects_topic=request.POST['personal_projects_topic']
            personal_projects_description=request.POST['personal_projects_description']
            skills = request.POST['skills']
            blog_link = request.POST['blog_link']
            gitHub_profile = request.POST['gitHub_profile']
            play_store_link = request.POST['play_store_link']
            behance_portfolio = request.POST['behance_portfolio']
            other_work_sample = request.POST['other_work_sample']

            internform(fname=fname,lname=lname,email=email,phone=phone,city=city
                       ,hometown=hometown,
            secondary_class=secondary_class,secondary_year=secondary_year,secondary_percentage=secondary_percentage,skills=skills,blog_link=blog_link,
                   seniorsecondary=seniorsecondary,seniorsecondary_year =seniorsecondary_year,
                       seniorecondary_percentage=seniorecondary_percentage,Diploma_field=Diploma_field,
            Diploma_college =Diploma_college,
            Diploma_year=Diploma_year ,Diploma_percentage=Diploma_percentage,graduation_field=graduation_field,graduation_college=graduation_college ,
            graduation_year=graduation_year,grad_percentage=grad_percentage,post_graduation_field=post_graduation_field ,
            post_graduation_college=post_graduation_college ,
            post_graduation_year=post_graduation_year ,post_graduation_percentage=post_graduation_percentage ,
            Phd_field=Phd_field ,Phd_college=Phd_college ,Phd_year=Phd_year,
            Phd_percentage=Phd_percentage,Job_company_name=Job_company_name ,
            Job_location=Job_location , Job_designation=Job_designation,
            Job_joining_date=Job_joining_date ,Job_relieving_date=Job_relieving_date ,

            Internships_company_name=Internships_company_name,
                       Internships_location=Internships_location ,
                       Internship_designation=Internship_designation,
            Internships_joining_date =Internships_joining_date,
            Internships_relieving_date =Internships_relieving_date ,
                       Positions_Responsibility =Positions_Responsibility,
            trainings_field =trainings_field ,trainings_location =trainings_location ,
            trainings_joining_date =trainings_joining_date ,trainings_relieving_date =trainings_relieving_date , personal_projects_topic =personal_projects_topic ,
            personal_projects_description =personal_projects_description ,gitHub_profile=gitHub_profile,play_store_link=play_store_link,behance_portfolio=behance_portfolio,other_work_sample=other_work_sample
                       ).save()

            messages.success(request,'The Form '
                             +request.POST['fname']+
                             " is registered Succesfully.")
            return  render(request,"viewresume.html")
            return HttpResponseRedirect('/userresumes')

        else:
           return  render(request,"applicationform.html")

def userresume(request):
    try:
        user = internform.objects.get(email=request.session["email"])

        resumes = internform.objects.filter(email=request.session["email"])
        return render(request, "viewresume.html", {'Resume': resumes, 'user': user})

    except Exception:
        return render(request, "applicationform.html")



def form_apply(request,):
    if request.method=="POST":

        company_name = request.POST['company_name'],
        company_email = request.POST['company_email']


        field = request.POST['field']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        phone=request.POST['phone']
        city=request.POST['city']
        hometown=request.POST['hometown']

        secondary_class=request.POST['secondary_class']
        secondary_year=request.POST['secondary_year']
        secondary_percentage=request.POST['secondary_percentage']
        seniorsecondary=request.POST['seniorsecondary']
        seniorsecondary_year=request.POST['seniorsecondary_year']
        seniorecondary_percentage=request.POST['seniorsecondary_percentage']
        Diploma_field=request.POST['Diploma_field']
        Diploma_college=request.POST['Diploma_college']
        Diploma_year=request.POST['Diploma_year']
        Diploma_percentage=request.POST['Diploma_percentage']
        graduation_field=request.POST['graduation_field']
        graduation_college=request.POST['graduation_college']
        graduation_year=request.POST['graduation_year']
        grad_percentage=request.POST['grad_percentage']
        post_graduation_field=request.POST['post_graduation_field']
        post_graduation_college=request.POST['post_graduation_college']
        post_graduation_year=request.POST['post_graduation_year']
        post_graduation_percentage=request.POST['post_graduation_percentage']
        Phd_field=request.POST['Phd_field']
        Phd_college=request.POST['Phd_college']
        Phd_year=request.POST['Phd_year']
        Phd_percentage=request.POST['Phd_percentage']

        Job_company_name=request.POST['Job_company_name']
        Job_location=request.POST['Job_location']
        Job_designation=request.POST['Job_designation']
        Job_joining_date=request.POST['Job_joining_date']
        Job_relieving_date=request.POST['Job_relieving_date']
        Internships_company_name=request.POST['Internships_company_name']
        Internships_location=request.POST['Internships_location']
        Internship_designation=request.POST['Internship_designation']
        Internships_joining_date=request.POST['Internships_joining_date']
        Internships_relieving_date=request.POST['Internships_relieving_date']

        Positions_Responsibility=request.POST['Positions_Responsibility']
        trainings_field=request.POST['trainings_field']
        trainings_location=request.POST['trainings_location']
        trainings_joining_date=request.POST['trainings_joining_date']
        trainings_relieving_date=request.POST['trainings_relieving_date']

        personal_projects_topic=request.POST['personal_projects_topic']
        personal_projects_description=request.POST['personal_projects_description']
        skills = request.POST['skills']
        blog_link = request.POST['blog_link']
        gitHub_profile = request.POST['gitHub_profile']
        play_store_link = request.POST['play_store_link']
        behance_portfolio = request.POST['behance_portfolio']
        other_work_sample = request.POST['other_work_sample']



        job_application_form(company_name=company_name,company_email=
        company_email,field=field,fname=fname,lname=lname,email=email,phone=phone,city=city
                   ,hometown=hometown,secondary_class=secondary_class,secondary_year=secondary_year,secondary_percentage=secondary_percentage,skills=skills,blog_link=blog_link,
               seniorsecondary=seniorsecondary,seniorsecondary_year =seniorsecondary_year,
                   seniorecondary_percentage=seniorecondary_percentage,Diploma_field=Diploma_field,
        Diploma_college =Diploma_college,
        Diploma_year=Diploma_year ,Diploma_percentage=Diploma_percentage,graduation_field=graduation_field,graduation_college=graduation_college ,
        graduation_year=graduation_year,grad_percentage=grad_percentage,post_graduation_field=post_graduation_field ,
        post_graduation_college=post_graduation_college ,
        post_graduation_year=post_graduation_year ,post_graduation_percentage=post_graduation_percentage ,
        Phd_field=Phd_field ,Phd_college=Phd_college ,Phd_year=Phd_year,
        Phd_percentage=Phd_percentage,Job_company_name=Job_company_name ,
        Job_location=Job_location , Job_designation=Job_designation,
        Job_joining_date=Job_joining_date ,Job_relieving_date=Job_relieving_date ,

        Internships_company_name=Internships_company_name,
                   Internships_location=Internships_location ,
                   Internship_designation=Internship_designation,
        Internships_joining_date =Internships_joining_date,
        Internships_relieving_date =Internships_relieving_date ,
                   Positions_Responsibility =Positions_Responsibility,
        trainings_field =trainings_field ,trainings_location =trainings_location ,
        trainings_joining_date =trainings_joining_date ,trainings_relieving_date =trainings_relieving_date , personal_projects_topic =personal_projects_topic ,
        personal_projects_description =personal_projects_description ,gitHub_profile=gitHub_profile,play_store_link=play_store_link,behance_portfolio=behance_portfolio,other_work_sample=other_work_sample

       ).save()

        messages.success(request, 'Your Data for Job are sent Successfull')

        return HttpResponseRedirect('/user_job/')

    else:
        return  render(request,"jobapply.html")






def applyformdata(request,id):
    try:
        user = internform.objects.get(email = request.session["email"])
        intern_details = add_job.objects.filter(id=id)

        intern_data = internform.objects.filter(email=request.session["email"])
        return render(request, "jobapply.html", {'all_data': intern_data,'intern_details': intern_details,'users':user})
        #return render(request, "jobapply.html", {'all_data': intern_data,'intern_details': intern_details})

    except internform.DoesNotExist:
        if request.method == "POST":
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            phone = request.POST['phone']
            city = request.POST['city']
            hometown = request.POST['hometown']

            secondary_class = request.POST['secondary_class']
            secondary_year = request.POST['secondary_year']
            secondary_percentage = request.POST['secondary_percentage']
            seniorsecondary = request.POST['seniorsecondary']
            seniorsecondary_year = request.POST['seniorsecondary_year']
            seniorecondary_percentage = request.POST['seniorsecondary_percentage']
            Diploma_field = request.POST['Diploma_field']
            Diploma_college = request.POST['Diploma_college']
            Diploma_year = request.POST['Diploma_year']
            Diploma_percentage = request.POST['Diploma_percentage']
            graduation_field = request.POST['graduation_field']
            graduation_college = request.POST['graduation_college']
            graduation_year = request.POST['graduation_year']
            grad_percentage = request.POST['grad_percentage']
            post_graduation_field = request.POST['post_graduation_field']
            post_graduation_college = request.POST['post_graduation_college']
            post_graduation_year = request.POST['post_graduation_year']
            post_graduation_percentage = request.POST['post_graduation_percentage']
            Phd_field = request.POST['Phd_field']
            Phd_college = request.POST['Phd_college']
            Phd_year = request.POST['Phd_year']
            Phd_percentage = request.POST['Phd_percentage']

            Job_company_name = request.POST['Job_company_name']
            Job_location = request.POST['Job_location']
            Job_designation = request.POST['Job_designation']
            Job_joining_date = request.POST['Job_joining_date']
            Job_relieving_date = request.POST['Job_relieving_date']
            Internships_company_name = request.POST['Internships_company_name']
            Internships_location = request.POST['Internships_location']
            Internship_designation = request.POST['Internship_designation']
            Internships_joining_date = request.POST['Internships_joining_date']
            Internships_relieving_date = request.POST['Internships_relieving_date']

            Positions_Responsibility = request.POST['Positions_Responsibility']
            trainings_field = request.POST['trainings_field']
            trainings_location = request.POST['trainings_location']
            trainings_joining_date = request.POST['trainings_joining_date']
            trainings_relieving_date = request.POST['trainings_relieving_date']

            personal_projects_topic = request.POST['personal_projects_topic']
            personal_projects_description = request.POST['personal_projects_description']
            skills = request.POST['skills']
            blog_link = request.POST['blog_link']
            gitHub_profile = request.POST['gitHub_profile']
            play_store_link = request.POST['play_store_link']
            behance_portfolio = request.POST['behance_portfolio']
            other_work_sample = request.POST['other_work_sample']

            internform(fname=fname, lname=lname, email=email, phone=phone, city=city
                       , hometown=hometown,
                       secondary_class=secondary_class, secondary_year=secondary_year,
                       secondary_percentage=secondary_percentage, skills=skills, blog_link=blog_link,
                       seniorsecondary=seniorsecondary, seniorsecondary_year=seniorsecondary_year,
                       seniorecondary_percentage=seniorecondary_percentage, Diploma_field=Diploma_field,
                       Diploma_college=Diploma_college,
                       Diploma_year=Diploma_year, Diploma_percentage=Diploma_percentage,
                       graduation_field=graduation_field, graduation_college=graduation_college,
                       graduation_year=graduation_year, grad_percentage=grad_percentage,
                       post_graduation_field=post_graduation_field,
                       post_graduation_college=post_graduation_college,
                       post_graduation_year=post_graduation_year, post_graduation_percentage=post_graduation_percentage,
                       Phd_field=Phd_field, Phd_college=Phd_college, Phd_year=Phd_year,
                       Phd_percentage=Phd_percentage, Job_company_name=Job_company_name,
                       Job_location=Job_location, Job_designation=Job_designation,
                       Job_joining_date=Job_joining_date, Job_relieving_date=Job_relieving_date,

                       Internships_company_name=Internships_company_name,
                       Internships_location=Internships_location,
                       Internship_designation=Internship_designation,
                       Internships_joining_date=Internships_joining_date,
                       Internships_relieving_date=Internships_relieving_date,
                       Positions_Responsibility=Positions_Responsibility,
                       trainings_field=trainings_field, trainings_location=trainings_location,
                       trainings_joining_date=trainings_joining_date, trainings_relieving_date=trainings_relieving_date,
                       personal_projects_topic=personal_projects_topic,
                       personal_projects_description=personal_projects_description, gitHub_profile=gitHub_profile,
                       play_store_link=play_store_link, behance_portfolio=behance_portfolio,
                       other_work_sample=other_work_sample
                       ).save()

            messages.success(request, 'Your Resume is Created Succesfully')

            return render(request, "userjobdetail.html")

        else:
            return render(request, "applicationform.html")





def applyinternshipformdata(request,id):
    try:
        user = internform.objects.get(email=request.session["email"])
        intern_details = add_internship.objects.filter(id=id)
        intern_data = internform.objects.filter(email=request.session["email"])
        return render(request, "internhsipapply.html", {'all_data': intern_data, 'intern_details': intern_details,'user':user})
        #return HttpResponseRedirect('/user_internship/')
    except internform.DoesNotExist:
        if request.method == "POST":
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            phone = request.POST['phone']
            city = request.POST['city']
            hometown = request.POST['hometown']

            secondary_class = request.POST['secondary_class']
            secondary_year = request.POST['secondary_year']
            secondary_percentage = request.POST['secondary_percentage']
            seniorsecondary = request.POST['seniorsecondary']
            seniorsecondary_year = request.POST['seniorsecondary_year']
            seniorecondary_percentage = request.POST['seniorsecondary_percentage']
            Diploma_field = request.POST['Diploma_field']
            Diploma_college = request.POST['Diploma_college']
            Diploma_year = request.POST['Diploma_year']
            Diploma_percentage = request.POST['Diploma_percentage']
            graduation_field = request.POST['graduation_field']
            graduation_college = request.POST['graduation_college']
            graduation_year = request.POST['graduation_year']
            grad_percentage = request.POST['grad_percentage']
            post_graduation_field = request.POST['post_graduation_field']
            post_graduation_college = request.POST['post_graduation_college']
            post_graduation_year = request.POST['post_graduation_year']
            post_graduation_percentage = request.POST['post_graduation_percentage']
            Phd_field = request.POST['Phd_field']
            Phd_college = request.POST['Phd_college']
            Phd_year = request.POST['Phd_year']
            Phd_percentage = request.POST['Phd_percentage']

            Job_company_name = request.POST['Job_company_name']
            Job_location = request.POST['Job_location']
            Job_designation = request.POST['Job_designation']
            Job_joining_date = request.POST['Job_joining_date']
            Job_relieving_date = request.POST['Job_relieving_date']
            Internships_company_name = request.POST['Internships_company_name']
            Internships_location = request.POST['Internships_location']
            Internship_designation = request.POST['Internship_designation']
            Internships_joining_date = request.POST['Internships_joining_date']
            Internships_relieving_date = request.POST['Internships_relieving_date']

            Positions_Responsibility = request.POST['Positions_Responsibility']
            trainings_field = request.POST['trainings_field']
            trainings_location = request.POST['trainings_location']
            trainings_joining_date = request.POST['trainings_joining_date']
            trainings_relieving_date = request.POST['trainings_relieving_date']

            personal_projects_topic = request.POST['personal_projects_topic']
            personal_projects_description = request.POST['personal_projects_description']
            skills = request.POST['skills']
            blog_link = request.POST['blog_link']
            gitHub_profile = request.POST['gitHub_profile']
            play_store_link = request.POST['play_store_link']
            behance_portfolio = request.POST['behance_portfolio']
            other_work_sample = request.POST['other_work_sample']

            internform(fname=fname, lname=lname, email=email, phone=phone, city=city
                       , hometown=hometown,
                       secondary_class=secondary_class, secondary_year=secondary_year,
                       secondary_percentage=secondary_percentage, skills=skills, blog_link=blog_link,
                       seniorsecondary=seniorsecondary, seniorsecondary_year=seniorsecondary_year,
                       seniorecondary_percentage=seniorecondary_percentage, Diploma_field=Diploma_field,
                       Diploma_college=Diploma_college,
                       Diploma_year=Diploma_year, Diploma_percentage=Diploma_percentage,
                       graduation_field=graduation_field, graduation_college=graduation_college,
                       graduation_year=graduation_year, grad_percentage=grad_percentage,
                       post_graduation_field=post_graduation_field,
                       post_graduation_college=post_graduation_college,
                       post_graduation_year=post_graduation_year, post_graduation_percentage=post_graduation_percentage,
                       Phd_field=Phd_field, Phd_college=Phd_college, Phd_year=Phd_year,
                       Phd_percentage=Phd_percentage, Job_company_name=Job_company_name,
                       Job_location=Job_location, Job_designation=Job_designation,
                       Job_joining_date=Job_joining_date, Job_relieving_date=Job_relieving_date,

                       Internships_company_name=Internships_company_name,
                       Internships_location=Internships_location,
                       Internship_designation=Internship_designation,
                       Internships_joining_date=Internships_joining_date,
                       Internships_relieving_date=Internships_relieving_date,
                       Positions_Responsibility=Positions_Responsibility,
                       trainings_field=trainings_field, trainings_location=trainings_location,
                       trainings_joining_date=trainings_joining_date, trainings_relieving_date=trainings_relieving_date,
                       personal_projects_topic=personal_projects_topic,
                       personal_projects_description=personal_projects_description, gitHub_profile=gitHub_profile,
                       play_store_link=play_store_link, behance_portfolio=behance_portfolio,
                       other_work_sample=other_work_sample
                       ).save()

            messages.success(request, 'Your Resume is Created Succesfully')

            return render(request, "userinternshipdetail.html")

        else:
            return render(request, "applicationform.html")





def internship_form_apply(request,):
    if request.method == "POST":

        company_name = request.POST['company_name'],
        company_email = request.POST['company_email']

        field = request.POST['field']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        city = request.POST['city']
        hometown = request.POST['hometown']

        secondary_class = request.POST['secondary_class']
        secondary_year = request.POST['secondary_year']
        secondary_percentage = request.POST['secondary_percentage']
        seniorsecondary = request.POST['seniorsecondary']
        seniorsecondary_year = request.POST['seniorsecondary_year']
        seniorecondary_percentage = request.POST['seniorsecondary_percentage']
        Diploma_field = request.POST['Diploma_field']
        Diploma_college = request.POST['Diploma_college']
        Diploma_year = request.POST['Diploma_year']
        Diploma_percentage = request.POST['Diploma_percentage']
        graduation_field = request.POST['graduation_field']
        graduation_college = request.POST['graduation_college']
        graduation_year = request.POST['graduation_year']
        grad_percentage = request.POST['grad_percentage']
        post_graduation_field = request.POST['post_graduation_field']
        post_graduation_college = request.POST['post_graduation_college']
        post_graduation_year = request.POST['post_graduation_year']
        post_graduation_percentage = request.POST['post_graduation_percentage']
        Phd_field = request.POST['Phd_field']
        Phd_college = request.POST['Phd_college']
        Phd_year = request.POST['Phd_year']
        Phd_percentage = request.POST['Phd_percentage']

        Job_company_name = request.POST['Job_company_name']
        Job_location = request.POST['Job_location']
        Job_designation = request.POST['Job_designation']
        Job_joining_date = request.POST['Job_joining_date']
        Job_relieving_date = request.POST['Job_relieving_date']
        Internships_company_name = request.POST['Internships_company_name']
        Internships_location = request.POST['Internships_location']
        Internship_designation = request.POST['Internship_designation']
        Internships_joining_date = request.POST['Internships_joining_date']
        Internships_relieving_date = request.POST['Internships_relieving_date']

        Positions_Responsibility = request.POST['Positions_Responsibility']
        trainings_field = request.POST['trainings_field']
        trainings_location = request.POST['trainings_location']
        trainings_joining_date = request.POST['trainings_joining_date']
        trainings_relieving_date = request.POST['trainings_relieving_date']

        personal_projects_topic = request.POST['personal_projects_topic']
        personal_projects_description = request.POST['personal_projects_description']
        skills = request.POST['skills']
        blog_link = request.POST['blog_link']
        gitHub_profile = request.POST['gitHub_profile']
        play_store_link = request.POST['play_store_link']
        behance_portfolio = request.POST['behance_portfolio']
        other_work_sample = request.POST['other_work_sample']

        internship_application_form(company_name=company_name, company_email=
        company_email, field=field, fname=fname, lname=lname, email=email, phone=phone, city=city
                             , hometown=hometown, secondary_class=secondary_class, secondary_year=secondary_year,
                             secondary_percentage=secondary_percentage, skills=skills, blog_link=blog_link,
                             seniorsecondary=seniorsecondary, seniorsecondary_year=seniorsecondary_year,
                             seniorecondary_percentage=seniorecondary_percentage, Diploma_field=Diploma_field,
                             Diploma_college=Diploma_college,
                             Diploma_year=Diploma_year, Diploma_percentage=Diploma_percentage,
                             graduation_field=graduation_field, graduation_college=graduation_college,
                             graduation_year=graduation_year, grad_percentage=grad_percentage,
                             post_graduation_field=post_graduation_field,
                             post_graduation_college=post_graduation_college,
                             post_graduation_year=post_graduation_year,
                             post_graduation_percentage=post_graduation_percentage,
                             Phd_field=Phd_field, Phd_college=Phd_college, Phd_year=Phd_year,
                             Phd_percentage=Phd_percentage, Job_company_name=Job_company_name,
                             Job_location=Job_location, Job_designation=Job_designation,
                             Job_joining_date=Job_joining_date, Job_relieving_date=Job_relieving_date,

                             Internships_company_name=Internships_company_name,
                             Internships_location=Internships_location,
                             Internship_designation=Internship_designation,
                             Internships_joining_date=Internships_joining_date,
                             Internships_relieving_date=Internships_relieving_date,
                             Positions_Responsibility=Positions_Responsibility,
                             trainings_field=trainings_field, trainings_location=trainings_location,
                             trainings_joining_date=trainings_joining_date,
                             trainings_relieving_date=trainings_relieving_date,
                             personal_projects_topic=personal_projects_topic,
                             personal_projects_description=personal_projects_description, gitHub_profile=gitHub_profile,
                             play_store_link=play_store_link, behance_portfolio=behance_portfolio,
                             other_work_sample=other_work_sample

                             ).save()

        messages.success(request, 'Your Data for Job are sent Successfull')
        #return  render(request,"userinternshipdetail.html")
        return HttpResponseRedirect('/user_internship/')
    else:
        return  render(request,"internhsipapply.html")
def internship_resumes(request):
    email = request.session["email"]
    if email =="":
        messages.success(request, "Login again!!")
    print(email)

    resume = internship_application_form.objects.filter(company_email=email)
    return render(request, "internship_resume.html",{'all_details':resume})

def internship_resumesdetails(request,id):
    resumedetails = internship_application_form.objects.filter(id=id)
    return render(request, "internship_resume_detail.html", {'all_details': resumedetails})

def internship_delete_resume(request, id):
        pi = internship_application_form.objects.get(id=id)
        pi.delete()
        messages.success(request, "Resume Deleted Successfully")
        return render(request, 'internship_resume.html')

def resumes(request):
    email = request.session["email"]
    if email =="":
        messages.success(request, "Login again!!")
    print(email)

    resume = job_application_form.objects.filter(company_email=email)
    return render(request, "resume.html",{'all_details':resume})

def resumesdetails(request,id):
    resumedetails = job_application_form.objects.filter(id=id)
    return render(request, "applicationformdetail.html", {'all_details': resumedetails})

def delete_resume(request, id):
        pi = job_application_form.objects.get(id=id)
        pi.delete()
        messages.success(request, "Resume Deleted Successfully")
        return render(request, 'resume.html')


# profile update

def company_profile_update(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        organization_name = request.POST.get('organization_name')
        organization_description = request.POST.get('organization_description')
        phone = request.POST.get('phone')

        address = request.POST.get('address')
        company_profile.objects.filter(email=request.session['email']).update(username=username,
                                                                              organization_name=organization_name,
                                                                              organization_description=organization_description,
        phone = phone, address = address)
        profile = company_profile.objects.filter(email=request.session['email'])
        return HttpResponseRedirect('/company_profile_view/')
    else:
        profile = company_profile.objects.filter(email=request.session['email'])
    return render(request, "company_profile_edit.html", {"profile": profile})


def user_profile_update(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')

        email = request.POST.get('email')

        phone = request.POST.get('phone')
        city = request.POST.get('city')

        Customer.objects.filter(email=email).update(first_name=first_name, email=email,
                                                    phone=phone, city=city)
        profile = Customer.objects.filter(email=email)
        return HttpResponseRedirect('/profile/')
    else:
        profile = Customer.objects.filter(email=request.session['email'])
    return render(request, "user_profile_edit.html", {"profile": profile})


# change password

def user_change_password(request):
    if request.method == 'POST':
        try:
            email = request.session['email']
            prev_password = request.POST.get('prev_password')

            new_password = request.POST.get('new_password')

            conf_password = request.POST.get('conf_password')
            userdetails = Customer.objects.get(email=email, password=prev_password)
            if userdetails.password == prev_password:

                if not new_password == conf_password:
                    messages.warning(request, "Password Not same")
                elif len(new_password) < 8:
                    messages.warning(request, "Minimum 8 characters required for Password")
                else:
                    Customer.objects.filter(email=email).update(password=new_password)
                    messages.success(request, "Password changed")
        except Customer.DoesNotExist:
            messages.success(request, "Password Invalid..")
    return render(request, "user_change_password.html")


def company_change_password(request):
    if request.method == 'POST':
        try:
            email = request.session['email']
            prev_password = request.POST.get('prev_password')

            new_password = request.POST.get('new_password')

            conf_password = request.POST.get('conf_password')
            userdetails = company_profile.objects.get(email=email, password=prev_password)
            if userdetails.password == prev_password:

                if not new_password == conf_password:
                    messages.warning(request, "Password Not same")
                else:
                    company_profile.objects.filter(email=email).update(password=new_password)
                    messages.success(request, "Password changed")
        except company_profile.DoesNotExist:
            messages.success(request, "Password Invalid..")
    return render(request, "company_change_password.html")

#for userpanel
def search1(request):
    if request.method == 'POST':
      query = request.POST['q']
      results = add_job.objects.filter(job_title=query)
    else:
      query = ""
      results = None
      messages.success(request,"No match found")

    return render(request,'userjob.html', {'results':results})
def search_location1(request):
    if request.method == 'POST':
      query = request.POST['p']
      loc = add_job.objects.filter(location=query)
    else:
      query = ""
      loc = None
      messages.success(request,"No match found")

    return render(request,'userjob.html', {'locs':loc})
def search_internship1(request):
    if request.method == 'POST':
      query = request.POST['q']
      results = add_internship.objects.filter(internship_title=query)
    else:
      query = ""
      results = None
      messages.success(request,"No match found")

    return render(request,'userinternship.html', {'results':results})
def searchinternshiplocation1(request):
    if request.method == 'POST':
      query = request.POST['p']
      loc = add_internship.objects.filter(location=query)
    else:
      query = ""
      loc = None
      messages.success(request,"No match found")
    return render(request, 'userinternship.html', {'locs': loc})

def testimonialinfo(request):
    if request.method=="POST":
        user_name=request.POST['user_name']
        location=request.POST['location']
        review=request.POST['review']
        uploads = request.POST['uploads']



        Testimonial(user_name=user_name,
                       location=location,review=review,
                       uploads=uploads,
                       ).save()
        messages.success(request,"Message Sent Succesfully.")
    else:
        return  render(request,"index.html")



def forgot(request):

        if request.method == "POST":
            try:
               em = request.POST.get("email")
               email_check = Customer.objects.get(email=em)
               data = {"email_check" : email_check}
               data1 = email_check.email
               global val
               def val():
                   return data1
               return render(request, "new_password.html")

            except Customer.DoesNotExist:
                messages.success(request,"Email does not exist!!!")
                return render(request, "login.html")

        return render(request,"forgetpassword.html")

def new_password(request):
    if request.method == "POST":
      data = val()
      print(data)
      a = Customer.objects.get(email=data)
      if request.POST.get("password") ==request.POST.get("cpassword"):

          a.password = request.POST.get("password")

          a.save()
          messages.success(request,"Password Change Successfully")
          return HttpResponseRedirect("/login")
      else:
           messages.success(request,"Password Not Match")
           return render(request,"new_password.html")



def company_forgot(request):
        if request.method == "POST":
            try:
              em = request.POST.get("email")
              email_check = company_profile.objects.get(email=em)
              data = {"email_check": email_check}
              data1 = email_check.email
              global val

              def val():
                     return data1


              return render(request, "company_new_passowrd.html")
            except company_profile.DoesNotExist:
                       messages.success(request, "Email does not exist!!!")
                       return render(request, "companylogin.html")



        return render(request, "companyforgetpassword.html")

def resumedata(request):
    if request.method == "POST":
        name = request.POST.get('name')   
        title = request.POST.get('personaltitle')   
        email =request.POST.get('email')
        city = request.POST.get('city')
        country = request.POST.get('country')
        address = request.POST.get('address')
        pnumber = request.POST.get('pnumber')
        summary = request.POST.get('summary')
        jobtitle = request.POST.get('jobtitle')   
        company =request.POST.get('company')
        workmode = request.POST.get('workmode')
        workcountry = request.POST.get('workcountry')
        startdate =request.POST.get('startdate')
        enddate = request.POST.get('enddate')
        jobdesc = request.POST.get('jobdesc')
        workhere = request.POST.get('workhere')
        degree = request.POST.get('degree')
        institudename = request.POST.get('institudename')   
        graduationdate = request.POST.get('graduationdate')
        edesc = request.POST.get('edesc')
        skill1 = request.POST.get('skill1')   
        skill2 = request.POST.get('skill2')   
        skill3 = request.POST.get('skill3')   
        skill4 = request.POST.get('skill4')   
        skill5 = request.POST.get('skill5')   
        skill6 = request.POST.get('skill6')
        Index = resume(name=name,title=title,email=email,address=address,city=city,country=country,
        pnumber=pnumber,summary=summary,jobtitle=jobtitle,company=company,
        workmode=workmode,workcountry=workcountry,startdate=startdate,enddate=enddate,jobdesc=jobdesc,
        workhere=workhere,degree=degree,institudename=institudename,graduationdate=graduationdate,
        edesc=edesc,skill1=skill1,skill2=skill2,skill3=skill3,skill4=skill4,skill5=skill5,skill6=skill6).save()
        message.success(request,"Your Resume is Ready!!! You can Download Now.")
        return HttpResponseRedirect('/resumetemp')
    return render(request,"makeresume.html")

def resumetemp(request):
    resumedata = resume.objects.all()
    return render(request,"resumetemp.html",{"resumedata" : resumedata})

def company_new_password(request):
    if request.method == "POST":
        data = val()
        print(data)
        a = company_profile.objects.get(email=data)
        if request.POST.get("password") == request.POST.get("cpassword"):
            a.password = request.POST.get("password")
            a.save()
            messages.success(request, "Password Change Successfully")
            return HttpResponseRedirect("/companylogin")
        else:
            messages.success(request, "Password Not Match")
            return render(request, "company_new_passowrd.html")
    return render(request, "company_new_passowrd.html")
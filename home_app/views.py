from django.shortcuts import render
from .models import Home, Statistics, AboutMe, Skill, Service, Project, Comment, Message

def home(request):
    home = Home.objects.all().last()
    statistics = Statistics.objects.all().last()
    about_me = AboutMe.objects.all().last()
    skills = Skill.objects.all()
    services = Service.objects.all()
    projects = Project.objects.all()
    comments = Comment.objects.all()

    if request.method == 'POST':
        fname = request.POST.get('name')
        lname = request.POST.get('family')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        body = request.POST.get('body')
        if fname and lname and email and phone and body:
            Message.objects.create(first_name=fname, last_name=lname, email=email, phone=phone, body=body)

    return render(request, 'index.html', context={'home': home, 'statis': statistics, 'about': about_me,
                                                  'skills': skills, 'services': services, 'projects': projects,
                                                  'comments': comments})

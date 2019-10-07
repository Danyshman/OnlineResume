from django.shortcuts import render


def index(request):
    return render(request, 'about.html')


def education(request):
    return render(request, 'education.html')


def experience(request):
    return render(request, 'experience.html')


def skills(request):
    return render(request, 'skills.html')

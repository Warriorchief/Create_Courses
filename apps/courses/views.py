from django.shortcuts import render, redirect, HttpResponse
from .models import Course
from django.contrib import messages

def index(request):
    if Course.objects.all().exists():
        context = {"courses" : Course.objects.all()}
        return render(request, "courses/index.html", context)
    return render(request, "courses/index.html")


def newCourse(request):
    if request.POST['course_name'] and request.POST['course_description']:
        course = request.POST['course_name']
        description = request.POST['course_description']
        if not Course.objects.filter(course_name=course):
            Course.objects.create(course_name=course, course_description=description)
        else:
            mistake = "that course is already listed here!"
            messages.error(request, mistake)
            return redirect('/')
    return redirect('/')

def destroy(request,id):
    Course.objects.filter(id=id).delete()
    return redirect('/')

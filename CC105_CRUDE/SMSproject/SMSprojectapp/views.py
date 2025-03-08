from django.shortcuts import render, redirect
from .models import StudentID

# Create your views here.
def ADD (request):
    Student = StudentID.objects.all()
    context = {'Student': Student}
    return render(request, "django/ADD.html", context)

def EDIT (request):
    return render(request, "django/EDIT.html")

def addstudent(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    dateofbirth = request.POST['dateofbirth']
    course = request.POST['course']
    enrollmentdate = request.POST['enrollmentdate']

    newStudent = StudentID(
        firstname = firstname,
        lastname = lastname,
        email = email,
        dateofbirth = dateofbirth,
        course = course,
        enrollmentdate = enrollmentdate,
    )
    newStudent.save()
    
    return redirect("/SMSprojectapp/")

def editstudent(request, id):
    Student = StudentID.objects.get(id=id)
    context = {'Student': Student}

    return render(request, "django/EDIT.html", context)

def updatestudent(request, id):
    Student = StudentID.objects.get(id=id)

    Student.firstname = request.POST['firstname']
    Student.lastname = request.POST['lastname']
    Student.email = request.POST['email']
    Student.dateofbirth = request.POST['dateofbirth']
    Student.course = request.POST['course']
    Student.enrollmentdate = request.POST['enrollmentdate']
    Student.save()

    return redirect("/SMSprojectapp/")

def deletestudent(request, id):
    Student = StudentID.objects.get(id=id)
    Student.delete()

    return redirect("/SMSprojectapp/")
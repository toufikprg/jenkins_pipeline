from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.role == 'admin':
                return redirect('admin_dashboard')

            elif user.role == 'teacher':
                return redirect('teacher_dashboard')

            elif user.role == 'student':
                return redirect('student_dashboard')

        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'auth/login.html')


def admin_dashboard(request):
    return render(request, 'dashboards/admin.html')

def teacher_dashboard(request):
    return render(request, 'dashboards/teacher.html')

def student_dashboard(request):
    return render(request, 'dashboards/student.html')

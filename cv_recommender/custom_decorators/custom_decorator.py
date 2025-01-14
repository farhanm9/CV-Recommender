from django.http import HttpResponse
from django.shortcuts import render, redirect


def unauthenticated_user(view_function):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.is_authenticated:
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                print('group:', group)
            print('group1:', group)
            if group == 'applicant':
                return redirect('applicantdashboard')
            if group == 'recruiter':
                return redirect('recruiterdashboard')
        else:
            return view_function(request, *args, **kwargs)

    return wrapper_function


def allowed_users(allowed_group=[]):
    def decorator(view_function):
        def wrapper_function(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            print('group2:', group)
            if group in allowed_group:
                return view_function(request, *args, **kwargs)
            else:
                if group == 'applicant':
                    return redirect('applicantdashboard')
                if group == 'recruiter':
                    return redirect('recruiterdashboard')

                # return HttpResponse("If you are not Logged In, Login first to view this page.\
                # if you are logged In already You are not ALLOWED to view this page.")
        return wrapper_function

    return decorator

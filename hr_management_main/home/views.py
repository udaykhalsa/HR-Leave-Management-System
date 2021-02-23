from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from .forms import LeaveApplicationForm, LeaveListForm
from .models import LeaveApplication, LeaveList

@login_required(login_url='login/')
def home_view(request):
    if request.user.is_superuser:
        return render(request, 'home/home_admin.html')
    else:
        return render(request, 'home/home_employee.html')

@login_required(login_url='login/')
def apply_leave_view(request):
    user = request.user
    form = LeaveApplicationForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save(user)
        return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'home/apply_leave.html', context)

@login_required(login_url='login/')
def leave_status_view(request):
    status = LeaveList.objects.filter(user=request.user)
    pending_status = LeaveApplication.objects.filter(user=request.user)
    context = {
        'status': status,
        'pending_status': pending_status
    }
    return render(request, 'home/leave_status.html', context)

@login_required(login_url='login/')
def applications_view(request):
    if request.user.is_superuser:
        applications = LeaveApplication.objects.all()
        leave_status = LeaveList()
        if request.method == "POST":
            id = request.POST.get('applications_id')
            leave_application_obj = LeaveApplication.objects.get(id=id)
            leave_status.user = leave_application_obj.user
            leave_status.reason = leave_application_obj.reason
            leave_status.from_date = leave_application_obj.from_date
            leave_status.to_date = leave_application_obj.to_date
            if request.POST.get('approve'):
                leave_status.leave_status = 'Approved'
            if request.POST.get('deny'):
                leave_status.leave_status = 'Denied'
            LeaveApplication.objects.filter(id=id).delete()
            leave_status.save()   
        context = {
            'applications': applications
        }
        return render(request, 'home/applications.html', context)
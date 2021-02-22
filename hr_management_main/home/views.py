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
        user = request.user
        form = LeaveApplicationForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save(user)
            return redirect('home')
        context = {
            'form': form
        }
        

        return render(request, 'home/home_employee.html', context)


@login_required(login_url='login/')
def applications_view(request):
    if request.user.is_superuser:
        applications = LeaveApplication.objects.all()
        if request.method == "POST":
            id = request.POST.get('applications_id')
            user = request.POST.get('applications_user')
            reason = request.POST.get('applications_reason')
            from_date = request.POST.get('applications_from_date')
            to_date = request.POST.get('applications_to_date')
            if request.POST.get('approve'):
                LeaveApplication.objects.filter(id=id).delete()
                something = LeaveList(user=user, reason=reason, from_date=from_date,
                 to_date=to_date, leave_status='Approve')
                leave_list_form = LeaveListForm(request.POST, instance=something)
                if leave_list_form.is_valid():
                    leave_list_form.save()             
            elif request.POST.get('deny'):
                something = LeaveList(user=user, reason=reason, from_date=from_date,
                 to_date=to_date, leave_status='Denied')
                leave_list_form = LeaveListForm(request.POST, instance=something)
                if leave_list_form.is_valid():
                    leave_list_form.save()          
        context = {
            'applications': applications
        }
        return render(request, 'home/applications.html', context)